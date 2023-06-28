from django.db import models
from users.models import Teacher

SEX = [
    ('male', 'Мужской'),
    ('female', 'Женский')
]

class Student(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=25)
    second_name = models.CharField(verbose_name='Фамилия', max_length=25)
    mail = models.EmailField(verbose_name='Почта', max_length=40)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    adress = models.CharField(verbose_name='Адрес', max_length=100)
    sex = models.CharField(verbose_name='Пол', choices=SEX)


class School(models.Model):  #Школа
    name = models.CharField(verbose_name='Название школы', max_length=20)
    grade = models.ForeignKey('Grade', verbose_name='Класс', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = "Школы"

    def __str__(self):
        return f'{self.name}'
    

class Grade(models.Model):  #Класс
    name = models.CharField(verbose_name='Класс', max_length=20)
    teacher = models.ForeignKey(Teacher, related_name='teacher', verbose_name='Учитель', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='students', verbose_name='Ученики', blank=True)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        
    def __str__(self):
        return f'{self.name}'