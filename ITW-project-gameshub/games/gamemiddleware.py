from .models import launch,popular,description,genres,logo
from django.shortcuts import render
from django.http import HttpResponseRedirect
class GetGame:
	def __init__(self,get_response):
		self.get_response=get_response
	def __call__(self, request):
		
		a=self.get_response(request)
		if (a.status_code!=404):
			return a
		else:
			return render(request,'games/myown404.html',{})