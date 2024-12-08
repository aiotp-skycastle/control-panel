from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from django.utils.timezone import localtime

from .models import Desk

class CallView(APIView):
    @extend_schema(
        summary="Retrieve the latest call status",
            responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "datetime": {"type": "string", "format": "date-time"},
                }
            },
            404: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "No data available"}
                }
            }
        }
    )
    def get(self, request, *args, **kwargs):
        latest_desk = Desk.objects.order_by('-datetime').first()
        
        if latest_desk:
            return JsonResponse({
                "success": True,
                "datetime": localtime(latest_desk.datetime).strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return JsonResponse({"success": False, "error": "No entries found"}, status=404)

    @extend_schema(
        summary="Call a manager",
        responses={
            201: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True}
                }
            },
            400: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "Status value is required"}
                }
            }
        }
    )
    def post(self, request, *args, **kwargs):
        desk = Desk(datetime=timezone.now())
        desk.save()
        
        return JsonResponse({"success": True})