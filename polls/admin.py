from django.contrib import admin

from .models import Question

#admin.site.register(Question)

# Define the admin class
class QuestionAdmin (admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text','pub_date')

# Register the admin class with the associated model
admin.site.register(Question, QuestionAdmin )