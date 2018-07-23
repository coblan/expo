from django.contrib import admin
from helpers.director.shortcut import page_dc
# Register your models here.
class Home(object):
    template='expo_cms/home.html'
    def __init__(self, request, **kws):
        pass
    def get_context(self):
        return {}
    
page_dc.update({
    'home':Home
})
