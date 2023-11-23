from django.contrib import admin
from django.urls import path

from name.views import NameListView, AddNameView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NameListView.as_view(), name='name_list_view'),
    path('name/', AddNameView.as_view(), name='name'),
]
