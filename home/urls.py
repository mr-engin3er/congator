from django.urls import path
from .views import (
    index,
    new_search,
)
app_name = 'home'

urlpatterns = [
    path('', index, name=''),
    path('new_search', new_search, name='new_search')

]
