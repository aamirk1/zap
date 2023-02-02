from django.db import models
from django.contrib.auth.models import User
import datetime
import os
    
# Create your models here.
def get_file_path(request,filename):
    orginal_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%m%d%H:%M%S')
    filename = "%s%s" % (nowTime, orginal_filename)
    return os.path.join('uploads/',filename)
def get_file_path_for_multi(request,filename):
    orginal_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%m%d%H:%M%S')
    filename = "%s%s" % (nowTime, orginal_filename)
    return os.path.join('uploads/multiimg/',filename)

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
    short_description = models.TextField(("Short Description"),max_length=200,null=False,blank=False)
    quantity = models.IntegerField(null =False,blank=False)
    description = models.TextField(("Description"),max_length=600,null=False,blank=False)
    howtouse = models.TextField(("How to Use"),default="Not Availabel",max_length=600,null=False,blank=False)
    benefits = models.TextField(("benefits"),default="Not Availabel",max_length=600,null=False,blank=False)
    whyuseinstapeel = models.TextField(("Why Use Instapeel"),default="Not Availabel",max_length=600,null=False,blank=False)
    ingridient = models.TextField(("Ingridient"),default="Not Availabel",max_length=500,null=False,blank=False)


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

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path_for_multi,verbose_name='Image')
    def __str__(self):
        return self.product.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    lname = models.CharField(max_length=150,null=False)
    email = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=50,null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150,null=False)
    state = models.CharField(max_length=150,null=False)
    country = models.CharField(max_length=150,null=False)
    pincode = models.CharField(max_length=150,null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatuses = (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150,choices=orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)


