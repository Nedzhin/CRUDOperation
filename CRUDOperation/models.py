from django.db import models
import datetime

class DiseaseType(models.Model):
    diseasetype_id=models.IntegerField(primary_key=True)
    diseasetype_description=models.CharField(max_length=140)
    class Meta:
      db_table = "diseasetype"

# class Country(models.Model):
#     cname=models.CharField(max_length=50)
#     population=models.BigIntegerField
# class Disease(models.Model):
#     disease_code=models.CharField(max_length=50)
#     pathogen=models.CharField(max_length=100)
#     description=models.CharField(max_length=140)
#     id=models.ForeignKey(DiseaseType, on_delete=models.CASCADE,primary_key=True)
# class Discover(models.Model):
#     cname=models.ForeignKey(Country, on_delete=models.CASCADE)
#     disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE,primary_key=True)
#     first_enc_date = models.DateField(default=datetime.date.today())
# class Users(models.Model):
#     email=models.CharField(max_length=60)
#     name=models.CharField(max_length=30)
#     surname=models.CharField(max_length=40)
#     salary=models.IntegerField(default=500000)
#     phone=models.CharField(max_length=20)
#     cname=models.ForeignKey(Country, on_delete=models.CASCADE)
# class PublicServant(models.Model):
#     email=models.ForeignKey(Users,on_delete=models.CASCADE)
#     department=models.CharField(max_length=50)

# class Doctor(models.Model):
#     email=models.ForeignKey(Users, on_delete=models.CASCADE)
#     degree=models.CharField(max_length=20)
# class Specialize(models.Model):
#     id=models.ForeignKey(DiseaseType, on_delete=models.CASCADE,primary_key=True)
#     email=models.ForeignKey(Doctor, on_delete=models.CASCADE)
# class Record(models.Model):
#     total_death=models.IntegerField(default=200000)
#     total_patients=models.IntegerField(default=200000)
#     disease_code=models.ForeignKey(Disease,on_delete=models.CASCADE,primary_key=True)
#     cname=models.ForeignKey(Country,on_delete=models.CASCADE)
#     email=models.ForeignKey(PublicServant,on_delete=models.CASCADE)