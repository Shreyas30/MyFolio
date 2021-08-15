from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    field = models.CharField(max_length=50)  # Complaint / Message / Enquiery
    subscription = models.CharField(max_length=50) 
    message = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

