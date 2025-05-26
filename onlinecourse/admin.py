from django.contrib import admin
# Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Register QuestionInline and ChoiceInline classes here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 2

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ['content']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register Question and Choice models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)