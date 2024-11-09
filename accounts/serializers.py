from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class SignupForm(serializers.Serializer):
    username = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required=True, 
        write_only=True,
        vaildators=[validate_password]
        )
    password2 = serializers.CharField(required=True, write_only=True)
    nickname = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'nickname')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다."})
        return data
    
    def create(self, validated_data):
        return super().create(validated_data)