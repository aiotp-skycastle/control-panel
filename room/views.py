import json

from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Illuminance, Temperature, Pressure, Servo

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

@method_decorator(csrf_exempt, name='dispatch')
class TemperatureView(View):
    def get(self, request, *args, **kwargs):
        recent_temperature = Temperature.objects.order_by('-datetime').first()
        
        if recent_temperature:
            return JsonResponse({
                "success": True,
                "datetime": recent_temperature.datetime,
                "status": recent_temperature.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        status_value = data.get('status')
        
        if status_value is not None:
            try:
                temperature = Temperature(datetime=timezone.now(), status=status_value)
                temperature.save()
                return JsonResponse({"success": True}, status=201)
            except ValueError:
                return JsonResponse({"success": False, "error": "Invalid sensor value"}, status=400)
        
        return JsonResponse({"success": False, "error": "Status value is required"}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class PressureView(View):
    def get(self, request, *args, **kwargs):
        recent_pressure = Pressure.objects.order_by('-datetime').first()
        
        if recent_pressure:
            return JsonResponse({
                "success": True,
                "datetime": recent_pressure.datetime,
                "status": recent_pressure.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        status_value = data.get('status')
        
        if status_value is not None:
            try:
                pressure = Pressure(datetime=timezone.now(), status=status_value)
                pressure.save()
                return JsonResponse({"success": True}, status=201)
            except ValueError:
                return JsonResponse({"success": False, "error": "Invalid sensor value"}, status=400)
        
        return JsonResponse({"success": False, "error": "Status value is required"}, status=400)

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
        data = json.loads(request.body)
        angle_value = data.get('angle')
        if angle_value is not None:
            try:
                angle_value = int(angle_value)
                print(angle_value)
                if 0 <= angle_value <= 180:
                    new_entry = Servo.objects.create(datetime=timezone.now(), angle=angle_value)
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