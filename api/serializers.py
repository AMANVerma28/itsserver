from rest_framework import serializers
from api.models import *

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
#        fields = ('HID','point','income')
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'