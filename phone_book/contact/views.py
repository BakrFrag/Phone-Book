from rest_framework import viewsets
from rest_framework import mixins 
from rest_framework.response import Response
from contact.models import Contact , PhoneNumber 
           
from contact.serializers import *

class ContactViewsets(mixins.CreateModelMixin , mixins.ListModelMixin, mixins.RetrieveModelMixin , viewsets.GenericViewSet):
    """
    handle operation on model contact 
    create contact and associate with mulipli numbers 
    retrieve single object
    list of contacts with username and attached numbers
    """
    queryset = Contact.objects.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ContactSerializer
        return ContactCreateSerializer
    
