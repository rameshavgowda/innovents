from . models import company
from rest_framework import serializers

class companyserializer(serializers.ModelSerializer):
    class Meta:
        model= company
        fields='__all__'

# def validate_company_code(self, value):
#     if value [0] !=[]] and value[1] !=[A-z] and value[2] !=[1-9] and value[3] :
#         raise serializers.ValidationError("Enter the valide company code")
#     return value
