from helpers.case.simcms.base_page import BasePage, BaseTabFields
from helpers.case.simcms.base_data import cms_page
from helpers.director.shortcut import director, ModelFields

class Home(BasePage):
    def getTemplate(self): 
        return 'expo_cms/home.html'
    
    def get_heads(self): 
        return [
            {'name': 'hello', 'label': '汉化','editor': 'linetext',}, 
            {'name': 'danyuan', 'label': '但愿','editor': 'linetext',}  
        ]
    
    def get_tabs(self):
        baseinfo = BaseInfo(crt_user = self.request.user)
        base2 =  BaseInfo2(crt_user = self.request.user)
        ls = [
            {'name':'baseinfo',
             'label':'基本信息',
             'com':'com_tab_fields',
             'get_data':{
                 'fun':'get_row',
                 'kws':{
                    'director_name':BaseInfo.get_director_name(),
                    'relat_field':'pk',              
                 }
             },
             'after_save':{
                 #'fun':'update_or_insert'
                 #'fun':'do_nothing'
                 'fun':'update_par_row_from_db'
             },
             'heads': baseinfo.get_heads(),
             'ops': baseinfo.get_operations()                 
             }, 
            #{'name':'baseinfo2',
             #'label':'基本信息2',
             #'com':'com_tab_fields',
             #'get_data':{
                 #'fun':'get_row',
                 #'kws':{
                    #'director_name':base2.get_director_name(),
                    #'relat_field':'pk',              
                 #}
             #},
             #'after_save':{
                 #'fun':'update_par_row_from_db'
             #},
             #'heads': base2.get_heads(),
             #'ops': base2.get_operations()                 
                  #}, 
        ]
        return ls

class BaseInfo(BaseTabFields):
    
    def get_heads(self): 
        return [
            {'name': 'slogan', 'label': '推广口号','editor': 'blocktext','style': 'width:30em;height:8em',}, 
            {'name': 'danyuan', 'label': '但愿','editor': 'linetext',},
            {'name':'pp','label':'测试标签','editor':'com-field-table-list',
             'table_heads':[{'name':'a','label':'显示一','editor':'com-table-pop-fields-local'},
                            {'name':'b','label':'显示二'}],
             'fields_heads':[{'name':'a','label':'显示一','editor':'linetext'},
                            {'name':'b','label':'显示二','editor':'linetext'}]
             }
        ]

class BaseInfo2(BaseTabFields):
    
    def get_heads(self): 
        return [
            {'name': 'bige', 'label': '逼格','editor': 'linetext',}, 
            {'name': 'danyuan', 'label': '但愿','editor': 'linetext',}  
        ]

    



director.update({
    'simcms.page.home': Home,
    'simcms.page.home.base': BaseInfo,
    'simcms.page.home.base2': BaseInfo2,
})

cms_page.update({
    'expo_cms_home': Home,
})