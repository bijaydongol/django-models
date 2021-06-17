from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

user=get_user_model()


IDENTIFICATION_TYPE = (
        ("others", "Others"),
)

# Create your models here.
class Teacher_info(models.Model):
    First_name=models.CharField(max_length=20,null=None)
    Middle_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20,null=None)
    Address=models.CharField(max_length=50)
    Subject=models.CharField(max_length=20)
    def __str__(self):
        return self.First_name


class student_info(models.Model):
    CLASS_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]
    First_name=models.CharField(max_length=20)
    Middle_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)
    Roll_No=models.IntegerField()
    Gender=models.BooleanField()
    Class = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
        default=1,
    )

    def __str__(self):
        return self.First_name,self.Middle_name

class AgentDetail(models.Model):
    

    user = models.OneToOneField(
    user, on_delete=models.CASCADE, related_name="agent_detail"
     )
    location = models.TextField()
    identification_type = models.CharField(choices=IDENTIFICATION_TYPE, max_length=20)
    identification_number = models.CharField(max_length=20)
    class meta:
        ordering = ['-id']
        verbos_name_plural="Agent_Detail"

   

    def __str__(self):
         return f"{self.user}"