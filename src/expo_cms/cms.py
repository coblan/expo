from helpers.case.simcms.base_page import BasePage
from helpers.case.simcms.base_data import cms_page
from helpers.director.shortcut import director

class Home(BasePage):
    def getTemplate(self): 
        return 'expo_cms/home.html'
    
    @classmethod
    def get_heads(cls): 
        return [
            {'name': 'hello', 'label': '汉化','editor': 'linetext',}, 
            {'name': 'danyuan', 'label': '但愿','editor': 'linetext',}
                
        ]



director.update({
    'simcms.page.home': Home,
})

cms_page.update({
    'expo_cms_home': Home,
})