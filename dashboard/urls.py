from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('branches', views.branches, name="branches"),
    path('branches/rm/<int:id>', views.deleteBranch),
    path('api/queue/', views.queue),
]
