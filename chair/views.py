import json

from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Chair

@method_decorator(csrf_exempt, name='dispatch')
class ChairView(View):
    def get(self, request, *args, **kwargs):
        latest_chair = Chair.objects.order_by('-datetime').first()
        
        if latest_chair:
            return JsonResponse({"success": True, "status": latest_chair.status, "datetime": latest_chair.datetime.strftime('%Y-%m-%d %H:%M:%S')})
        else:
            return JsonResponse({"success": False, "error": "No status found"}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            status = data.get('status')
            
            if status not in ['on', 'off']:
                return JsonResponse({"success": False, "error": "Invalid status"}, status=400)
            
            chair = Chair(datetime=timezone.now(), status=status)
            chair.save()
            
            return JsonResponse({"success": True, "status": status})
        
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)