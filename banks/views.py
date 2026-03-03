from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView
from .models import Bank, Branches
from .forms import BankForm, BranchForm
from django.urls import reverse_lazy


@login_required
def add_bank(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.save()
            return redirect(f"/banks/{bank.id}/details/")
    else:
        form = BankForm()
    return render(request, "banks/add_bank.html", {"form": form})



def add_branch(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)

    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized: Please log in", status=401)

    if bank.owner != request.user:
        return HttpResponse("Forbidden: You are not the owner of this bank", status=403)

    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank

            branch.save()
            return redirect(f"/banks/branch/{branch.id}/details/")
    else:
        form = BranchForm()

    return render(request, "banks/add_branch.html", {"form": form, "bank": bank})


def edit_branch(request, branch_id):
    branch = get_object_or_404(Branches, id=branch_id)
    bank = branch.bank

    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    if bank.owner != request.user:
        return HttpResponse("Forbidden: You are not the owner of this bank", status=403)

    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect(f"/banks/branch/{branch.id}/details/")
    else:
        form = BranchForm(instance=branch)

    return render(request, "banks/edit_branch.html", {"form": form, "branch": branch})
def all_banks(request):
    banks = Bank.objects.all()
    return render(request, "banks/all_banks.html", {"banks": banks })


def bank_details(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()
    return render(request, "banks/bank_details.html", {"bank": bank, "branches": branches})




def branch_details(request, branch_id):

    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    branch = get_object_or_404(Branches, id=branch_id)

    if branch.bank.owner != request.user:
        return HttpResponse("you are not owner", status=403)
    data = {
        "id": branch.id,
        "name": branch.name,
        "transit_num": branch.transit_num,
        "address": branch.address,
        "email": branch.email,
        "last_modified": branch.last_updated,
    }
    return render(request,"banks/branch_details.html",{"data":data})

class UpdateBankView(UpdateView):
    model = Bank
    fields = ["name", "swift_code", "institution_number", "description"]
    template_name = "banks/Update_Bank.html"
    success_url = reverse_lazy("all_banks")

class BankDeleteView(DeleteView):
    model = Bank
    template_name = 'banks/delete_bank.html'
    success_url = reverse_lazy("all_banks")