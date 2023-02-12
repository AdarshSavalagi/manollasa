from django.db import models



BA = 'BA'
BBA = 'BBA'
BCOM = 'BCOM'
BLIS = 'BLIS'
BOSSE = 'BOSSE'
BSC = 'BSC'
BSW = 'BSW'
MA = 'MA'
MBA = 'MBA'
MEDICAL = 'MEDICAL'
MLISS = 'MLISS'

Branch = (
    (BA, "BA"),
    (BBA, "BBA"),
    (BLIS, "BLIS"),
    (MA, "MA"),
    (MEDICAL, "MEDICAL"),
    (MBA, "MBA"),
    (BOSSE, "BOSSE"),
    (BCOM, "BCOM"),
    (BSC, "BSC"),
    (BSW, "BSW"),
)

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=100,default='nothing')
    Email = models.CharField(max_length=100,default='nothing')
    Message = models.TextField(default='nothing')
    Subject = models.TextField(default='nothing')
    date = models.DateField()

    def __str__(self):
        return self.Name

class apply(models.Model):
    
    Name = models.CharField(max_length=100,blank=True,default='nothing')
    Email = models.CharField(max_length=100,default='nothing')
    Place = models.CharField(max_length=100,blank=True,default='nothing')
    Phone = models.CharField(max_length=100,blank=True,default='nothing')
    Branch = models.CharField(max_length=10, choices=Branch,blank=True,default='nothing')
    date = models.DateField()

    def __str__(self):
        return self.Name