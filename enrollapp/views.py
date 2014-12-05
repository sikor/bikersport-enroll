from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from enrollapp.models import Event, Term, Enrollment, UserDetails


class EnrollmentForm(forms.ModelForm):
    rules = forms.BooleanField(label='',
                               required=True)

    class Meta:
        model = Enrollment
        fields = ['term', 'rules', 'user']

    def __init__(self, *args, **kwargs):
        self.request_event = kwargs.pop("event")
        self.request_user = kwargs.pop("user")
        super(EnrollmentForm, self).__init__(*args, initial={'user': self.request_user}, **kwargs)
        terms = Term.objects.filter(event=self.request_event)
        choices = []
        for term in terms:
            if term.participants.count() < 2:
                choices.append((term.id, str(term)))
        self.fields['term'].choices = tuple(choices)

    def clean_user(self):
        return self.request_user


def get_user_details_form(request):
    if len(UserDetails.objects.filter(user=request.user.id)) > 0:
        user_form = UserDetailsForm(instance=request.user.details)
    else:
        user_form = UserDetailsForm()
    return user_form


def get_user_term(event, request):
    term = None
    if request.user.is_active:
        terms = Term.objects.filter(event=event, participants=request.user)
        if len(terms) > 0:
            term = terms[0]
    return term


def render_event(request, urlname, enroll_form=None, user_form=None, event=None):
    event = event or Event.objects.get(urlname=urlname)
    user_form = user_form or get_user_details_form(request)
    form = enroll_form or EnrollmentForm(event=event, user=request.user)
    term = get_user_term(event, request)
    return render(request, 'enrollapp/event.html', {'event': event, 'user': request.user, 'enroll_form': form,
                                                    'term': term, 'user_form': user_form})


def event(request, urlname):
    return render_event(request, urlname)


def index(request):
    events = Event.objects.all()
    return render(request, 'enrollapp/index.html', {'events': events})


@login_required
def enroll_user(request, urlname):
    event = Event.objects.get(urlname=urlname)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, event=event, user=request.user)
        if form.is_valid():
            form.save()
        else:
            return render_event(request, urlname, enroll_form=form, event=event)
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
        if UserDetails.objects.filter(user=user).count() > 0:
            form = UserDetailsForm(request.POST, instance=request.user.details)
        else:
            form = UserDetailsForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = user
            details.save()
        else:
            return render_event(request, urlname, user_form=form)

    return redirect('event', urlname)