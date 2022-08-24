import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobposting.settings")
django.setup()

from users.models      import User
from companies.models  import Company
from recruits.models   import Recruit, RecruitUser

COMPANY_PATH     = "./resource/companies.csv"
USER_PATH        = "./resource/users.csv"
RECRUIT_PATH     = "./resource/recruits.csv"
RECRUITUSER_PATH = "./resource/recruits_users.csv"

def insert_company():
    with open(COMPANY_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name     = row[0]
            nation   = row[1]
            location = row[2]

            Company.objects.create(
                name     = name,
                nation   = nation,
                location = location
            )

    print("SECCESSED UPLOAD SELLER DATA!")
    
def insert_user():
    with open(USER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name            = row[0]
            applied_company = row[1]
            prefer_position = row[2]

            User.objects.create(
                name            = name,
                applied_company = applied_company,
                prefer_position = prefer_position
            )

    print("SECCESSED UPLOAD USER DATA!")
    
def insert_recruit():
    with open(RECRUIT_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            position     = row[0]
            compensation = row[1]
            content      = row[2]
            skill        = row[3]
            company_id   = row[4]
            company      = Company.objects.get(id=company_id)

            Recruit.objects.create(
                position     = position,
                compensation = compensation,
                content      = content,
                skill        = skill,
                company      = company
            )

    print("SECCESSED UPLOAD PRODUCT DATA!")
    
def insert_recruituser():
    with open(RECRUITUSER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            recruit_id = row[0]
            user_id    = row[1]
            recruit    = Recruit.objects.get(id=recruit_id)
            user       = User.objects.get(id=user_id)

            RecruitUser.objects.create(
                recruit = recruit,
                user    = user
            )

    print("SECCESSED UPLOAD PRODUCTUSER DATA!")


insert_company()
insert_user()
insert_recruit()
insert_recruituser()