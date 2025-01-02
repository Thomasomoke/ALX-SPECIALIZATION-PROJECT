from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from . forms import OrderForm, CreateUserForm, TicketCategoryForm, BookingForm, EventForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def dashBoard(request):
	orders = Order.objects.all().order_by('-status')[0:5]
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = Order.objects.all().count()
	delivered = Order.objects.filter(status='Delivered').count()
	pending = Order.objects.filter(status='Pending').count()



	context = {'customers':customers, 'orders':orders,
	'total_customers':total_customers,'total_orders':total_orders, 
	'delivered':delivered, 'pending':pending}
	return render(request, 'accounts/dashBoard.html', context)

def products(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'accounts/products.html', context)

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	total_orders = orders.count()



	orderFilter = OrderFilter(request.GET, queryset=orders) 
	orders = orderFilter.qs

	context = {'customer':customer, 'orders':orders, 'total_orders':total_orders,
	'filter':orderFilter}
	return render(request, 'accounts/customer.html', context)




def createOrder(request):
	action = 'create'
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/order_form.html', context)



def updateOrder(request, pk):
	action = 'update'
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/customer/' + str(order.customer.id))

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/order_form.html', context)



def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		customer_id = order.customer.id
		customer_url = '/customer/' + str(customer_id)
		order.delete()
		return redirect(customer_url)
		
	return render(request, 'accounts/delete_item.html', {'item':order})

@login_required
def create_event(request):
    if  request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')  # Redirect to the event list
    else:
        form = EventForm()

    return render(request, 'accounts/create_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()  # Fetch all events
    context = {'events': events}
    return render(request, 'accounts/event_list.html', context)

#view to show event details
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk) 
    ticket_categories = event.ticket_categories.all()  
    context = {'event': event, 'ticket_categories': ticket_categories}
    return render(request, 'accounts/event_detail.html', context)


def ticket_category_list(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk) 
    ticket_categories = event.ticket_categories.all()  
    context = {'event': event, 'ticket_categories': ticket_categories}
    return render(request, 'accounts/ticket_category_list.html', context)


@login_required
def create_ticket_category(request):
    event = Event.objects.first()
    if request.method == 'POST':
        form = TicketCategoryForm(request.POST)
        if form.is_valid():
            ticket_category = form.save(commit=False)
            ticket_category.event = event 
            ticket_category.save()
            return redirect('ticket_category_list')
    else:
        form = TicketCategoryForm()
    return render(request, 'accounts/ticket_category_form.html', {'form': form})

# View to create a booking
@login_required
def create_booking(request):
    event = Event.objects.first() 
    ticket_categories = event.ticket_categories.all() 
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_name = request.user.username 
            booking.customer_email = request.user.email
            booking.save()
            messages.success(request, 'Booking Successful!')
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    
    context = {'event': event, 'ticket_categories': ticket_categories, 'form': form}
    return render(request, 'accounts/booking_form.html', context)


def booking_confirmation(request):
    
    booking = Booking.objects.first()

    if not booking:
        messages.error(request, "No booking found.")
        return redirect('create_booking')  

    return render(request, 'accounts/booking_confirmation.html', {
        'Event': booking.event,
        'User name': booking.user_name,

        'Booking date': booking.booking_date,
        'Ticket category': booking.ticket_category,
        'Quantity': booking.quantity,
        'Message': 'Booking Successful!',
    })

# View to list all bookings for a specific event
def booking_list(request, event_pk):
    event = Event.objects.first()
    
    bookings = event.booking_set.all()  
    context = {'event': event, 'bookings': bookings}
    return render(request, 'accounts/booking_list.html', context)


def booking_detail(request, booking_pk):
    booking = get_object_or_404(Booking)  
    context = {'booking': booking}
    return render(request, 'accounts/booking_detail.html', context)


@login_required
def update_booking(request, booking_pk):
    booking = get_object_or_404(Booking, pk=booking_pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', booking_pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    
    context = {'form': form, 'booking': booking}
    return render(request, 'accounts/booking_form.html', context)



@login_required
def delete_booking(request):
   
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            booking = get_object_or_404(Booking, id=booking_id)
            booking.delete()
            return redirect('event_list')  
    else:
        
        return redirect('event_list')  

    return render(request, 'accounts/booking_confirm_delete.html')