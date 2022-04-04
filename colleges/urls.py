from django.urls import path
from . import views


urlpatterns = [
    path("",views.startingpage,name="Startingpage"),
    path("scores",views.scores,name="scores"),
    path("<value>",views.linkpages, name="linkingpage"),
    path("scholarship/<value>",views.detailcollege, name="Collegedetail")
]