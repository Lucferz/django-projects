from django.db import models

# Create your models here.
#los fields aparentemente tienen los siguientes parametros max_length, null, blank
class Estados(models.Model):
    es_id = models.IntegerField(primary_key=True)
    es_desc =models.Charfield(max_length=80,null=False,blank=False)
    def __str__(self) -> str:
        return super().__str__()
        
    