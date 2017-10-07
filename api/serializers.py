from rest_framework import serializers
from api.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
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

"""
class HPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household_Photo
        fields = '__all__'

class HASerializer(serializers.ModelSerializer):
    class Meta:
        model = Household_Audio
        fields = '__all__'

class HVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household_Video
        fields = '__all__'

class FPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm_Photo
        fields = '__all__'

class WPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well_Photo
        fields = '__all__'

class SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage_Photo
        fields = '__all__'

class FVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm_Video
        fields = '__all__'
"""