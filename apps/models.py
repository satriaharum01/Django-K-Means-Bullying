from django.db import models

# Create your models here.

class m_data(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    s_fisik = models.IntegerField(max_length=2, blank=True, null=True)
    s_verbal = models.IntegerField(max_length=2, blank=True, null=True)
    s_psikologis = models.IntegerField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'data_history'