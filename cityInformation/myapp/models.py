from django.db import models

# Create your models here.
class Province(models.Model):
    Id=models.IntegerField()
    Name=models.CharField(max_length=50)

    class Meta:
        db_table="province"

class City(models.Model):
    Id=models.IntegerField()
    ProvinceId=models.IntegerField()
    Name=models.CharField(max_length=100)

    class Meta:
        db_table="city"

class District(models.Model):
    Id=models.IntegerField()
    CityId=models.IntegerField()
    Name=models.CharField(max_length=100)

    class Meta:
        db_table="district"
