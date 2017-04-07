from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class posting(models.Model):
    post_id = models.IntegerField(primary_key=True)
	#employer_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    post_title = models.CharField(default="make an app", max_length=50)
    description = models.CharField(default="a decent job", max_length=1000)
    #status could be set up as a list of choices
    status = models.IntegerField(default=0)
    finish_date = models.DateTimeField(default=timezone.now)
    post_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('posting:detail', kwargs={'pk': self.post_id})

    def __str__(self):
        return self.post_title
