from django.urls import path
from candidate import views
urlpatterns = [
    path('candidate-dashboard/',views.candidate_dashboard, name='candidate_dashboard'),
    path('myjobs/',views.myJobListViews, name='myjoblistviews'),
    path('applyforjob/<int:pk>/',views.applyforjob, name='applyforjob'),
]