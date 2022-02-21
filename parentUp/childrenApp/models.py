from django.db import models

# Create your models here.
class Children(models.Model):
    child_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(null=False, max_length=4, choices=(('Boy', 'Boy'), ('Girl', 'Girl')), default='Boy')
    birth_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=32)