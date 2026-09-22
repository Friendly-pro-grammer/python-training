from django.db import models

# Create your models here.
class Role(models.Model):
    roleName=models.CharField(max_length=200)
    accessModules = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    
    def __str__(self):
        return self.roleName