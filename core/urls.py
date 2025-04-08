from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', home_view),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('talabalar/<int:pk>/update/', talaba_update_view),
    path('bitiruvchilar/', bitiruvchilar_view),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('muallif-qoshish/', muallif_post_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:pk>/', kitob_view),
    path('kitoblar/<int:pk>/update/', kitob_update_view),
]
