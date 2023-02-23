from rest_framework import serializers
from .models import *

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization
        fields = ['name','description']


class UserSerializer(serializers.ModelSerializer):
    
    organizations = OrganizationSerializer(read_only=True, many=True)

        
    class Meta:
            model = User
            fields = ['email','password','first_name','last_name','icon','phone','organizations']
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.save()
        return instance
    

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = User
            fields = ['email','first_name','last_name']


class OrganizationListSerializer(serializers.ModelSerializer):
    
    users = serializers.SerializerMethodField()
    
    def get_users(self, organization):
        users = organization.user_set.all()
        data = UserListSerializer(users, many=True).data
        return data 
    
    class Meta:
        model = Organization
        fields = ['name','description', 'users']
