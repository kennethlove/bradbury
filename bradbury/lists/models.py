from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class List(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name="lists")
    name = models.CharField(blank=True, default="My List", max_length=255)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ("user", "name")

    def __unicode__(self):
        return self.name

    def save(self):
        if self.__class__.objects.filter(name=self.name):
            self.name = u"%s_" % self.name

        self.slug = slugify(self.name)
        return super(List, self).save()
