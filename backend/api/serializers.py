from rest_framework import serializers

from project.models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password',]

    # def create(self, validated_data):
    #     user = User.objects.create_user(username = validated_data['username'],email=validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class DataSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ['timestamp','input_value',]

    # def get_user(self, obj):
    #     return obj.user.username 

