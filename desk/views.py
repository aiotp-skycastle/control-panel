from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils import timezone

from .models import Desk, Servo

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

class ServoView(View):
    def get(self, request):
        latest_record = Servo.objects.order_by('-datetime').first()
        if latest_record:
            data = {
                'angle': latest_record.angle,
                'datetime': latest_record.datetime
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'No records found.'}, status=404)

    def post(self, request):
        angle_value = request.POST.get('angle')
        if angle_value is not None:
            try:
                angle_value = int(angle_value)
                if 0 <= angle_value <= 180:
                    new_entry = Servo.objects.create(angle=angle_value)
                    data = {
                        'angle': new_entry.angle,
                        'datetime': new_entry.datetime
                    }
                    return JsonResponse(data)
                else:
                    return JsonResponse({"error": "Angle must be between 0 and 180."}, status=400)
            except ValueError:
                return JsonResponse({"error": "Invalid angle value. Must be an integer."}, status=400)
        return JsonResponse({"error": "Angle parameter is required."}, status=400)