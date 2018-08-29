from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
# Create your models here.

ZHANXUN_STATUS=(
    (0,'离线'),
    (1,'在线'),
)

class ZhanXunModel(models.Model):
    title = models.CharField('标题',max_length=500)
    cover = PictureField('封面',max_length=400,blank=True)
    content = models.TextField('内容',blank=True)
    status=models.IntegerField('状态',choices=ZHANXUN_STATUS,default=0)
    update_time =models.DateTimeField('更新时间',auto_now=True)

