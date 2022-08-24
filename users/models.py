from django.db import models

class User(models.Model):
    '''
    지원자 정보를 위한 모델입니다.
    '''
    name            = models.CharField(max_length=20)
    applied_company = models.CharField(max_length=20, blank=True)
    prefer_position = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'users'