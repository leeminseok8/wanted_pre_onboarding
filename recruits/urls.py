from django.urls import path

from recruits.views import RecruitView, RecruitDetailView, ApplyView

urlpatterns = [
    path("/", RecruitView.as_view()),
    path("/<int:recruit_id>", RecruitDetailView.as_view()),
    path("/apply", ApplyView.as_view())
]