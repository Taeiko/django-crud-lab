from django.db import models

# Create your models here.

class Console(models.Model):
    name = models.CharField(max_length=80, unique=False)
    release_year = models.IntegerField()
    is_worth_playing= models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table= 'game-consoles'
        
    def __str__(self):
            return f'name:{self.name}, is it worth playing? : {self.is_worth_playing}'