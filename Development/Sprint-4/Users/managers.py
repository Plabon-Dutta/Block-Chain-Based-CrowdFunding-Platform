from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username Must be set")
        if not email:
            raise ValueError("Email Must be set")
        if not password:
            raise ValueError("Password Must be set")
        
        email = self.normalize_email(email)
        user = self.model(username = username, email = email, password = password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("For Superuser is_staff must be True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("For Superuser is_superuser must be True")
        if extra_fields.get('is_active') is not True:
            raise ValueError("For Superuser is_active must be True")
        return self.create_user(username, email, password, **extra_fields)