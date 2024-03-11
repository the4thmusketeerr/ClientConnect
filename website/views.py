from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Clients

# Create your views here.


def home(request):
    clients = Clients.objects.all()
    #Check to see if logging in
    if request.method == 'POST':
        action = request.POST['action']
        print(action)
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("Error logging in - Please try again..."))
            return redirect('home')
    else:
        return render(request, 'home.html', {'clients':clients}) #rendering the login.html template


def client_record(request,pk):
    if request.user.is_authenticated:
        #Look up Records
        client_record = Clients.objects.get(id=pk) #get the client record that corresponds the primary key(pk) which is the id
        return render(request, 'client.html', {'client_record':client_record})
    else:
        messages.success(request, ("You must be logged in to view client records"))
        return redirect('home')

def delete_client(request,pk):
    if request.user.is_authenticated:
        delete_client = Clients.objects.get(id=pk)
        delete_client.delete()
        messages.success(request, ("Client has been deleted"))
        return redirect('home')
    else:
        messages.success(request, ("You must be logged in to delete client records"))
        return redirect('home')

def add_client(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_client = form.save()
				messages.success(request, "Client has been added successfully")
				return redirect('home')
		return render(request, 'add_client.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_client(request,pk):
     if request.user.is_authenticated:
         current_client = Clients.objects.get(id=pk)
         form = AddRecordForm(request.POST or None, instance=current_client)
         if request.method == "POST":
             if form.is_valid():
                 form.save()
                 messages.success(request, "Client details have been updated")
                 return redirect('home')
         return render(request, 'update_client.html', {'form':form})


def search_client(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            search_query = request.POST.get('search', '')
            clients = Clients.objects.filter(first_name__icontains=search_query) | Clients.objects.filter(last_name__icontains=search_query)
            return render(request, 'search_client.html', {'search_query': search_query, 'clients': clients})
        else:
            
            # Handle GET requests, e.g., redirect to home page
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to search client records.")
        return redirect('home')
     


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')