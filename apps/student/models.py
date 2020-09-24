from django.db import models


# Create your models here.


class Student(models.Model):
    gender_choice = (('男', '男'), ('女', '女'))
    sno = models.IntegerField(db_column="SNo", primary_key=True, null=False)
    name = models.CharField(db_column="SName", max_length=100, null=False)
    gender = models.CharField(db_column="Gender", max_length=100, choices=gender_choice)
    birthday = models.DateField(db_column="Birthday", null=False)
    mobile = models.CharField(db_column="Mobile", max_length=100)
    email = models.CharField(db_column="Email", max_length=100)
    address = models.CharField(db_column="Address", max_length=200)
    image = models.CharField(db_column="Image", max_length=200, null=True)

    # 自定义生成表名
    class Mete:
        managed = True
        db_table = "Student"

    def __str__(self):
        return "学号:%s\t姓名:%s\t性别:%s" % (self.sno, self.name, self.gender)
