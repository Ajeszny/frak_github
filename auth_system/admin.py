from django.contrib import admin
from .models import Grade
from .models import LessonPlan


class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'date', 'time', 'lesson_type')
    list_filter = ('teacher', 'date', 'lesson_type')
    search_fields = ('teacher__username', 'lesson_type')


admin.site.register(LessonPlan, LessonPlanAdmin)
admin.site.register(Grade)
