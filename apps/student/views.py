from django.shortcuts import render
from student.models import Student
from django.http import JsonResponse


# Create your views here.

def get_students(request):
    # 使用orm获取所有学生信息
    try:
        obj_students = Student.objects.all().values()
        # 结果转换为标准list
        student = list(obj_students)
        return JsonResponse({'code': 1, 'data': student})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "获取学生信息错误出现异常，具体错误：" + str(e)})
