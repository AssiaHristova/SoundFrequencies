from django.urls import path

from sound_frequencies.profiles.views import SignUpView, LogInView, log_out, ProfileDetailsView, ProfileUploadsView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile details'),
    path('uploads/', ProfileUploadsView.as_view(), name='profile uploads'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('log-in/', LogInView.as_view(), name='log in'),
    path('log-out/', log_out, name='log out'),

]
