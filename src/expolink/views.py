from django.shortcuts import render

from django.views.generic.base import View
from helpers.director.engine import BaseEngine

# Create your views here.

class Home(View):
  
    def get(self,request):
        baseengine = BaseEngine()
        baseengine.request = request
        page_data ={}
        if request.user.is_authenticated():
            page_data['username']=request.user.username
        ctx={
            'page_data':page_data,
            'js_config':baseengine.getJsConfig()
        }
        template = self.get_template()
        return render(request,template,context=ctx)        
    
    def get_template(self):
        return 'expolink/index.html'
    

class D3(Home):
    def get_template(self):
        return 'expolink/3d.html'
    

class VR(Home):
    def get_template(self):
        return 'expolink/vr.html'

class FullScreen(Home):
    def get_template(self):
        return 'expolink/fullscreen.html'

#def home(request):
    #page_data ={}
    #if request.user.is_authenticated():
        #page_data['username']=request.user.username
    #ctx={
        #'page_data':page_data
    #}
    #return render(request,'expolink/index.html',context=ctx)

