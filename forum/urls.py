from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('',views.index,name="ForumHome" ),
    path('post/',views.post,name="Post" ),
    path('profile/',views.profile,name="Profile" ),
    path('payment/',views.payment,name="Payment" ),
    path('subscribe/',views.subscribe,name="Subscribe" ),
    path('createpost/',views.createPost,name="CreatePost"),
    path('editprofile/',views.editProfile,name="EditProfile"),
    path('follow/',views.follow,name="Follow"),
    path('unfollow/',views.unfollow,name="Unfollow"),
    path('search/',views.search,name="Search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)