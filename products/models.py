from django.db import models
from django.contrib.auth.models import User

# List of Manufacturers.

MAKE_CHOICES = (
    ('', 'Please choose a Make'),
    ('audi','Audi'),
    ('bmw', 'BMW'),
    ('toyota','Toyota'),
    ('nissan','Nissan'),
    ('mini','Mini'),
)

# Generates a unique quote number when the user submits the form. 

def increment_quote_number():
    last_quote = Services.objects.all().order_by('invoice_no').last()
    if not last_quote:
         return 'QUOTE_1001'
    quote_no = last_quote.invoice_no
    quote_int = int(quote_no.split('_')[1])
    new_quote_int = quote_int + 1
    new_quote_no = 'QUOTE_' + str(new_quote_int)
    return new_quote_no

# Table for types of service the company offers.
class TypeOfService(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='quotes', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.name)

# Table for the list of colours to be used.
class WrapColour(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='wrap_colour')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.name)
    
# Table for extra services the company would like to offer.
class OptionalService(models.Model):
    name = models.CharField(max_length=60)
    is_needed = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.name)

# Table for any vehicle damage that needs to be recorded.
class Damage(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return str(self.name)

# Main table that links the others above for submitting a quote to the owner.
class Services(models.Model):
    invoice_no = models.CharField(max_length=500, default=increment_quote_number, null=True , blank=True)
    type_of_service = models.ForeignKey(TypeOfService, on_delete=models.CASCADE, null=True)
    optional_service = models.ManyToManyField(OptionalService)
    wrap_colour = models.ForeignKey(WrapColour, on_delete=models.CASCADE, null=True)
    damage = models.ManyToManyField(Damage)
    damage_details = models.TextField(max_length=500, blank=True)
    car_make = models.CharField(max_length=30, choices=MAKE_CHOICES, default='Please choose a Make', null=False)
    car_model = models.CharField(max_length=30, null=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    user = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.invoice_no)
        
 