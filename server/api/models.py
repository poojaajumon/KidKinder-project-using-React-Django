from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_class = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    teacher_image = models.ImageField(upload_to='images/')
    teacher_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name


class Classes(models.Model):
    classes_image = models.ImageField(upload_to='images/')
    classes_topic = models.CharField(max_length=100)
    classes_details = models.CharField(max_length=300)

    def __str__(self):
        return self.classes_topic


