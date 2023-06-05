# import datetime
from django.db import models

c_choices = (
    (0, "ноль"),
    (10, "десять"),
    (15, "пятнадцать"),
    (20, "двадцать"),
)


class Abc(models.Model):
    task = models.CharField(verbose_name="Формулировка  задачи", default="1/(XY) равно ?", max_length=255)
    x = models.IntegerField(verbose_name="Значение X", default=0, )
    y = models.IntegerField(verbose_name="Значение Y", default=0, help_text="Подсказка для поля Y")
    z = models.IntegerField(verbose_name="Значение Z", choices=c_choices, default=0, )
    current_date = models.DateTimeField(verbose_name="Дата изменения(save)", auto_now=True)

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"{self.id}&{self.task}"


    class Meta:
        verbose_name = "Z_Y_Z"
        verbose_name_plural = "X_Y_Z_S"
        ordering = ('-id', '-x')




# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)


# python manage.py makemigrations
# python manage.py migrate


# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']
