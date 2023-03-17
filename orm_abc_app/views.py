import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateAbcForm
from .models import Abc


def index(request):
    return render(request, 'index.html')


class AbcFormCreate(forms.Form):
    a = forms.IntegerField(initial=1, min_value=2)
    b = forms.IntegerField(required=False)
    c = forms.IntegerField(label='c_lable' )

def abc_form(request):
    abc_form = AbcFormCreate()
    print(abc_form)
    return render(request, 'abc_form.html', {"abc_form": abc_form})


def abc_get(request):
    print(request.GET)
    print(request.GET.get("a"))
    print(request.GET.get("b"))
    print(request.GET.get("c"))
    A = request.GET.get("a")
    B = request.GET.get("b")
    C = request.GET.get("c")
    return HttpResponse(f"""
    <pre>
    A = {A}
    B = {B}
    C = {C}
    </pre>
    """)


# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)


def datetime_nov(request):
    datetime_now = datetime.datetime.now()
    print(datetime_now)
    context = {'key': datetime_now}
    return render(request, 'datetime_now.html', context)


def list_dict(request):
    list_main = (1, 2, 3, 4, 5)
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {'list_main': list_main, 'dict_main': dict_main}  # будем передавать в шаблон как один общий объект
    return render(request, 'list_main.html', context)


def form_create_0(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("\nform_post_valid:\n", form)
            return redirect('orm_abc_app:form_result')
    else:
        print("else:\n")
        form = CreateAbcForm()
    print('\nform_else:\n', form)

    print('\nform:\n', form)
    context = {
        'form': form
    }
    print("\ncontext1:\n", context)
    # return render(request, 'form_create.html', context)
    return render(request, 'form_create_0.html', context)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            form.save()
            print("\norm_post_valid:\n", form)
            return redirect('orm_abc_app:form_result')
    else:
        print("else:\n")
        form = CreateAbcForm()
    print('\nform_else:\n', form)

    context = {
        'form': form
    }
    print("\ncontext:\n", context)
    # return render(request, 'form_create.html', context)
    return render(request, 'form_create.html', context)


def form_result(request):
    rows = Abc.objects.all()
    print("rows:\n", rows)
    row = list(Abc.objects.values_list())[-1]
    print("row: \n", row)
    if row[2] + row[3] == row[4]:
        result = " С равна сумме A и B"
    else:
        result = "С не равна сумме A и B"
    last_data = [row[2], row[3], row[4], result]
    print('last_data:\n', last_data)
    task_main = list()
    task_main.append(row[1])
    print('task_form_abc_app:\n', task_main, 'last_data: ', last_data, '\n')
    context = {'task_main': task_main, 'last_data': last_data}
    return render(request, 'form_result.html', context)


def table(request):
    # print ((Abc.))
    rows = Abc.objects.values_list()
    print(rows)
    context = {'rows': rows}
    return render(request, 'table.html', context)
