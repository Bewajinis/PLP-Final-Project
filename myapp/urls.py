from re import template
from django.urls import path
from django.contrib.auth import views as  auth_view
from myapp.forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from myapp import views
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile',),
    path('address/', views.address, name='address',),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),


    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.show_cart, name='checkout'),



    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),



    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='myapp/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view (template_name='myapp/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='myapp/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='myapp/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name ='myapp/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name ='myapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 