from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date_added=models.DateField(auto_now_add=True)
    

    

   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})

# Create your models here.

    class Meal(models.Model):
        name = models.CharField(max_length=100, blank=False, null=False)
        date_added = models.DateField(auto_now_add=True)
        description = models.CharField(max_length=75, blank=False, null=False)
        review = models.CharField(max_length=100, blank=True, null=True)
        image_url = models.TextField(null= True, blank=True)

class Mealprice(models.Model):
    item= models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.item) +":$" + str(self.price)
    

    