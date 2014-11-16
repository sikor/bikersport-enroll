from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from enrollapp.models import Event, Term, Enrollment, UserDetails


class EnrollForm(forms.Form):
    term = forms.ChoiceField(label="Termin")

    def __init__(self, *args, **kwargs):
        event = kwargs.pop("event")
        super(EnrollForm, self).__init__(*args, **kwargs)
        terms = Term.objects.filter(event=event)
        choices = []
        for term in terms:
            if len(term.participants.all()) < 2:
                choices.append((term.id, str(term)))
        self.fields['term'].choices = tuple(choices)




def event(request, urlname):
    event = Event.objects.get(urlname=urlname)
    form = EnrollForm(event=event)
    if len(UserDetails.objects.filter(user=request.user.id)) > 0:
        user_form = UserDetailsForm(instance=request.user.details)
    else:
        user_form = UserDetailsForm()
    term = None
    if request.user.is_active:
        terms = Term.objects.filter(event=event, participants=request.user)
        if len(terms) > 0:
            term = terms[0]
    return render(request, 'enrollapp/event.html', {'event': event, 'user': request.user, 'enroll_form': form,
                                                    'term': term, 'user_form': user_form})


def index(request):
    events = Event.objects.all()
    return render(request, 'enrollapp/index.html', {'events': events})


@login_required
def enroll(request, urlname):
    event = Event.objects.get(urlname=urlname)
    if request.method == 'POST':
        form = EnrollForm(request.POST, event=event)
        if form.is_valid():
            terms = Term.objects.filter(event=event, participants=request.user)
            if len(terms) == 0:
                term = Term.objects.get(pk=form.cleaned_data['term'])
                if len(term.participants.all()) < 2:
                    enrollment = Enrollment(user=request.user, term=term)
                    enrollment.save()
    return redirect('event', event.urlname)


@login_required
def unenroll(request, urlname):
    e = Event.objects.get(urlname=urlname)
    if request.method == 'POST':
        term = Term.objects.get(event=e, participants=request.user)
        enrollment = Enrollment.objects.get(user=request.user, term=term)
        enrollment.delete()
    return redirect('event', urlname)

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['weight', 'height']


@login_required
def user_details(request, urlname):
    user = request.user
    if request.method == 'POST':
        if len(UserDetails.objects.filter(user=user)) > 0:
            form = UserDetailsForm(request.POST, instance=request.user.details)
        else:
            form = UserDetailsForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = user
            details.save()

    return redirect('event', urlname)