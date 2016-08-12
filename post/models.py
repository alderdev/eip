from django.db import models

# Create your models here.
class Post(models.Model):

    subject = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    invalid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def get_absoulte_url(self):

        return "/posts/detail/%s/" %( str(self.id) )
