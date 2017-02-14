from django.db import models

# Create your models here.
class Posting(models.Model):
    #posting_text = models.CharField(max_length=200)
    #posting_type = models.CharField(max_length = 12)
    # posting_id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date published')
