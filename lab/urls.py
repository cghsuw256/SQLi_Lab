from django.urls import path

from . import views

app_name = "lab"
urlpatterns = [
    # GET과 POST 모두 login_view에서 처리한다.
    path("", views.login_view, name="login"),
    path("data", views.data_view, name="data"),
]
