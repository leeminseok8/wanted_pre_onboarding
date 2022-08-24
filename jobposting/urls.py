from django.urls import path, include

urlpatterns = [
    path("recruits", include("recruits.urls")),
    path("users", include("users.urls")),
    path("companies", include("companies.urls"))
]