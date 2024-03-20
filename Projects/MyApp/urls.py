from django.urls import path, include
from MyApp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.home, name = "home"),
    path("create/",views.create, name = "create"),
    path("read/",views.read, name = "read"),
    path("update/",views.update, name = "update"),
    path("delete/",views.delete, name = "delete"),
]