
from . models import company
from rest_framework import serializers
import re

class companyserializer(serializers.ModelSerializer):
    
    class Meta:
        model= company
        fields='__all__'

    def validate_Strength(self, value):
        if value is not None:
            if value < 0 :
                raise serializers.ValidationError("Strength should be a positive integer")
            return value

    def validate_Company_code(self, value):
        code_pattern='^[A-Z][A-Z]\d{2}(E|N)$'
        result = re.match(code_pattern, value)
        if not result:
            raise serializers.ValidationError("company code should be there in format of HB78E 0r HB78N ")
        return value

