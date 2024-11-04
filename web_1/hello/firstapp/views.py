from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            (form.save())  # Сохранение данных в БД
            return redirect('success')  # Перенаправление на страницу успеха
    else:
        form = UserForm()
    return render(request, 'firstapp/user_form.html', {'form': form})