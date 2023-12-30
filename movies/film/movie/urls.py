"""
URL configuration for film project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings
app_name='movie'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('add/',views.add,name="add"),
    path('add1/',views.add1,name="add1"),
    path('view1/<int:p>',views.viewbyid,name="viewbyid"),
    path('deletebyid/<int:p>',views.delete,name="deletebyid"),
    path('editbyid/<int:p>',views.update,name="editbyid"),
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
