from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema

from .models import Buzzer
from django.utils import timezone

# Create your views here.
class BuzzerView(APIView):
    @extend_schema(
        summary="Retrieve the latest buzzer status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "datetime": {"type": "string", "format": "date-time"}
                },
            },
            404: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "No status found"}
                },
            }
        },
    )
    def get(self, request, *args, **kwargs):
        latest_buzzer = Buzzer.objects.order_by('-datetime').first()

        if latest_buzzer:
            return Response({
                "success": True,
                "datetime": latest_buzzer.datetime.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return Response({
                "success": False,
                "error": "No status found"
            }, status=404)

    @extend_schema(
        summary="Create a new desk alert",
        request={
        'application/json': {
            'type': 'object',
            'properties': {
            },
            'required': ['status']
        }
        },
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                },
            },
        },
    )
    def post(self, request, *args, **kwargs):
        buzzer = Buzzer(datetime=timezone.now())
        buzzer.save()

        return Response({"success": True})