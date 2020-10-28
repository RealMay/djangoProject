from django.shortcuts import render
from student.models import Student
from django.http import JsonResponse
import json
from django.db.models import Q


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


def query_students(request):
    """查询学生信息"""
    # 接收传递过来的查询条件
    data = json.loads(request.body.decode(encoding="utf-8"))
    try:
        # 获取所有满足条件的学生信息
        obj_students = Student.objects.filter(
            Q(sno__icontains=data['inputstr']) | Q(name__icontains=data['inputstr']) | Q(
                gender__icontains=data['inputstr']) | Q(mobile__icontains=data['inputstr']) | Q(
                email__icontains=data['inputstr']) | Q(address__icontains=data['inputstr'])).values()
        # 结果转换为标准list
        student = list(obj_students)
        return JsonResponse({'code': 1, 'data': student})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询学生信息错误出现异常，具体错误：" + str(e)})
