from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from .models import Show
from time import strftime
from django.contrib import messages
from datetime import date

def shows(request):
  context = {
    'shows': Show.objects.all()
  }
  return render(request, 'shows.html', context)

def shows_new(request):
  context = {
    'today': str(date.today())
  }
  return render(request, 'shows_new.html', context)

def create(request):
  if request.method == "POST":
    print('🆕', request.POST)
    
    errors = Show.objects.getErrors(request.POST)
    
    if errors:
      print('\n*'*4,'ERRORS 🛑\n')
    else:
      print('\n*'*4,'NO errors ✅\n')
    
    if len(errors) > 0:
      print('\n*'*4,'ERRORS 🛑\n')
      for key_category, message_value in errors.items():
        messages.error(request, message_value, extra_tags=key_category)
      return redirect('/shows/new')
    else:
      title = request.POST['title']
      network = request.POST['network']
      release_date = request.POST['release_date']
      desc = request.POST['desc']
    
      Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    
      just_created_show_id = Show.objects.last().id 
      return redirect(f'/show/{just_created_show_id}')
  else:
    return redirect('/shows/new')



def show(request, show_id):
  context= {
    'this_show' : Show.objects.get(id=show_id)
  }
  return render(request, 'show.html', context)

def edit(request, show_id):
  # how the edit screen get the show 
  # DATETIME!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  context = {
    'this_show' : Show.objects.get(id=show_id)
  }
  print('\n---'*10)
  print(context['this_show'].release_date)
  print(type(context['this_show'].release_date))
  
  rd = Show.objects.get(id=show_id).release_date
  rd2 = rd.strftime('%Y-%m-%d')
  
  print('\n-'*2)
  print(rd2)
  print(type(rd2))
  
  context = {
    'this_show' : Show.objects.get(id=show_id),
    'rd' : rd2
  }
  return render(request, 'edit.html', context)

def update(request, show_id):
  if request.method == "POST":
    
    errors = Show.objects.getErrors(request.POST)
    
    if errors:
      print('\n*'*4,'ERRORS 🛑\n')
      for key_category, message_value in errors.items():
        messages.error(request, message_value, extra_tags=key_category)
        return redirect('/show/'+str(show_id)+'/edit')
    else:
      print('\n*'*4,'NO errors ✅\n')
      this_show = Show.objects.get(id=show_id)
      this_show.title = request.POST['title']
      this_show.network = request.POST['network']
      this_show.release_date = request.POST['release_date']
      this_show.desc = request.POST['desc']
      this_show.save()
      return redirect('/show/'+str(show_id))
  else :
    return redirect('/show/'+str(show_id)+'/edit')

def destroy(request, show_id):
  Show.objects.get(id=show_id).delete()
  return redirect('/')