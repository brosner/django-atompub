from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from django.db import models


class Collection(models.Model):
    
    title = models.CharField(maxlength=100)
    
    def get_absolute_url(self):
        return "/collection/%s/" % self.id
    
    def href(self):
        return "http://%s%s" % (Site.objects.get_current().domain, self.get_absolute_url())
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass


class Workspace(models.Model):
    
    title = models.CharField(maxlength=100)
    collections = models.ManyToManyField(Collection, blank=True)
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass


class Accept(models.Model):
    
    collection = models.ForeignKey(Collection)
    text = models.CharField(maxlength=100)
    
    class Admin:
        list_display = ("collection", "text")


# @@@ category documents not yet supported
# @@@ fixed categories not yet supported
# @@@ inherited category scheme not yet supported

class Category(models.Model):
    
    collection = models.ForeignKey(Collection)
    term = models.CharField(maxlength=100)
    scheme = models.URLField(null=True, verify_exists=False, blank=True)
    label = models.CharField(maxlength=100, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "categories"

    class Admin:
        list_display = ("collection", "term", "scheme", "label")


class MemberEntry(models.Model):
    
    collection = models.ForeignKey(Collection)
    
    title = models.CharField(maxlength=100)
    creator = models.ForeignKey(User)
    edited = models.DateTimeField()
    
    def get_absolute_url(self):
        return "/entry/%s/" % self.id
    
    def href(self):
        return "http://%s%s" % (Site.objects.get_current().domain, self.get_absolute_url())
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "member entries"
    
    class Admin:
        pass