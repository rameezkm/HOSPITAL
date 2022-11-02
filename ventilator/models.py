from django.db import models

class Department(models.Model):
    d_name=models.CharField(max_length=30)
    d_description=models.TextField()
    def __str__(self):
        return self.d_name
class Doc(models.Model):
    d_name=models.CharField(max_length=50)
    d_department=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_spec = models.TextField()
    doc_image = models.ImageField(upload_to='doctors/')
    def __str__(self):
        return self.d_name  

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=100)
    d_name=models.ForeignKey(Doc,on_delete=models.CASCADE)
    booking_date=models.DateField() 
    booked_on=models.DateTimeField(auto_now_add=True)                                  



