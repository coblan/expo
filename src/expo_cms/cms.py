from helpers.case.simcms.base_page import BasePage
from helpers.case.simcms.base_data import cms_page
from helpers.director.shortcut import director

class Home(BasePage):
    def getTemplate(self): 
        return 'expo_cms/home.html'
    
    def get_heads(self): 
        return [
            {'name': 'hello', 'label': '汉化','editor': 'linetext',}, 
            {'name': 'danyuan', 'label': '但愿','editor': 'linetext',}  
        ]
    
    def get_tabs(self):
        ls = [
            {'name':'basice',
             'label':'基本信息',
             'com':'com_tab_table',
             
             'get_data':{
                 'fun':'get_rows',
                 'kws':{
                    'model_name':model_to_name(TbTicketstake),
                    'relat_field':'ticketid',
                 }
                 
             },
             'heads_ctx':TicketstakeTable(crt_user=self.crt_user).get_head_context()  
             },

            {'name':'ticketparlay',
             'label':'串关规则',
             'com':'com_tab_table',
             'get_data':{
                 'fun':'get_rows',
                 'kws':{
                    'model_name':model_to_name(TbTicketparlay),
                    'relat_field':'ticketid',
                 }
                 
             },
             'heads_ctx':TicketparlayTable(crt_user=self.crt_user).get_head_context()
             }                   
        ]
        return ls
    
    


director.update({
    'simcms.page.home': Home,
})

cms_page.update({
    'expo_cms_home': Home,
})