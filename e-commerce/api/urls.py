from django.urls import path,include

urlpatterns=[
    
    path("api/v1/",include('products.urls')),
    path("api/v1/auth/",include('users.urls'))
]