from rest_framework import serializers 
from contact.models import Contact , PhoneNumber
from django.db import transaction


class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    serializing phone number models
    """
  
    class Meta:
        model= PhoneNumber
        fields=["number"]


        



     
class ContactSerializer(serializers.ModelSerializer):
    """
    contact serializer
    """
    numbers = serializers.StringRelatedField(many=True, read_only=True)
   
    class Meta:
        model = Contact
        fields = ["username","numbers"]
class ContactCreateSerializer(serializers.ModelSerializer):
    """
    serializing contact number model 
    """
    numbers = PhoneNumberSerializer(many=True ,write_only=True)
    class Meta:
        model = Contact
        fields = ["username","numbers"]


    def create(self , validated_data):
        """
        custom logic for insert contact name and associate it with multpli phone numbers , wrapp with transaction to prevent create usernames without numbers
        """
        with transaction.atomic():
            contact = validated_data.pop("username")
            contact , created  = Contact.objects.get_or_create(username=contact)
            for number in validated_data.get("numbers"):
                PhoneNumber.objects.create(
                    **number
                    , contact=contact
                )
            return contact
        
