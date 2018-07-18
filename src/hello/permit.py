from helpers.director.base_data import site_cfg
from django.utils.translation import ugettext as _

def get_permit(): 
    permit = [
        { 'label': _('活动'),
         'children': [
             { 'label': _('创建活动'), 'value': 'TbBanner',}, 
             { 'label': _('删除活动'), 'value': 'TbNotice',}, 
             { 'label': _('添加嘉宾'), 'value': 'TbAppversion',}, 
             ]
         }, 
        { 'label': _('嘉宾'),
         'children': [
             {'label': _('创建嘉宾'), 'value': 'TbAccount',}, 
             {'label': _('创建其他'), 'value': 'TbLoginlog',}, 
             ],
         }, 
        {'label': _('MoneyFlow'),
         'children': [
             {'label': '金流渠道', 'value': 'TbChannel',}, 
             {'label': '金流日志', 'value': 'TbChargeflow',}
             ],
        }, 
        {'label': _('Tb Match'), 
         'children': [
             {'label': _('Tb Match'), 'value': 'TbMatches',}, 
             {'label': _('Tb TicketMaster'), 'value': 'TbTicketmaster.all',},              
             ],
        }, 
       
        {'label': _('RiskControl'),
         'children': [
            {'label': _('Tb RC Filter'), 'value': 'TbRcFilter',}, 
            {'label': _('Tb RC Level'), 'value': 'TbRcLevel',}, 
            {'label': _('Tb RC User'), 'value': 'TbRcUser',}, 
            {'label': _('Tb Withdraw Limit Log'), 'value': 'TbWithdrawlimitlog',}, 
                 
                 
             {'label': _('Tb Blankuserlist'), 'value': 'TbBlackuserlist',}, 
             {'label': _('Tb BlackuserlistLog'), 'value': 'TbBlackuserlistLog',}, 
             {'label': _('Blackiplist'), 'value': 'Blackiplist',}, 
             {'label': _('Black IP Range'), 'value': 'Blackiprangelist',}, 
             {'label': _('White IP'), 'value': 'Whiteiplist',}, 
             {'label': _('White User'), 'value': 'Whiteuserlist',}
             ],}, 
        {'label': _('User'),
         'children': [
            #{'label': _('查看用户'), 'value': 'User.read',}, 
             {'label': _('User'), 'value': 'User.write',}, 
             {'label': _('Role'), 'value': 'Group',}
             ],
         }
        
        
    ]
    return permit

site_cfg['permit.options'] = get_permit
#permit_dc['__root__'] = permit