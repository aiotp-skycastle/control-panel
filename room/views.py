import json

from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Illuminance

@method_decorator(csrf_exempt, name='dispatch')
class IlluminanceView(View):
    def get(self, request, *args, **kwargs):
        recent_illuminance = Illuminance.objects.order_by('-datetime').first()
        
        if recent_illuminance:
            return JsonResponse({
                "success": True,
                "datetime": recent_illuminance.datetime,
                "status": recent_illuminance.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        status_value = data.get('status')
        
        if status_value is not None:
            try:
                illuminance = Illuminance(datetime=timezone.now(), status=status_value)
                illuminance.save()
                return JsonResponse({"success": True}, status=201)
            except ValueError:
                return JsonResponse({"success": False, "error": "Invalid sensor value"}, status=400)
        
        return JsonResponse({"success": False, "error": "Status value is required"}, status=400)