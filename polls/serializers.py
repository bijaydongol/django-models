import polls
from polls.models import question

from rest_framework import serializers

class questionserializer(serializers.ModelSerializer):
  
  
    class Meta:
        model = question
        fields = ['id','pub_date','question_text']