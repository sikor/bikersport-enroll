from django.contrib import admin

# Register your models here.
from enrollapp.models import Event, Term, UserDetails


class TermInline(admin.TabularInline):
    model = Term
    extra = 10

class EventAdmin(admin.ModelAdmin):
    inlines = (TermInline,)

admin.site.register(Event, EventAdmin)
admin.site.register(Term)
admin.site.register(UserDetails)