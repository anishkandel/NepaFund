from django.urls import path
from crowdapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import ChangePassword, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='accounts/changepassword.html', form_class=ChangePassword, success_url='/changepasswordsuccess/'), name='changepassword'),
    path('changepasswordsuccess/',auth_views.PasswordChangeView.as_view(template_name='accounts/changepasswordsuccess.html'),name='changepasswordsuccess'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_success.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]