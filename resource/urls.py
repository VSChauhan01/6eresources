from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path('data',views.data,name='data'),
]