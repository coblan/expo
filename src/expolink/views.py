from django.shortcuts import render

from django.views.generic.base import View
from helpers.director.engine import BaseEngine
from .models import ZhanXunModel
from django.forms.models import model_to_dict
# Create your views here.

class Home(View):
  
    def get(self,request):
        self.request = request
        baseengine = BaseEngine()
        baseengine.request = request
        page_data ={}
        if request.user.is_authenticated():
            page_data['username']=request.user.username
        ctx={
            'page_data':page_data,
            'js_config':baseengine.getJsConfig()
        }
        ctx.update( self.extraCtx())
        template = self.get_template()
        return render(request,template,context=ctx)   
    
    def extraCtx(self):
        ls=[]
        for zhan in ZhanXunModel.objects.all():
            ls.append({'title':zhan.title,'pk':zhan.pk})
        return {
            'zhanxun':ls
        }
    
    def get_template(self):
        return 'expolink/index.html'
    
class Zhanxun(Home):
    def get_template(self):
        return 'expolink/zhanxun.html'
    
    def extraCtx(self):
        rows = ZhanXunModel.objects.all()
        rows = [model_to_dict(inst) for inst in rows]
        return {
            'rows': rows
        }

class Zhanxun2(Home):
    def get_template(self):
        return 'expolink/zhanxun2.html'
    
    def extraCtx(self):
        pk = self.request.GET.get('id')
        row = ZhanXunModel.objects.get(pk=pk)
        
        return  {
            'row':model_to_dict(row)
            }


class D3(Home):
    def get_template(self):
        return 'expolink/3d.html'
    

class VR(Home):
    def get_template(self):
        return 'expolink/vr.html'

class FullScreen(Home):
    def get_template(self):
        return 'expolink/fullscreen.html'


