
from django.contrib import admin
from django.urls import path, include
from .views  import homepage, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",homepage),
    path('about',about),
    path('products/', include('products.urls'))
    
]
