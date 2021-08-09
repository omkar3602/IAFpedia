from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='main_page'),
    path('about_us/',views.about_us,name='about_us'),
    path('sources/',views.sources,name='sources'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('contactus/',views.contactus,name='contactus'),
    path('newsfeed/',views.newsfeed,name='newsfeed'),
    path('exams/',views.exams,name='exams'),
    path('exams/army',views.exams_army,name='exams_army'),
    path('exams/navy',views.exams_navy,name='exams_navy'),
    path('exams/airforce',views.exams_airforce,name='exams_airforce'),
    path('exams/army/<str:pk>',views.exam_sub_army,name='exam_sub_army'),
    path('exams/navy/<str:pk>',views.exam_sub_navy,name='exam_sub_navy'),
    path('exams/airforce/<str:pk>',views.exam_sub_airforce,name='exam_sub_airforce'),
    path('hof_army/',views.hof_army,name='hof_army'),
    path('hof_navy/',views.hof_navy,name='hof_navy'),
    path('hof_airforce/',views.hof_airforce,name='hof_airforce'),
    path('historical_events/',views.he,name='he'),
    path('donations/',views.donations,name='donations'),
    path('profile/',views.settings,name='settings'),
    path('profile/edit/',views.settings_edit,name='settings_edit'),
]
