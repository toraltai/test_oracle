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
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE, null=True)
    adress = models.CharField(verbose_name='Адрес', max_length=100)
    sex = models.CharField(verbose_name='Пол', choices=SEX)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class School(models.Model):  #Школа
    name = models.CharField(verbose_name='Название школы', max_length=20)
    grade = models.ForeignKey('Grade', verbose_name='Класс', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = "Школы"

    def __str__(self):
        return f'{self.name}'
    

class Grade(models.Model):  #Класс
    name = models.CharField(verbose_name='Класс', max_length=20)
    teacher = models.ForeignKey(Teacher, related_name='teacher',verbose_name='Учитель', on_delete=models.CASCADE)
    students = models.ForeignKey(Student, related_name='students', verbose_name='Ученики',on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        
    def __str__(self):
        return f'{self.name}'