import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from users.models     import User
from companies.models import Company
from recruits.models  import Recruit, RecruitUser

class RecruitView(View):
    
    # 채용 공고 등록
    def post(self, request):
        try:
            data = json.loads(request.body)

            position             = data["position"]
            compensation         = data["compensation"]
            content              = data["content"]
            skill                = data["skill"]
            company_id           = data["company_id"]

            Recruit.objects.create(
                position             = position,
                compensation         = compensation,
                content              = content,
                skill                = skill,
                company_id           = company_id
            )

            return JsonResponse({"message" : "SECCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    # 채용 공고 조회 및 검색
    def get(self, request):
        try:
            search = request.GET.get("search", None)
    
            q = Q()
    
            # 포함하는 검색 범위
            if search:
                q |= Q(position__icontains=search)
                q |= Q(compensation__icontains=search)
                q |= Q(skill__icontains=search)
                q |= Q(company__name__contains=search)
                q |= Q(company__nation__contains=search)
                q |= Q(company__location__contains=search)
    
            recruits = Recruit.objects.select_related("company").filter(q)
    
            result = [{
                "recruit_id"   : recruit.id,
                "company_id"   : recruit.company.id,
                "name"         : recruit.company.name,
                "nation"       : recruit.company.nation,
                "location"     : recruit.company.location,
                "position"     : recruit.position,
                "compensation" : str(format((recruit.compensation), ",d"))+"원",
                "skill"        : recruit.skill
            }for recruit in recruits]
    
            return JsonResponse({"result" : result}, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"message" : "RECRUIT_DOES_NOT_EXIST"}, status=400)

class RecruitDetailView(View):

    # 채용 공고 상세페이지
    def get(self, request, recruit_id):
        try:
            recruit = Recruit.objects.select_related("company").get(id=recruit_id)
            others  = Company.objects.get(id=recruit.company.id)
    
            result = {
                "recruit_id"   : recruit.id,
                "company_id"   : recruit.company.id,
                "name"         : recruit.company.name,
                "nation"       : recruit.company.nation,
                "location"     : recruit.company.location,
                "position"     : recruit.position,
                "compensation" : str(format((recruit.compensation), ",d")) + "원",
                "skill"        : recruit.skill,
                "content"      : recruit.content,
                "others_recruit" : [other["id"] for other in others.recruit_set.values() \
                                    if other["id"] != recruit.id] # 회사의 다른 채용 공고
            }
    
            return JsonResponse({"result" : result}, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"message" : "RECRUIT_DOES_NOT_EXIST"}, status=400)

    # 채용 공고 수정
    def patch(self, request, recruit_id):
        try:
            data = json.loads(request.body)

            recruit = Recruit.objects.select_related("company").get(id=recruit_id)
            company_id = data.get("company_id")

            # 인증 절차를 제외한 무분별한 수정을 막기위한 최소한의 인가
            if recruit.company.id != company_id:
                return JsonResponse({"result" : "NEED_TO_AUTHORIZATION"}, status=403)

            position     = data.get("position", recruit.position)
            compensation = data.get("compensation", recruit.compensation)
            content      = data.get("content", recruit.content)
            skill        = data.get("skill", recruit.skill)

            Recruit.objects.filter(id=recruit_id).update(
                position     = position,
                compensation = compensation,
                content      = content,
                skill        = skill
            )
                
            return JsonResponse({"result" : "SECCESS"}, status=201)

        except Recruit.DoesNotExist:
            return JsonResponse({"result" : "RECRUIT_DOES_NOT_EXIST"}, status=400)

    # 채용 공고 삭제
    def delete(self, request, recruit_id):
        try:
            data = json.loads(request.body)

            recruit = Recruit.objects.select_related("company").get(id=recruit_id)
            company_id = data.get("company_id")

            # 인증 절차를 제외한 무분별한 삭제를 막기위한 최소한의 인가
            if recruit.company.id != company_id:
                return JsonResponse({"result" : "NEED_TO_AUTHORIZATION"}, status=403)
    
            recruit.delete()

            return JsonResponse({"return" : "SECCESS"}, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"result" : "RECRUIT_DOES_NOT_EXIST"}, status=400)

class ApplyView(View):

    # 채용 공고 지원
    def post(self, request):
        try:
            data = json.loads(request.body)

            recruit_id = data["recruit_id"]
            user_id    = data["user_id"]

            user = User.objects.get(id=user_id)
            recruit = Recruit.objects.get(id=recruit_id)

            # 이미 지원한 공고가 존재할 경우
            if user.applied_company:
                return JsonResponse({"message" : "APPLIED_COMPANY_DOES_EXIST"}, status=400)

            recruituser, created = RecruitUser.objects.get_or_create(
                user_id    = user_id,
                recruit_id = recruit_id,
            )
            
            if created:
                user.applied_comany = recruit.company.name
                return JsonResponse({"result" : "SECCESS"}, status=201)

        except KeyError:
            return JsonResponse({"result" : "KEY_ERROR"}, status=400)
