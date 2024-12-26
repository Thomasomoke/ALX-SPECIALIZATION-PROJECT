from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def orders(self):
		order_count = self.order_set.all().count()
		return str(order_count)
	


class Product(models.Model):

	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True) 
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.product)

class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('past', 'Past'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    
    def __str__(self):
        return self.name

class TicketCategory(models.Model):
    event = models.ForeignKey(Event, related_name='ticket_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # e.g., General, VIP
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.name}"
    
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=255)
    booking_date = models.DateTimeField(auto_now_add=True)
    ticket_category = models.CharField(max_length=100)  # Add this field
    quantity = models.PositiveIntegerField()  # Add this field


    def __str__(self):
        return f"{self.user_name} - {self.ticket_category.name}"