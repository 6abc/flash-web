# flash-web

1. ## Create a New Django Project:
```sh
   django-admin startproject crud_app cd crud_app
```
2. ## Create a Model:** Create a file named `models.py` in the `crud_app` directory:
```sh
from django.db import models
class Person(models.Model):
   name = models.CharField(max_length=30)
   age = models.IntegerField()
```
3. ## Create a Migration:** Run the following command to create a migration:
```sh
python manage.py makemigrations
```
4. ## Apply the Migration:** Run the following command to apply the migration:
```sh
python manage.py migrate 
```
5. ##Create a Form:** Create a file named `forms.py` in the `crud_app` directory:
```sh
from django import forms
from .models import Person
class PersonForm(forms.ModelForm):
   class Meta: model = Person fields = ['name', 'age']
```
6. ##Create a View:** Create a file named `views.py` in the `crud_app` directory:
```sh
from django.shortcuts import render, redirect from django.urls
import reverse_lazy from .models
import Person from .forms
import PersonForm

def index(request):
   people = Person.objects.all()
   return render(request, 'index.html', {'people': people})
def create(request):
   if request.method == 'POST':
      form = PersonForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect(reverse_lazy('index')) else: form = PersonForm() return render(request, 'create.html', {'form': form})

def update(request, pk):
   person = Person.objects.get(pk=pk)
      if request.method == 'POST':
         form = PersonForm(request.POST, instance=person)
            if form.is_valid():
               form.save()
            return redirect(reverse_lazy('index'))
            else:
               form = PersonForm(instance=person)
            return render(request, 'update.html', {'form': form})
def delete(request, pk):
   person = Person.objects.get(pk=pk)
   if request.method == 'POST':
      person.delete()
   return redirect(reverse_lazy('index'))
   return render(request, 'delete.html', {'person': person})
``` 
7. ##Create Templates:** Create the following templates in the `templates` directory: * `index.html`:
```sh
html {% extends 'base.html' %} {% block content %} <h1>People</h1> <ul> {% for person in people %} <li>{{ person.name }} ({{ person.age }})</li> {% endfor %} </ul> <a href="{% url 'create' %}">Create New Person</a> {% endblock %} ``` * `create.html`: ```html {% extends 'base.html' %} {% block content %} <h1>Create New Person</h1> <form method="POST"> {% csrf_token %} {{ form.as_p }} <input type="submit" value="Create"> </form> {% endblock %} ``` * `update.html`: ```html {% extends 'base.html' %} {% block content %} <h1>Update Person</h1> <form method="POST"> {% csrf_token %} {{ form.as_p }} <input type="submit" value="Update"> </form> {% endblock %} ``` * `delete.html`: ```html {% extends 'base.html' %} {% block content %} <h1>Delete Person</h1> <p>Are you sure you want to delete {{ person.name }}?</p> <form method="POST"> {% csrf_token %} <input type="submit" value="Delete"> </form> {% endblock %}
``` 
8. ##Add URLs:** Add the following URLs in the `urls.py` file:
```sh
python from django.urls import path from . import views urlpatterns = [ path('', views.index, name='index'), path('create/', views.create, name='create'), path('update/<int:pk>/', views.update, name='update'), path('delete/<int:pk>/', views.delete, name='delete'), ]
``` 
9. ##Run the Server:** Run the following command to start the development server:
```sh
python manage.py runserver
``` 
10. ##Test the App:** Open your browser and navigate to
```sh
http://127.0.0.1:8000/`
```
You should see a list of people. You can click the "Create New Person" link to create a new person, the "Update" link to update an existing person, or the "Delete" link to delete a person.
