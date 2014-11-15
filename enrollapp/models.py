from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class UserDetails(models.Model):
    user = models.ForeignKey(User, related_name="details")
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female')))

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
    participant = models.ForeignKey(User, related_name="terms")
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    event = models.ForeignKey(Event, related_name="terms")

    def __str__(self):
        if self.participant is not None:
            status = self.participant.username
        else:
            status = "free"
        return "%s (%s, %s, %s)" % (self.name, self.starttime, self.endtime, status)


