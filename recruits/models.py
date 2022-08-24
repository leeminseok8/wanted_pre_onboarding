from django.db import models

from users.models     import User
from companies.models import Company

class Recruit(models.Model):
    '''
    채용 공고 등록을 위한 모델입니다.
    '''
    position     = models.CharField(max_length=30)
    compensation = models.IntegerField()
    content      = models.CharField(max_length=1000)
    skill        = models.CharField(max_length=100)
    company      = models.ForeignKey(Company, on_delete=models.CASCADE)
    user         = models.ManyToManyField(User, through="RecruitUser")

    class Meta:
        db_table = 'recruits'

class RecruitUser(models.Model):
    '''
    채용 공고 지원을 위한 모델입니다.
    '''
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recruits_users'