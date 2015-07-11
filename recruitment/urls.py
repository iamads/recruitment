from django.conf.urls import patterns, include, url
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'candidate', views.CandidateView)
router.register(r'recruiter', views.RecruiterView)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
