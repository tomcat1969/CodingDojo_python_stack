from django.db import models
from datetime import date
from datetime import datetime


def isPast(list_date):
    year = int(list_date[0])
    month = int(list_date[1])
    day = int(list_date[2])
    today = date.today()
    if year > today.year:
        return False
    elif year < today.year:
        return True
    else:
        if month > today.month:
            return False
        elif month < today.month:
            return True
        else:
            if day > today.day:
                return False
            else:
                return True


class ShowManager(models.Manager):
    def basic_validator(self,post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "title should be at least 2 characters"
        if len(post_data['network']) < 3:
            errors['network'] = "network should be at least 3 characters"
        if len(post_data['desc']) < 10 and len(post_data['desc']) != 0:
            errors['desc'] = "Description should be at least 10 characters or 0"
        mydate = post_data['release_date']
        list_date = mydate.split("-")
        if isPast(list_date) != True:
            errors['release_date'] = "release date should be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


# print("hello")
# str = '2024-09-07'
# l = str.split("-")
# print(l)
# print(isPast(l))
