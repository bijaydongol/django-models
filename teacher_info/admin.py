from teacher_info.models import Teacher_info
from django.contrib import admin
from .models import Teacher_info,student_info,AgentDetail
# Register your models here.
admin.site.register(Teacher_info)
admin.site.register(student_info)
admin.site.register(AgentDetail)