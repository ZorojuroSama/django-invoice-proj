from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return HttpResponse("incorrect username and password")
    return render(request, "login.html")


def signupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        user = User.objects.filter(username = uname)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')
        
        user = User.objects.create(
            username = uname,
            email = email,
        )
        user.set_password(pass1)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('login')
    return render(request, 'signup.html')

# Client Model Form


def add_invoice(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ClientFm = ClientForm(request.POST)

            if ClientFm.is_valid():
                comp = ClientFm.cleaned_data["company_name"]
                gst = ClientFm.cleaned_data["gst_number"]
                cntry = ClientFm.cleaned_data["country"]
                sts = ClientFm.cleaned_data["state"]
                add = ClientFm.cleaned_data["address"]

                obj = Client.objects.create(
                    company_name=comp,
                    gst_number=gst,
                    country=cntry,
                    state=sts,
                    address=add,
                )
                obj.save()

                messages.success(
                    request, "Your 'Client' form has been submitted successfully."
                )

                ClientFm = ClientForm()
        else:
            ClientFm = ClientForm()

            return render(request,'addinvoice.html',{'ClientFm':ClientFm})
    else:
       return HttpResponse('/')

def service(request):
    serviceFm = ServiceForm()
    if request.method == 'POST':
        servicefm = ServiceForm(request.POST)
        if servicefm.is_valid():
            servicefm.save()
            return redirect('service')
        client = request.POST.get('client')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')

        user = Services.objects.create(
            client = client,
            description = description,
            quantity = quantity,
            amount = amount,
        )
        user.save()
    return render(request, 'service.html', {'serviceFm': serviceFm})


def addClient(request):
    providerObj = AddClient.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = ClientForm()
    
    context = {'form': form, 'providerObj': providerObj}
    
    return render(request, 'addclient.html', context)


def update_client(request, item_id):
    client = AddClient.objects.get(pk=item_id)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClientForm(instance=client)
    
    context = {'form': form}
    return render(request, 'update_client.html', context)


def delete_client(request, item_id):
    client = AddClient.objects.get(pk=item_id)
    if request.method == 'POST':
        client.delete()
        return redirect('dashboard')
    
    context = {'client': client}
    return render(request, 'delete_client.html', context)