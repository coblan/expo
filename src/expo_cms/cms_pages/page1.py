from helpers.case.simcms.base_page import BasePage, BaseTabFields
from helpers.case.simcms.base_data import cms_page
from helpers.director.shortcut import director, ModelFields
import json

class Page1(BasePage):
    def getTemplate(self): 
        return 'expo_cms/page1.html'
    
    def getName(self): 
        return '普通页面'
    #def get_heads(self): 
        #return [
            #{'name': 'hello', 'label': '汉化','editor': 'linetext',}, 
            #{'name': 'danyuan', 'label': '但愿','editor': 'linetext',}  
        #]
    
    def mergeCtx(self, par, ctx): 
        
        ctx['menu_lianjie'] = []  #json.loads(ctx['menu_lianjie'])
        
        out = dict(par)
        out.update(ctx)
        if not ctx['menu_lianjie'] and par.get('menu_lianjie'):
            out['menu_lianjie'] = par.get('menu_lianjie')
        return out
    
    def get_tabs(self):
        pagecontent = PageContent(crt_user = self.request.user)
        ls = [
            {'name':'baseinfo',
             'label':'基本信息',
             'com':'com_tab_fields',
             'get_data':{
                 'fun':'get_row',
                 'kws':{
                    'director_name':pagecontent.get_director_name(),
                    'relat_field':'pk',              
                 }
             },
             'after_save':{
                 #'fun':'update_or_insert'
                 #'fun':'do_nothing'
                 'fun':'update_par_row_from_db'
             },
             'heads': pagecontent.get_heads(),
             'ops': pagecontent.get_operations()                 
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

class PageContent(BaseTabFields):
    def get_heads(self): 
        return [
            {'name': 'content', 'label': '页面内容','editor': 'richtext',}, 
            #{'name':'menu_lianjie','label':'导航栏链接','editor':'com-field-table-list',
             #'table_heads':[{'name':'url','label':'url','editor':'com-table-pop-fields-local'},
                            #{'name':'label','label':'显示文字'}, 
                            #{'name': 'op', 'label': '', 'editor': 'com-table-change-order',}],
             #'fields_heads':[{'name':'url','label':'url','editor':'linetext'},
                            #{'name':'label','label':'显示文字','editor':'linetext'}]
             #}
        ]    
    
    #def get_heads(self): 
        #return [
            #{'name': 'slogan', 'label': '推广口号','editor': 'blocktext','style': 'width:30em;height:8em',}, 
            #{'name': 'danyuan', 'label': '但愿','editor': 'linetext',},
            #{'name':'pp','label':'测试标签','editor':'com-field-table-list',
             #'table_heads':[{'name':'a','label':'显示一','editor':'com-table-pop-fields-local'},
                            #{'name':'b','label':'显示二'}, 
                            #{'name': 'op', 'label': '', 'editor': 'com-table-change-order',}],
             #'fields_heads':[{'name':'a','label':'显示一','editor':'linetext'},
                            #{'name':'b','label':'显示二','editor':'linetext'}]
             #}
        #]

#class BaseInfo2(BaseTabFields):
    
    #def get_heads(self): 
        #return [
            #{'name': 'bige', 'label': '逼格','editor': 'linetext',}, 
            #{'name': 'danyuan', 'label': '但愿','editor': 'linetext',}  
        #]

    



director.update({
    'simcms.page.page1': Page1,
    'simcms.page.page1.pageconent': PageContent,
})

cms_page.update({
    'expo_cms_page1': Page1,
})