from django.db import models


class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    age = models.IntegerField(null=True, blank=False)
    address = models.CharField(null=True, blank=False, max_length=256)
    salary = models.IntegerField(null=True, blank=True)
    join_date = models.DateTimeField(null=False, blank=False)

    @classmethod
    def create(cls, _id, name, age, address, salary, join_date):
        return cls(_id=_id, name=name, age=age, address=address, salary=salary, join_date=join_date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
