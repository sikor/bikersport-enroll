from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.



def validate_weight(value):
    if value < 30:
        raise ValidationError('Za mała waga.')


def validate_height(value):
    if value < 50:
        raise ValidationError('Za mały wzrost')


class UserDetails(models.Model):
    user = models.OneToOneField(User, related_name="details")
    weight = models.IntegerField(_("Waga [kg]"), validators=[validate_weight])
    height = models.IntegerField(_("Wzrost [cm]"), validators=[validate_height])
    age = models.IntegerField(_("Wiek"), blank=True, null=True)
    sex = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female')), blank=True, null=True)

    def __str__(self):
        return self.user.username


class Event(models.Model):
    name = models.CharField(max_length=100)
    urlname = models.CharField(max_length=30, unique=True)
    is_open = models.BooleanField(default=False)
    close_time = models.DateTimeField(blank=True, null=True)

    def is_enrollment_open(self):
        if self.close_time is None:
            return self.is_open
        return self.close_time > timezone.now() and self.is_open


    def __str__(self):
        return self.name + ("(open)" if self.is_open else "(closed)")


class Term(models.Model):
    MAX_USERS_PER_TERM = 2
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, through='Enrollment', related_name="terms")
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(Event, related_name="terms")

    def slots_remaining(self):
        return max(0, Term.MAX_USERS_PER_TERM - len(self.participants.all()))

    def __str__(self):
        if len(self.participants.all()):
            status = ', '.join(user.first_name for user in self.participants.all())
        else:
            status = "Pusty"

        if self.starttime is not None:
            return "%s - %s" % (self.name, self.starttime.time())
        else:
            return self.name


class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name="enrollments")
    term = models.ForeignKey(Term, verbose_name=_('Termin'), related_name="enrollments")

    def clean(self):
        if self.term.event is None or not self.term.event.is_enrollment_open():
            raise ValidationError('Nie można zapisać się na zamknięte wydarzenie.')

        user_terms = Term.objects.filter(event=self.term.event, participants=self.user).count()
        if user_terms != 0:
            raise ValidationError('Jesteś już zapisany na to wydarzenie.')

        if self.term.participants.count() >= Term.MAX_USERS_PER_TERM:
            raise ValidationError('Brak wolnych miejsc w tym terminie.')

        if UserDetails.objects.filter(user=self.user).count() == 0:
            raise ValidationError('Zanim się zapiszesz musisz uzupełnić dane do konfiguracji trenażera.')

    class Meta:
        unique_together = ('user', 'term')
