from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils import timezone

from .models import Desk

@method_decorator(csrf_exempt, name='dispatch')
class CallView(View):
    def post(self, request, *args, **kwargs):
        desk = Desk(datetime=timezone.now())
        desk.save()
        
        return JsonResponse({"success": True})