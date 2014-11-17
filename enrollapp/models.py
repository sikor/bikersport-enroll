from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
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

    def __str__(self):
        return self.name + ("(open)" if self.is_open else "(closed)")


class Term(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, through='Enrollment', related_name="terms")
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(Event, related_name="terms")

    def __str__(self):
        if len(self.participants.all()):
            status = ', '.join(user.first_name for user in self.participants.all())
        else:
            status = "Pusty"
        return "%s (%s) %s" % (self.name, status, self.starttime.time())


class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name="enrollments")
    term = models.ForeignKey(Term, related_name="enrollments")

    class Meta:
        unique_together = ('user', 'term')
