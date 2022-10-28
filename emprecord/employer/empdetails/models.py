from django.db import models

class employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=50)
    empage=models.IntegerField()
    empaddress=models.TextField()
# Create your models here.


    def __str__(self):
        return self.empname