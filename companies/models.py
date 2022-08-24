from django.db import models

class Company(models.Model):
    '''
    회사 정보를 위한 모델입니다.
    '''
    name     = models.CharField(max_length=20)
    nation   = models.CharField(max_length=10)
    location = models.CharField(max_length=50)

    class Meta:
        db_table = 'companies'