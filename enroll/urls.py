from django.urls import path
from enroll import views

urlpatterns = [
    path('signup/', views.signUp, name = 'signup-page'),
    path('login/', views.login_user, name = 'login-page'),
    path('dashboard/', views.dashboard, name = 'dashboard-page'),
    path('logout/', views.logout_user, name = 'logout-page'),
    path('chage-password/', views.change_password, name = 'change-password-page'),
    path('imgupload/', views.add_img_upload, name = 'img-upload-page'),
    path('update/<int:id>/', views.update_info, name = 'update-page'),
    path('delete/<int:id>/', views.DeleteRedirectView.as_view(), name = 'delete-page'),
    path('details/<int:pk>/', views.DetailProductDetailView.as_view(), name = 'details-page'),
]
