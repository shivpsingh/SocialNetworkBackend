from django.contrib import admin
from .models import Address, Profile
from django.utils.html import mark_safe
from baton.admin import InputFilter


class ProfileGenderListFilter(admin.SimpleListFilter):
    title = 'Gender'
    parameter_name = 'gender'

    def lookups(self, request, model_profile):
        return [('M', 'Male',), ('F', 'Female',), ('O', 'Others',)]

    def queryset(self, request, queryset):
        if self.value() == 'M':
            return queryset.filter(gender='M')
        elif self.value() == 'F':
            return queryset.filter(gender='F')
        elif self.value() == 'O':
            return queryset.filter(gender='O')
        else:
            return queryset.all()


class ProfileCityListFilter(InputFilter):
    title = 'City'
    parameter_name = 'permanent_add.city'

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(permanent_add__city=str(self.value()))
        else:
            return queryset.all()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    @staticmethod
    def profile_image(model_obj):
        width = model_obj.profile_pic.width
        height = model_obj.profile_pic.height
        return mark_safe(f'<img src="{model_obj.profile_pic.url}" width="{width}" height={height} />')

    # readonly_fields = ['profile_image']
    search_fields = ('user__username',)
    list_filter = (ProfileGenderListFilter, ProfileCityListFilter)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
