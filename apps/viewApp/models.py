from django.db import models

class Author(models.Model):
    """ 作者表 """
    name = models.CharField(max_length=32, verbose_name='作者')
    age = models.IntegerField(verbose_name='年龄')

    # 继承模型管理器
    objects = models.Manager()

    def __str__(self):
        return self.name
