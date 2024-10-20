
from django.urls import path
from . import views
from .views import HomeView
from django.views.generic import RedirectView
from .views import register

urlpatterns = [
    path('', RedirectView.as_view(url='/churches/', permanent=False), name='home'),
     path('', HomeView.as_view(), name='home'),
      path('churches/', RedirectView.as_view(url='/register/', permanent=False), name='home'),
    # Church URLs
    path('churches/', views.ChurchListView.as_view(), name='church_list'),
    path('churches/<int:pk>/', views.ChurchDetailView.as_view(), name='church_detail'),
    
    
    
    path('church/delete/<int:pk>/', views.delete_church, name='delete_church'),
    path('churches/<int:pk>/edit/', views.EditChurchView.as_view(), name='edit_church'),
    path('church/create/', views.ChurchCreateView.as_view(), name='create_church'),
    path('register/', register, name='register'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),  # Ensure this is present
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Contribution URLs
    path('churches/<int:church_id>/contributions/', views.ContributionListView.as_view(), name='contribution_list'),
    path('churches/<int:church_id>/contributions/create/',views. ContributionCreateView.as_view(), name='contribution_create'),
    path('contributions/<int:pk>/update/', views.ContributionUpdateView.as_view(), name='contribution_update'),
    path('contributions/<int:pk>/delete/', views.ContributionDeleteView.as_view(), name='contribution_delete'),

    # Request URLs
    path('churches/<int:church_id>/requests/', views.RequestListView.as_view(), name='request_list'),
    path('churches/<int:church_id>/requests/create/', views.RequestCreateView.as_view(), name='request_create'),
    path('requests/<int:pk>/update/', views.RequestUpdateView.as_view(), name='request_update'),
    path('requests/<int:pk>/delete/', views.RequestDeleteView.as_view(), name='request_delete'),

    # Donation URLs
    path('requests/<int:request_id>/donations/', views.DonationListView.as_view(), name='donation_list'),
    path('requests/<int:request_id>/donations/create/', views.DonationCreateView.as_view(), name='donation_create'),
    path('donations/<int:pk>/update/', views.DonationUpdateView.as_view(), name='donation_update'),
    path('donations/<int:pk>/delete/', views.DonationDeleteView.as_view(), name='donation_delete'),
    
    
    
    
    ]
    

    