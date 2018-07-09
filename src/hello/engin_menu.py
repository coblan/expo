# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine,page,fa,can_list,can_touch
from django.contrib.auth.models import User,Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
from django.utils.translation import ugettext as _
from django.conf import settings

#from .js_translation import get_tr
#from maindb.models import TbBanner, TbAppversion, TbNotice, TbCurrency, TbQa, TbActivity, TbAppresource, TbAccount, TbLoginlog, \
     #TbBalancelog, TbChargeflow, TbChannel, TbTicketmaster, TbMatches, TbRcFilter, TbRcLevel, TbRcUser, TbBlackuserlist, TbBlackuserlistLog, \
     #Blackiprangelist, Whiteiplist, Whiteuserlist, TbWithdrawlimitlog, TbTeams,
#from maindb.models import * 
#from . import permit

class PcMenu(BaseEngine):
    url_name='admin'
    #brand = 'SportsCenter'
    #mini_brand='SC'
    brand = '管理后台'
    mini_brand='管理' 
    

    @property
    def menu(self):
        crt_user = self.request.user
        menu=[
            {'label':_('DashBoard'),'url':page('home'),'icon':fa('fa-home'), 'visible':True}, 

            #{'label':_('Marketing'),'icon':fa('fa-image'), 'visible': True,
             #'submenu':[
                #{'label':_('Banner'),'url':page('TbBanner'), 'visible': can_touch(TbBanner, crt_user) },
                #{'label':_('App Package'),'url':page('maindb.TbAppversion'), 'visible': can_touch(TbAppversion, crt_user),},
                #{'label':_('Notice'),'url':page('maindb.TbNotice'), 'visible': can_touch(TbNotice, crt_user),},
                #{'label':_('Currency'),'url':page('maindb.TbCurrency'), 'visible': can_touch(TbCurrency, crt_user)},
                #{'label':_('Help'),'url':page('maindb.TbQa'), 'visible': can_touch(TbQa, crt_user),},
                #{'label':_('Activity'),'url':page('maindb.TBActive'), 'visible': can_touch(TbActivity, crt_user),},
                #{'label':_('AppResource'),'url':page('AppResource'), 'visible': can_touch(TbAppresource, crt_user),},

                #]},  
            {'label':_('User'),'icon':fa('fa-user'),'visible':True,
                 'submenu':[
                     {'label':_('User'),'url':page('jb_user'),'visible':can_touch(User, crt_user)},
                     {'label':_('权限组'),'url':page('jb_group'),'visible':can_touch(Group, crt_user)},
                     #{'label':'权限分组','url':page('group_human'),'visible':can_touch(Group)},
                   ]},   
            ]
        return menu

PcMenu.add_pages(page_dc)