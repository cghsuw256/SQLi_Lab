from django.urls import include, path

# lab/urls.py로 연결
urlpatterns = [path("", include("lab.urls"))]
