from django.db import models

# Create your models here.

    

class Contact(models.Model):
    date =models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.IntegerField()
    desc = models.TextField()
 
    def __str__(self) :
        return self.name



PROJECT_CHOICES= [
            ('drone', 'Drone_detection'),
            ('pothole', 'Pothole_counter'),
            ('facemask', 'Facemask_detection'),
            ('tooth', 'tooth_detection'),
        ]


class Info(models.Model):

    
    name = models.CharField(max_length=122, blank=True)
    email = models.EmailField(max_length=122, blank=True)
    phone = models.IntegerField( blank=True)
    proj = models.CharField(choices=PROJECT_CHOICES, max_length=100, blank=True)

    def __str__(self) :
        return self.name
    
# class Drone(models.Model):
#     name = models.CharField(max_length=50)
#     drone_img = models.ImageField(upload_to='images/')

#     def __str__(self) :
#         return self.name




GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female')
    ]

class Signup(models.Model):
    # name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=False)
    username = models.CharField(max_length=100) 
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)

    def __str__(self) :
        return self.username