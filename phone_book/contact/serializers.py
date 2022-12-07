from rest_framework import serializers 
from contact.models import Contact , PhoneNumber



class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    serializing phone number models
    """
    class Meta:
        model= PhoneNumber
        fields=["number"]



class ContactSerializer(serializers.ModelSerializer):
    """
    serializing contact number model 
    """
    numbers = PhoneNumberSerializer(many=True)
    class Meta:
        model = Contact
        fields = ["username","numbers"]