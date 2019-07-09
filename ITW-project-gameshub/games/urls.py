from django.contrib import admin
from django.urls import path
from project.latestfeed import PopularFeed
from . import views
urlpatterns = [
	path('about',views.about,name='about'),#about page
    path('',views.index,name='index'),# home page
    path('contact',views.contact,name='contact'),# contact page
    path('latest',views.lall,name='latestall'),# latest page
    path('popular',views.pall,name='popularall'),# popular page
    path('latest/<str:choice>',views.lfilter,name='latestfilter'),# latest page with filter of a given genre
    path('popular/feed',PopularFeed()),# feed of Top 5 game
    path('popular/<str:choice>',views.pfilter,name='popularfilter'),# popular page with filter of a given genre
    path('<str:gamename>',views.singlep,name='gamepage'), #single page of a particular game
]
