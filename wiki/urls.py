from django.contrib import admin
from django.urls import path
from . import views

# TEMPLATE URLS

app_name = 'wiki'

urlpatterns = [
  path('', views.IndexView.as_view(), name='wiki'),
    path('admin/', admin.site.urls),
    path('list/', views.WikiPageListView.as_view(), name='list'),
    path('list/<int:pk>', views.WikiPageDetailView.as_view(), name="detail"),
    path('create/', views.WikiPageCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.WikiPageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.WikiPageDeleteView.as_view(), name='delete'),
]