from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils import timezone

from .models import Desk

@method_decorator(csrf_exempt, name='dispatch')
class CallView(View):
    def get(self, request, *args, **kwargs):
        latest_desk = Desk.objects.order_by('-datetime').first()
        
        if latest_desk:
            return JsonResponse({
                "success": True,
                "datetime": latest_desk.datetime.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return JsonResponse({"success": False, "error": "No entries found"}, status=404)

    def post(self, request, *args, **kwargs):
        desk = Desk(datetime=timezone.now())
        desk.save()
        
        return JsonResponse({"success": True})