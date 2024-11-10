from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from accounts.models import Role, UserRole

User = get_user_model()

class SignupForm(serializers.Serializer):
    username = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required=True, 
        write_only=True,
        validators=[validate_password]
        )
    nickname = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'nickname')

    def create(self, validated_data):
        # 사용자 생성
        user = User.objects.create_user(**validated_data)
        
        # 'USER' 역할 가져오기 (없으면 생성)
        user_role, created = Role.objects.get_or_create(role='USER')
        
        # UserRole 중계 테이블에 사용자와 역할 추가
        UserRole.objects.create(user=user, role=user_role)
        
        return user