from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField
from suppliers.models import SupplierAccount
from django.core.files.storage import FileSystemStorage
from django.db.models import FloatField

from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
CURRENCY_CHOICES = (
    ('1', 'RON'),
    ('2', 'EUR'),
)

class ActivityQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ActivityManager(models.Manager):
    def get_queryset(self):
        return ActivityQuerySet(self.model, using=self._db)

    def all(self,*args,**kwargs):
        return self.get_queryset().active()



class Type(models.Model):
    # activities = models.ForeignKey(Activity,on_delete=models.CASCADE,)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        verbose_name = "activity_type"
        verbose_name_plural = "activities_type"

def create_type_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Type.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def type_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        verbose_name = "category"
        verbose_name_plural = "categories"

def create_category_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def category_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


class ActivityAgeInterval(models.Model):
    title = models.CharField(max_length=250,help_text="Interval Name")


    def __str__(self):
        return self.title

    class Meta:
        app_label = "core"
        verbose_name = "Activity Age Interval"
        verbose_name_plural = "Activity Age Intervals"

def create_age_interval_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = ActivityAgeInterval.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def Age_interval_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

class ActivityLocation(models.Model):
    name = models.CharField(max_length=250)
    tagline = models.TextField(max_length=100,null=True,blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "core"
        verbose_name = "Activity Location"
        verbose_name_plural = "Activity Locations"


def media_location(instance, filename):
    return "%s/%s" % (instance.slug,filename)

class Activity(models.Model):
    supplier = models.ForeignKey(SupplierAccount,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, null=False,on_delete=models.CASCADE)
    # supplier = models.ForeignKey(Supplier, default=None,on_delete=models.CASCADE)
    age_interval = models.ManyToManyField(ActivityAgeInterval, default=None)
    media = models.ImageField(upload_to=media_location,
                            null=True,blank=True,
                            height_field = "height_field",
                            width_field = "width_field",
                            storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = HTMLField(max_length=2500)
    short_description = HTMLField(max_length=500,null=True,blank=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    sale_price = models.DecimalField(max_digits=20,decimal_places=2,null=True, blank=False)
    slug = models.SlugField(allow_unicode=True, unique=True)
    order = models.IntegerField(default=0,help_text="Activity priority (bigger is better)")
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)
    active = models.BooleanField(default=True)
    tagline = models.CharField(max_length=100,null=True,blank=True, default=None)
    location_tags = models.ManyToManyField(ActivityLocation,default=None)
    address = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=44.4268)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=-26.1025)
    price_currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,default=1)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)



    objects = ActivityManager()

    def __str__(self):
        return self.title

    # def get_absolute_url(self,*args,**kwargs):
    #     view_name = "core:detail_slug"
    #     return "%s/" % (self.slug)
    #     # return reverse(view_name,kwargs={"pk:self.id"})

    def get_absolute_url(self):
        view_name = "core:detail_slug"
        return reverse(view_name, kwargs={"slug": self.slug})


    # def get_redirect_url(self):
    #     view_name = "core:detail_slug"
    #     return reverse(view_name, kwargs={"slug": self.slug})

    def get_edit_url(self,*args,**kwargs):
        view_name = "suppliers:activity_edit"
        return reverse(view_name,kwargs={"pk":self.id})

    class Meta:
        ordering = ['-order']
        app_label = "core"
        verbose_name = "activity"
        verbose_name_plural = "activities"

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Activity.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def activity_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(activity_pre_save_reciever, sender=Activity)

class Seller(models.Model):
    supplier = models.ForeignKey(SupplierAccount,on_delete=models.CASCADE)
    location_tagline = models.CharField(max_length=100)
    seller_location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=44.4268)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=-26.1025)
    activities = models.ManyToManyField(Activity, null=True, blank=True)
    category = models.ManyToManyField(Category,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.location_tagline


def thumbnail_location(instance, filename):
    return "%s/%s" %(instance.activity.slug, filename)

THUMB_CHOICES = (
    ("hd", "HD"),
    ("sd", "SD"),
    ("micro", "Micro"),
)

class Thumbnail(models.Model):
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=THUMB_CHOICES, default='hd')
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    height = models.CharField(max_length=20, null=True, blank=True)
    width = models.CharField(max_length=20, null=True, blank=True) 
    media = models.ImageField(
        width_field = "width",
        height_field = "height",
        blank=True, 
        null=True, 
        upload_to=thumbnail_location)

    def __unicode__(self): 
        return str(self.media.path)

import os
import shutil
from PIL import Image
import random

from django.core.files import File

def create_new_thumb(media_path, instance, owner_slug, max_length, max_width):
        filename = os.path.basename(media_path)
        thumb = Image.open(media_path)
        size = (max_length, max_width)
        thumb.thumbnail(size, Image.ANTIALIAS)
        temp_loc = "%s/%s/tmp" %(settings.MEDIA_ROOT, owner_slug)
        if not os.path.exists(temp_loc):
            os.makedirs(temp_loc)
        temp_file_path = os.path.join(temp_loc, filename)
        if os.path.exists(temp_file_path):
            temp_path = os.path.join(temp_loc, "%s" %(random.random()))
            os.makedirs(temp_path)
            temp_file_path = os.path.join(temp_path, filename)

        temp_image = open(temp_file_path, "w")
        thumb.save(temp_image)
        thumb_data = open(temp_file_path, "rb")

        thumb_file = File(thumb_data)
        instance.media.save(filename, thumb_file)
        shutil.rmtree(temp_loc, ignore_errors=True)
        return True

def activity_post_save_receiver(sender, instance, created, *args, **kwargs):
    if instance.media:
        hd, hd_created = Thumbnail.objects.get_or_create(activity=instance, type='hd')
        sd, sd_created = Thumbnail.objects.get_or_create(activity=instance, type='sd')
        micro, micro_created = Thumbnail.objects.get_or_create(activity=instance, type='micro')

        hd_max = (500, 500)
        sd_max = (350, 350)
        micro_max = (150, 150)

        media_path = instance.media.path
        owner_slug = instance.slug
        if hd_created:
            create_new_thumb(media_path, hd, owner_slug, hd_max[0], hd_max[1])
        
        if sd_created:
            create_new_thumb(media_path, sd, owner_slug, sd_max[0], sd_max[1])

        if micro_created:
            create_new_thumb(media_path, micro, owner_slug, micro_max[0], micro_max[1])



post_save.connect(activity_post_save_receiver,sender=Activity)

class MyActivities(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    actvity = models.ManyToManyField(Activity, blank=True)


    def __unicode__(self):
        return "%s" %(self.activity.count())

    class Meta:
        verbose_name = "My Activity"
        verbose_name_plural = "My Activities"

class ActivityRating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" %(self.rating)




# def image_upload_to(instance,filename):
#     location_folder = "activities/%s/%s"
#     # title = instance.activity.title
#     # slug = slugify(title)
# #     # basename, file_extension = filename.split(".")
# #     # new_filename = "%s-%s/%s" % (slug, instance.id,file_extension)
# #     return "activities/%s/%s" % (slug, filename)


# class ActivityImage(models.Model):
#     activity = models.ForeignKey(Activity,on_delete=models.CASCADE,)
#     image = models.ImageField(upload_to=image_upload_to)

#     def __str__(self):
#         return self.activity.title

# class Tag(models.Model):
#      title = models.CharField(max_length=120, unique=True)
#     slug = models.SlugField(unique=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#       return self.title
    
#     def get_absolute_url(self):
#       view_name = "tags:title"
#       return reverse(view_name, kwargs={"slug": self.slug})

# def tag_pre_save_receiver(sender, instance, *args, **kwargs):
#   if not instance.slug:
#       instance.slug = slugify(instance.title)

# def image_upload_to(instance,filename):
#     title = instance.Activity.title
#     slug = slugify(title)
#     return "core/%s/%s" % (slug, filename)


# class ActivityImage(models.Model):
#     activities = models.ForeignKey(Activity,on_delete=models.CASCADE,)
#     image = models.ImageField(upload_to=image_upload_to)
#     title = models.CharField(max_length=120,null=True,blank=True)
#     featured_image = models.BooleanField(default=False)
#     delete_image = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated = models.DateTimeField(auto_now_add=True,auto_now=False)

#     def __str__(self):
#         return self.title


