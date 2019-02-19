from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.course_name


class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.department_name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.age)

    class Meta:
        abstract = True


class Student(Person):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % self.course


class Teacher(Person):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % self.department
