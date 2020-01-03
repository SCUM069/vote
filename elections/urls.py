
from django.urls import include, path,re_path
from elections import views


app_name = 'elections'
urlpatterns = [
    path('', views.index, name='home'),
    path('areas/<str:area>/', views.areas, name='areas'),
    path('polls/<int:poll_id>/', views.polls, name='polls'),
    path('areas/<str:area>/results', views.results, name='results'),
    re_path(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates)

]
