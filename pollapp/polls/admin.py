from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    """"The class representation of the choices for the question's admin interface"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """the class represenetation of the admin interface for question"""
    fieldsets = [(None, {"fields": ["question_text"]}), ("the publication date of the question", {"fields": ["pub_date"]})]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
