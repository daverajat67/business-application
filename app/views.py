from django.shortcuts import render,redirect
from app.models import Business
from app.forms import BusinessForm
# Create your views here.

def bussiness_crud(request, pk = None):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
        businesses = Business.objects.all()

    return render(request, 'businesses/business_form.html', {'form': form,"businesses":businesses })

def update_bussiness(request, pk = None):
    if request.method == 'POST':
        if pk:
            # Edit an existing business
            business = Business.objects.get(id=pk)
            form = BusinessForm(request.POST, instance=business)
            if form.is_valid():
                form.save()
                return redirect('business_list')
    else:
        if pk:
            # Load an existing business for editing
            business = Business.objects.get(id=pk)
            form = BusinessForm(instance=business)
    return render(request, 'businesses/update_business_form.html', {'form': form})

def delete_business(request, pk=None):
    if pk is not None:
        business = Business.objects.get(id=pk)
        business.delete()
        return redirect('business_list')