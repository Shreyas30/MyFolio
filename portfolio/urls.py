from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('',views.index,name="PortfolioHome" ),
    path('preview/',views.preview,name="Preview" ),
    path('select/',views.select,name="Select" ),
    path('img/',views.imgHandler,name="imgHandler" ),
    path('download/',views.download,name="Download" ),
    

    # path('input/', views.inputData, name="Input"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)