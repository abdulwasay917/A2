from django.contrib import admin
from django.urls import path,include
from banks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('banks/', include('banks.urls')),
    path("", views.all_banks, name="all_banks"),
      #
]