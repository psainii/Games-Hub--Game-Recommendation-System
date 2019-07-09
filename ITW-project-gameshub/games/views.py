from django.shortcuts import render,get_object_or_404
from games.models import launch,logo,description,popular,genres,response
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
def index(request):  # view for home page
	return render(request,'games/index.html',{})
def about(request): # view for about page
	return render(request,'games/about.html',{})
def contact(request):# feedback form system
	if (request.method=='POST'):
		v1=response(name=str(request.POST.get("Name")),phoneno=int(request.POST.get("Phone Number")),email=str(request.POST.get("Email")),message=str(request.POST.get("Message")),)
		v1.save()
		return HttpResponseRedirect('/games') #redirecting to home page
	else:
		return render(request,'games/contact.html',context={})
def lall(request): # latest games showing all games
	with connection.cursor() as cursor:
		cursor.execute('select T.link,U.name from games_logo as T,games_launch as U where T.name_id=U.name order by U.year desc;')
		l1=cursor.fetchall()
	return render(request,'games/latestgames.html',context={'logos':l1,'c':'all'})
def lfilter(request,choice): # latest games showing games of the 'choice' genre
	l2=(('arcade','arcade'),('action','action'),('racing','racing'),('puzzle','puzzle'),('strategy','strategy'),('sports','sports'),('war','war'),)
	if (choice,choice) not in l2:
		return render(request,'games/myown404.html') # if genre not found raising 404 error
	with connection.cursor() as cursor:
		cursor.execute('select T.link,U.name from games_logo as T,games_launch as U, games_genres as F where T.name_id=U.name and T.name_id=F.name_id and F.genre=%s order by U.year desc;',[choice])
		l1=cursor.fetchall()
	return render(request,'games/latestgames.html',context={'logos':l1,'c':choice})
def pfilter(request,choice): #popular games showing games of the 'choice' genre
	l2=(('arcade','arcade'),('action','action'),('racing','racing'),('puzzle','puzzle'),('strategy','strategy'),('sports','sports'),('war','war'),)
	if (choice,choice) not in l2:
		return render(request,'games/myown404.html') # if genre not found raising 404 error
	with connection.cursor() as cursor:
		cursor.execute('select T.link,U.name_id,U.votes from games_logo as T,games_popular as U, games_genres as F where T.name_id=U.name_id and T.name_id=F.name_id and F.genre=%s order by U.votes desc;',[choice])
		l1=cursor.fetchall()
	return render(request,'games/populargames.html',context={'logos':l1,'c':choice})
def pall(request): # popular games showing all games
	with connection.cursor() as cursor:
		cursor.execute('select T.link,U.name_id,U.votes from games_logo as T,games_popular as U where T.name_id=U.name_id order by U.votes desc')
		l1=cursor.fetchall()
		return render(request,'games/populargames.html',context={'logos':l1,'c':"all"})
@csrf_exempt
def singlep(request,gamename): # individual page of games
	if (request.method=='POST'):
		# post method called by javascript to increase or decrease votes of games
		a=request.POST["gamen"]
		l=popular.objects.get(name=a)
		l.votes=l.votes+int(request.POST["flag"])
		l.save()
		return JsonResponse({"a":"b"})
	#l1 having details of the game in this specific order.
	#0. name
	#1. company
	#2. year
	#3. genre
	#4. description
	l1=[]
	l=get_object_or_404(launch,name=gamename)
	l1.append(l.name)
	l1.append(l.company)
	l1.append(l.year)
	l2=genres.objects.get(name=gamename)
	l1.append(l2.genre)
	l3=description.objects.get(name=gamename)
	l1.append(l3.description)
	l4=logo.objects.get(name=gamename)
	l1.append(l4.link)
	return render(request,'games/single.html',context={'details':l1})
