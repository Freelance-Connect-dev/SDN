from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class posting(models.Model):
    post_id = models.AutoField(primary_key=True)
	#employer_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    post_title = models.CharField(default="", max_length=50)
    company_name = models.CharField(default="", max_length=30)
    description = models.CharField(default="", max_length=1000)
    total_pay = models.FloatField(default=100)
    #status could be set up as a list of choices
    status = models.IntegerField(default=0)
    finish_date = models.DateTimeField(default=timezone.now)
    post_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField('home.Tag')

    def get_absolute_url(self):
        return reverse('posting:detail', kwargs={'pk': self.post_id})

    def __str__(self):
        return self.post_title

class Post_Tag(models.Model):
	job_id = models.ForeignKey(posting,on_delete=models.CASCADE)
	skill_id = models.ForeignKey('home.Tag',on_delete=models.CASCADE)
