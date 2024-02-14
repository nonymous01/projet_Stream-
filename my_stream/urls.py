from django.contrib import admin
from django.urls import path
from .views import inscription,connexion,home,add_photo,add_video
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription , name="inscription"),
    path('connexion/', connexion , name="connexion"),
    path('home/', home , name="home"),
    path('photo/', add_photo, name="add_photo"),
     path('video/', add_video, name="add_photo")
    

]
