from django.db import models


class HeaderTop(models.Model):
    text = models.TextField()
    icon = models.CharField(max_length=5)
    adress = models.CharField(max_length=250)
    
    def __str__(self):
        return self.text
    
class HeaderCenter(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class HeaderEnd(models.Model):
    text_top = models.CharField(max_length=30)
    text_big = models.CharField(max_length=50)
    text_end = models.TextField()
    but_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text_big
    
    
    
    
class MainOneTop(models.Model):
    name = models.CharField(max_length=69)
    
    def __str__(self):
        return self.name
    
class MainOneLeft(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
    but_name = models.CharField(max_length=40)
    but_adress = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class MainOneRight(models.Model):
    pay = models.IntegerField()
    img = models.CharField(max_length=10)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.name