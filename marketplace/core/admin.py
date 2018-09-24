from django.contrib import admin
from core.models import Activity, Category, ActivityAgeInterval, ActivityLocation, Type, Thumbnail, ActivityRating, Seller



from django.conf import settings


admin.autodiscover()

class ThumbnailInline(admin.TabularInline):
    extra = 1
    model = Thumbnail


# class ActivityImageInline(admin.TabularInline):
#     extra = 1
#     model = ActivityImage


class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('__str__','description','price','order','active','categories_class','live_link')

    inlines = [ThumbnailInline]
    search_fields = ['title','description','price']
    list_filter = ['title','price','timestamp']
    prepopulated_fields = {"slug": ('title',)}
    # readonly_fields = ['categories_class']

    class Meta:
        model = Activity

    #  class Media:
    #     if hasattr(settings, 'AIzaSyCKNJPWmU88Z0wWkIpmDjrj9vrqP82igf0') and settings.GOOGLE_MAPS_API_KEY:
    #         css = {
    #             'all': ('static/static_dirs/css/admin/location_picker.css',),
    #         }
    #         js = (
    #             'https://maps.googleapis.com/maps/api/js?key={AIzaSyCKNJPWmU88Z0wWkIpmDjrj9vrqP82igf0}'.format(settings.GOOGLE_MAPS_API_KEY),
    #             'static/static_dirs/js/admin/location_picker.js',
    #         )

    # def current_price(self,obj):
    #     if obj.sale_price > 0:
    #         return obj.sale_price
    #     else:
    #         return obj.price

    def categories_class(self,objects):
        cat = []
        for i in Category.objects.all():
            link = "<a href="'/admin/core/category/' + str(i.id) + "/>" + i.title + "</a>"
            cat.append(link)
        return cat

    categories_class.allow_tags = True


    def live_link(self,objects):
        link = "<a href="'/admin/core/activity/'+ str(objects.id) + "/change>" + objects.title + "</a>"
        return link

    live_link.allow_tags = True

admin.site.register(Activity,ActivitiesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    class Meta:
        model = Category

admin.site.register(Category,CategoryAdmin)

# class SupplierAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug":('name',)}
#     class Meta:
#         model = Supplier

# admin.site.register(Supplier,SupplierAdmin)

class ActivityAgeIntervalAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug":('title',)}
    class Meta:
        model = ActivityAgeInterval

admin.site.register(ActivityAgeInterval,ActivityAgeIntervalAdmin)

class ActivityLocationAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug":('title',)}
    class Meta:
        model = ActivityLocation

admin.site.register(ActivityLocation,ActivityLocationAdmin)

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
    class Meta:
        model = Type

admin.site.register(Type,TypeAdmin)

admin.site.register(Thumbnail)

admin.site.register(ActivityRating)

admin.site.register(Seller)
