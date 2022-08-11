from . import views
from django.urls import path


urlpatterns = [
    path('create/',views.Create_company.as_view()),
    path('update/<int:pk>', views.Update_company.as_view()),
    path('delete/<int:pk>', views.Destroy_company.as_view()),
    path('all', views.List_company.as_view()),
    path('retrieve/<int:pk>', views.Retrieve_company.as_view()),

]
