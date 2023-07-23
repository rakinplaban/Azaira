from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from project.models import *
from rest_framework.authtoken.models import Token
from datetime import datetime
# Create your views here.
@api_view(['GET'])
def index(request):
    try:
        start_datetime_str = request.GET.get('start_datetime', None)
        end_datetime_str = request.GET.get('end_datetime', None)
        user_id = request.GET.get('user_id', None)

        # Convert the datetime strings to datetime objects
        start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M:%S')

        # Modify the query to include the exact start and end datetime
        data_objects = Data.objects.filter(
            user__id=user_id,
            timestamp__range=(start_datetime, end_datetime)
        )

        serializer = DataSerializer(data_objects, many=True)
        data = {
            "status": "success",
            "user_id": user_id,
            "payload": serializer.data
        }
        return Response(data)
    except ValueError as e:
        return Response({"message": "Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS' format."},
                        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serialiser = RegisterSerializer(data=request.data)
        data = {}
        if serialiser.is_valid():
            account = serialiser.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            token , create = Token.objects.get_or_create(user=account)
            data['token'] = token.key
        else:
            data = serialiser.errors
        return Response(data)
    

