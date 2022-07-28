from django.urls import path
from .views import HomepageView , Aboutus
urlpatterns = [
   
    path('', HomepageView.as_view() , name='home'),
    path('aboutus/', Aboutus.as_view() , name='aboutus'),
]
