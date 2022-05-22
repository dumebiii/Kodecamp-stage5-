from django.urls import path
from .views import *

urlpatterns = [

    path('', page1, name='page1' ),
    path('1/', page2, name='page2'),
    path('2/', page3, name='page3' )
]
