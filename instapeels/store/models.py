from django.db import models
import datetime
import os
    
# Create your models here.
def get_file_path(request,filename):
    orginal_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%m%d%H:%M%S')
    filename = "%s%s" % (nowTime, orginal_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug = models.CharField(("slug"), max_length=50,null=False,blank=False)
    name = models.CharField(("Name"), max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path,null=False,blank=False)
    description = models.TextField(("Description"),max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=trending")
    meta_title = models.CharField(("Meta Title"), max_length=100,null=False,blank=False)
    meta_keyword = models.CharField(("Meta Keyword"), max_length=250,null=False,blank=False)
    meta_description = models.CharField(("Meta Description"), max_length=550,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(("slug"), max_length=50,null=False,blank=False)
    name = models.CharField(("Name"), max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path,null=False,blank=False)
    short_description = models.TextField(("Description"),max_length=200,null=False,blank=False)
    quantity = models.IntegerField(null =False,blank=False)
    description = models.TextField(("Description"),max_length=500,null=False,blank=False)
    orginal_price = models.FloatField(null =False,blank=False)
    selling_price = models.FloatField(null =False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=trending")
    tag = models.CharField(max_length=150, null =False,blank=False)
    meta_title = models.CharField(("Meta Title"), max_length=100,null=False,blank=False)
    meta_keyword = models.CharField(("Meta Keyword"), max_length=250,null=False,blank=False)
    meta_description = models.CharField(("Meta Description"), max_length=550,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name