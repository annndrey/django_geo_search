from django.conf import settings
from django.db import models


from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class SupplierAccount(models.Model):
	user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,)
	managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="manager_sellers", blank=True)
	active = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)



	def __str__(self):
		return self.user.username

	# class Meta:
	# 	verbose_name = "supplier"
	# 	verbose_name_plural = "suppliers"


# Create your models here.



# class Supplier(models.Model):
#     # activities = models.ForeignKey(Activity,on_delete=models.CASCADE,)
#     name = models.CharField(max_length=120)
#     description = models.CharField(max_length=300)
#     slug = models.SlugField()
#     timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated = models.DateTimeField(auto_now_add=True,auto_now=False)

#     def __str__(self):
#         return self.name

#     class Meta:
#         app_label = "core"
#         verbose_name = "supplier"
#         verbose_name_plural = "suppliers"

# def create_supplier_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Supplier.objects.filter(slug=slug)
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

# def supplier_pre_save_reciever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)