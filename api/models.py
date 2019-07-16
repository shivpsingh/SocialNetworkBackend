"""
1. Model Specifications:
    - a custom user model called 'Profile' which has following fields (other than name, email, etc.)
        - phone number (must be unique)
        - gender (choices are: male, female, other)
        - profile pic (an image upload field)
        - date of birth (a date or datetime field)
        - permanent address (must be a one-to-one field of Address model)
        - company address (must be a one-to-one field of Address model)
        - friends (must be a many-to-many field of Profile model)

    - the 'Address' model must contain following fields:
        - street address
        - city
        - state
        - pincode
        - country
"""

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from PIL import Image


class Address(models.Model):

    street_address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    pincode = models.IntegerField(null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.state}, {self.country}'


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone Number Must be 10 Digit.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, null=True, blank=True)
    GENDER_CHOICES = [('M', 'Male',), ('F', 'Female',), ('O', 'Others',)]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='1', null=False, blank=False)
    profile_pic = models.ImageField(upload_to='media/', default='no-img.jpg', null=True, blank=True)
    dob = models.DateField()
    permanent_add = models.OneToOneField(Address, related_name='profile_perm_add', on_delete=models.CASCADE,
                                         null=False, blank=False)
    current_add = models.OneToOneField(Address, related_name='profile_curr_add', on_delete=models.CASCADE,
                                       null=False, blank=False)
    friends = models.ManyToManyField('self', blank=True)

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 150 or img.width > 150:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)

    def __str__(self):
        return f'{self.user.username}'


