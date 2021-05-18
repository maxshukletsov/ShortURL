from django.urls import path
from . import views

urlpatterns = [
    path('url/', views.ShortUrlView.as_view()),
    path('<str:short_url>', views.RedirectView),

]
