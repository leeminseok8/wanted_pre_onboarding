from django.test import TestCase, Client

from recruits.models  import Recruit, RecruitUser
from users.models     import User
from companies.models import Company

class RecruitViewTest(TestCase):
    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국",
            location = "서울"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 500000,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )

    def test_success_recruit_view_post_method(self):
        client = Client()

        result = {
            "id"            : 1,
            "name"          : "원티드",
            "nation"        : "한국",
            "location"      : "서울",
            "position"      : "백엔드",
            "compensation"  : 500000,
            "content"       : "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            "skill"         : "python",
            "company_id"    : 1,
        }

        response = client.post('/recruits', result)
        
        self.assertEqual(response.json(),{"message" : "SECCESS"})
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        Recruit.objects.all().delete()
        Company.objects.all().delete()

    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 500000,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )

    def test_fail_recruit_view_post_method(self):
        client = Client()
        response = client.post('/recruits/')

        result = {
            "id"            : 1,
            "name"          : "원티드",
            "nation"        : "한국",
            "position"      : "백엔드",
            "compensation"  : 500000,
            "content"       : "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            "skill"         : "python",
            "company_id"    : 1,
        }

        self.assertEqual(response.json(),{"message" : "KEY_ERROR"})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        Recruit.objects.all().delete()
        Company.objects.all().delete()

    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국",
            location = "서울"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 500000,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )

    def test_seccess_recruit_view_get_method(self):
        client = Client()
        response = client.get('/recruits/')

        result = [{
            "name"          : "원티드",
            "nation"        : "한국",
            "location"      : "서울",
            "position"      : "백엔드",
            "compensation"  : "500,000원",
            "skill"         : "python",
            "recruit_id"    : 1,
            "company_id"    : 1
        }]

        self.assertEqual(response.json(),{"result" : result})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Recruit.objects.all().delete()
        Company.objects.all().delete()

class RecruitDetailViewTest(TestCase):
    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국",
            location = "서울"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 0,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )
    
    def test_seccess_recruit_detail_view_get_method(self):
        client = Client()
        response = client.get('/recruits/1')

        result = {
            "recruit_id"     : 1,
            "company_id"     : 1,
            "name"           : "원티드",
            "nation"         : "한국",
            "location"       : "서울",
            "position"       : "백엔드",
            "compensation"   : "0원",
            "skill"          : "python",
            "content"        : "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            "others_recruit" : []
        }

        self.assertEqual(response.json(),{"result" : result})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Recruit.objects.all().delete()
        Company.objects.all().delete()

    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국",
            location = "서울"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 0,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )

    def test_seccess_recruit_detail_view_patch_method(self):
        client = Client()

        result = {
            "recruit_id  "   : 1,
            "name        "   : "원티드",
            "nation      "   : "한국",
            "location    "   : "서울",
            "position    "   : "백엔드",
            "compensation"   : "0원",
            "skill       "   : "python",
            "content     "   : "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            "others_recruit" : []
        }

        response = client.patch('/recruits/1', result)

        self.assertEqual(response.json(),{"message" : "SECCESS"})
        self.assertEqual(response.status_code, 201)

    def test_seccess_recruit_detail_view_patch_method(self):
        client = Client()
        response = client.delete('/recruits/1')

        self.assertEqual(response.json(),{"message" : "SECCESS"})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Recruit.objects.all().delete()
        Company.objects.all().delete()

class ApplyViewTest(TestCase):
    def setUp(self):
        Company.objects.create(
            id       = 1,
            name     = "원티드",
            nation   = "한국",
            location = "서울"
        )

        Recruit.objects.create(
            id            = 1,
            position      = "백엔드",
            compensation  = 0,
            content       = "원티드에서 주니어 백엔드 개발자를 채용합니다.",
            skill         = "python",
            company_id    = 1,
        )

        RecruitUser.objects.create(
            recruit_id = 1,
            user_id    = 1
        )

        User.objects.create(
            id   = 1,
            name = "이민석"
        )

    def test_seccess_apply_view_post_method(self):
        client = Client()
        response = client.post("/apply")

        self.assertEqual(response.json(),{"message" : "SECCESS"})
        self.assertEqual(response.status_code, 200)