from django.db import models
class User(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)

    class Product(models.Model):
        pid=models.IntegerField(primary_key=True)
        pname=models.CharField(max_length=20)
        pcost=models.DecimalField(max_digits=10,decimal_places=4)
        pmfdt=models.DateField()
        pexpdt=models.DateField()