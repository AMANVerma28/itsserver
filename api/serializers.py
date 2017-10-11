from rest_framework import serializers
from api.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

#Serializer Class for model Household
class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = '__all__'

#Serializer Class for model Farm
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

#Serializer Class for model Storage
class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

#Serializer Class for model Well
class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

#Serializer Class for model Season
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

#Serializer Class for model Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

#Serializer Class for model Yield
class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = '__all__'

#Serializer Class for model Crop
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'