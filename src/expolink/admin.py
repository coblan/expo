from django.contrib import admin
from . import js_cfg
from helpers.director.shortcut import TablePage,ModelTable,page_dc,director,ModelFields
from .models import ZhanXunModel
# Register your models here.

class ZhanXunPage(TablePage):
    template='jb_admin/table.html'
    def get_label(self):
        return '展讯页面'
    
    class tableCls(ModelTable):
        model = ZhanXunModel
        #hide_fields=['content']
        exclude =['content']
        
        def dict_head(self, head):
            if head['name'] == 'title':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name']='zhanxun_form'
                
            return head
        
    
    def get_context(self):
        ctx =super().get_context()
        form_obj = ZhanXunForm(crt_user=self.crt_user)
        ls = [
          {'name':'zhanxun_form',
           'label':'展讯编辑',
           'com':'com_tab_fields',
           'get_data':{
               'fun':'get_row',
               'kws':{
                  'director_name':form_obj.get_director_name(),
                  'relat_field':'pk',              
               }
           },
           'after_save':{
               'fun':'update_or_insert'
               #'fun':'do_nothing'
               #'fun':'update_par_row_from_db'
           },
           'heads': form_obj.get_heads(),
           'ops': form_obj.get_operations()                 
           }, 
        ]
        ctx['tabs'] =ls
        return ctx
    

class ZhanXunForm(ModelFields):
    class Meta:
        model = ZhanXunModel
        exclude = []
    def dict_head(self, head):
        if head['name']=='content':
            head['editor'] ='richtext'
        return head

director.update({
    'expolink.zhanxun':ZhanXunPage.tableCls,
    'expolink.zhanxun.edit':ZhanXunForm
})

page_dc.update({
    'expolink.zhanxun':ZhanXunPage
})