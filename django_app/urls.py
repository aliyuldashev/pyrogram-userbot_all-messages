from django.urls import path
from . import views

urlpatterns = [
    path('word/',views.give_view.as_view()),
    path('admins/', views.admin_view.as_view()),
    path('users/<str:tg_id>/<str:xabar>/<str:soz>/<str:f_name>/<str:kanal>/',views.users)

]