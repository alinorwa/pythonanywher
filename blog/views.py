from django.http import HttpResponse
from django.template import loader 
from .models import User
from django.shortcuts import redirect



def admin(request):
  return redirect('admin')

def home(request):
  users = User.objects.all().order_by('-id')
  template = loader.get_template('home.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))



def details(request, id):
  user = User.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'user': user,
  }
  return HttpResponse(template.render(context, request))