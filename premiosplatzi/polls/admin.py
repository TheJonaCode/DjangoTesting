from django.contrib import admin
from . models import Question


class ChoiceInline(admin.StackedInline):
    model = Choices
    extra: 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'questiontext']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)