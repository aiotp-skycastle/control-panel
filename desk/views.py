from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import Desk

class CallView(APIView):
    @extend_schema(
        summary="Retrieve the latest call status",
    )
    def get(self, request, *args, **kwargs):
        latest_desk = Desk.objects.order_by('-datetime').first()
        
        if latest_desk:
            return JsonResponse({
                "success": True,
                "datetime": latest_desk.datetime.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return JsonResponse({"success": False, "error": "No entries found"}, status=404)

    @extend_schema(
        summary="Call the manager",
    )
    def post(self, request, *args, **kwargs):
        desk = Desk(datetime=timezone.now())
        desk.save()
        
        return JsonResponse({"success": True})