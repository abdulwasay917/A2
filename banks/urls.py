from django.urls import path
from . import views

urlpatterns = [

    path("add/", views.add_bank, name="add_bank"),
    path("<int:bank_id>/details/", views.bank_details, name="bank_details"),
    path("<int:bank_id>/branches/add/", views.add_branch, name="add_branch"),
    path("branch/<int:branch_id>/details/", views.branch_details, name="branch_details"),
    path("branch/<int:branch_id>/edit/", views.edit_branch, name="edit_branch"),
    path("update/<int:pk>/", views.UpdateBankView.as_view(), name="update_bank"),
    path("delete/<int:pk>/", views.BankDeleteView.as_view(), name="delete_bank"),

]