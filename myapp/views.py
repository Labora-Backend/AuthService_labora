from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
import random
from django.core.mail import send_mail
from .models import PasswordResetOTP

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    role = request.data.get("role")

    if not username or not password or not role:
        return Response({"error": "username, password, role required"})

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"})

    User.objects.create_user(
        username=username,
        password=password,
        email=email,
        role=role
    )

    return Response({"message": "User registered successfully"})



@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": "Invalid credentials"})

    refresh = RefreshToken.for_user(user)

    return Response({
        "message": "Login successful",
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user_id": user.id,
        "role": user.role
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([AllowAny])
def send_reset_otp(request):
    email = request.data.get("email")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Email not registered"}, status=404)

    otp = str(random.randint(100000, 999999))

    PasswordResetOTP.objects.create(user=user, otp=otp)

    send_mail(
        subject="Password Reset OTP",
        message=f"Your OTP is {otp}",
        from_email="noreply@labora.com",
        recipient_list=[email],
    )

    return Response({"message": "OTP sent to email"})



@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password_with_otp(request):
    email = request.data.get("email")
    otp = request.data.get("otp")
    new_password = request.data.get("new_password")

    try:
        user = User.objects.get(email=email)
        otp_obj = PasswordResetOTP.objects.filter(
            user=user, otp=otp
        ).latest('created_at')
    except:
        return Response({"error": "Invalid OTP"}, status=400)

    user.set_password(new_password)
    user.save()

    otp_obj.delete()

    return Response({"message": "Password reset successful"})




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token=request.data.get("refresh")
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response("Logout Successfully......")
    except Exception:
        return Response("Invalid Token")