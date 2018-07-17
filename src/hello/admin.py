from helpers.director.shortcut import page_dc
from . import permit

class Home(object):
    template='hello/home.html'
    def __init__(self,request, par_url):
        pass
    def get_context(self):
        return {}

page_dc.update({
    'home':Home
})