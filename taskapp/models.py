from django.db import models

class taskmodel(models.Model):
    lecture=models.CharField(max_length=25)
    number=models.IntegerField(default=0)
    limit=models.DateTimeField()
    repeat = models.BooleanField(default=False)
    repeat_interval = models.CharField(max_length=10,choices=[
        ('daily', '毎日'),   
        ('weekly', '毎週')], 
        blank=True, null=True )
    


    
    
    
