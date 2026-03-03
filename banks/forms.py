from django import forms
from .models import Bank, Branches

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ["name", "swift_code", "institution_number", "description"]  #

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branches
        fields = ["name", "transit_num", "address", "email"]