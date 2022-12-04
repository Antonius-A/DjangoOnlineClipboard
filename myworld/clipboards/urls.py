from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('view/<str:ui>', views.view, name='view'),
  path('search/', views.search, name='search'),
  path('add/', views.add, name='add'),
  path('add/addclipboard/', views.addclipboard, name='addclipboard'),
  path('delete/<str:ui>', views.delete, name='delete'),
  path('update/<str:ui>', views.update, name='update'),
  path('update/updateclipboard/<str:ui>', views.updateclipboard, name='updateclipboard'),
  path('passcode-error', views.passcode_error, name='passcode-error'),
]