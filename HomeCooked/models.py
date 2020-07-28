from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date_added=models.DateField(auto_now_add=True)
    

    

   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})

# Create your models here.



