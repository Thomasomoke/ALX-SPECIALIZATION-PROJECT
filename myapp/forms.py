from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Event, TicketCategory, Booking

from .models import Customer, Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        exclude = ['user']

# Form for Event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'image', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# Form for Ticket Category
class TicketCategoryForm(forms.ModelForm):
    class Meta:
        model = TicketCategory
        fields = ['name', 'price', 'available_quantity']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., VIP, Business, Regular'}),
            'price': forms.NumberInput(attrs={'min': 0, 'placeholder': 'e.g., 1000'}),
            'available_quantity': forms.NumberInput(attrs={'min': 1, 'placeholder': 'e.g., 50'}),
        }
        
# Form for Booking
class BookingForm(forms.ModelForm):
    ticket_category = forms.ModelChoiceField(queryset=TicketCategory.objects.all(), empty_label="Select Ticket Category")
    
    class Meta:
        model = Booking
        fields = ['event', 'user_name', 'ticket_category', 'quantity']
        widgets = {
            'ticket_category': forms.Select(),
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }

    def clean_quantity(self):
        """
        Ensure that the quantity being booked does not exceed the available quantity.
        """
        quantity = self.cleaned_data.get('quantity')
        ticket_category = self.cleaned_data.get('ticket_category')

        if ticket_category and quantity > ticket_category.available_quantity:
            raise forms.ValidationError(
                f"Only {ticket_category.available_quantity} tickets are available for this category."
            )
        return quantity
