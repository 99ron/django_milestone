from django.db import models

# Generates a unique quote number. 
def increment_quote_number():
    last_quote = Services.objects.all().order_by('id').last()
    if not last_quote:
         return 'QUOTE0001'
    quote_no = last_quote.quote_no
    quote_int = int(quote_no.split('QUOTE')[-1])
    new_quote_int = quote_int + 1
    new_quote_no = 'QUOTE' + str(new_quote_int)
    return new_quote_no

# Main table used for displaying on the Quotes page.
class Services(models.Model):
    invoice_no = models.CharField(max_length=500, default=increment_quote_number, null=True, blank=True)
    type_of_service = models.ManyToManyField('TypeOfService')
    optional_service = models.ManyToManyField('OptionalService')
    damage = models.ManyToManyField('Damage')
    car_make = models.CharField(max_length=30, null=False)
    car_model = models.CharField(max_length=30, null=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.IntegerField()
    
    def __str__(self):
        return self.name
        
class TypeOfService(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='quotes', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

class OptionalService(models.Model):
    name = models.CharField(max_length=60)
    is_needed = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

class Damage(models.Model):
    name = models.CharField(max_length=120)
    is_damaged = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    