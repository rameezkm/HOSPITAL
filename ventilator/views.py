from django.shortcuts import redirect, render
from django.http import HttpResponse
from . forms import BookingForm
from . models import Department, Doc

def index(request):
    return render(request, 'index.html')
def department(request):
    conn=Department.objects.all()
    return render(request, 'department.html',{'conn':conn})
def doctors(request):
    world=Doc.objects.all()
    return render(request,'doctor.html',{'world':world})
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    form = BookingForm()
    booking = {
        'form': form
    }
    return render(request, 'booking.html',booking)
        
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')




