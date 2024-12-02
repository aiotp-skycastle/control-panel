import json

from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import Illuminance, Temperature, Pressure, Servo

class IlluminanceView(APIView):
    @extend_schema(
        summary="Retrieve the latest illuminance status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "datetime": {"type": "string", "format": "date-time"},
                    "status": {"type": "number", "example": 500}
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
        recent_illuminance = Illuminance.objects.order_by('-datetime').first()
        
        if recent_illuminance:
            return JsonResponse({
                "success": True,
                "datetime": recent_illuminance.datetime,
                "status": recent_illuminance.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    @extend_schema(
        summary="Create a new illuminance status",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'number',
                        'description': 'Illuminance sensor value in lux',
                        'example': 456
                    }
                },
                'required': ['status']
            }
        },
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
                    "error": {"type": "string", "oneOf": [
                        {"example": "Status value is required"},
                        {"example": "Invalid sensor value"}
                    ]}
                }
            }
        }
    )
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

class TemperatureView(APIView):
    @extend_schema(
        summary="Retrieve the latest temperature status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "datetime": {"type": "string", "format": "date-time"},
                    "status": {"type": "number", "example": 25.5}
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
        recent_temperature = Temperature.objects.order_by('-datetime').first()
        
        if recent_temperature:
            return JsonResponse({
                "success": True,
                "datetime": recent_temperature.datetime,
                "status": recent_temperature.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    @extend_schema(
        summary="Create a new temperature status",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'number',
                        'description': 'Temperature sensor value in Celsius',
                        'example': 24.5
                    }
                },
                'required': ['status']
            }
        },
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
                    "error": {"type": "string", "oneOf": [
                        {"example": "Status value is required"},
                        {"example": "Invalid sensor value"}
                    ]}
                }
            }
        }
    )
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

class PressureView(APIView):
    @extend_schema(
        summary="Retrieve the latest pressure status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "datetime": {"type": "string", "format": "date-time"},
                    "status": {"type": "number", "example": 1013.25}
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
        recent_pressure = Pressure.objects.order_by('-datetime').first()
        
        if recent_pressure:
            return JsonResponse({
                "success": True,
                "datetime": recent_pressure.datetime,
                "status": recent_pressure.status
            }, status=200)
        else:
            return JsonResponse({"success": False, "error": "No data available"}, status=404)

    @extend_schema(
        summary="Create a new pressure status",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'number',
                        'description': 'Pressure sensor value in hPa',
                        'example': 1013.23
                    }
                },
                'required': ['status']
            }
        },
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
                    "error": {"type": "string", "oneOf": [
                        {"example": "Status value is required"},
                        {"example": "Invalid sensor value"}
                    ]}
                }
            }
        }
    )
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

class ServoView(APIView):
    @extend_schema(
        summary="Retrieve the latest servo angle status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "status": {"type": "integer", "example": 90},
                    "datetime": {"type": "string", "format": "date-time"}
                }
            },
            404: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "No records found."}
                }
            }
        }
    )
    def get(self, request):
        latest_record = Servo.objects.order_by('-datetime').first()
        if latest_record:
            data = {
                "success": True,
                'status': latest_record.angle,
                'datetime': latest_record.datetime
            }
            return JsonResponse(data)
        else:
            return JsonResponse({
                "success": False,
                'error': 'No records found.'
            }, status=404)

    @extend_schema(
        summary="Create a new servo angle status",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'angle': {
                        'type': 'integer',
                        'minimum': 0,
                        'maximum': 180,
                        'description': 'Servo motor angle (0-180 degrees)',
                        'example': 45
                    }
                },
                'required': ['angle']
            }
        },
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": True},
                    "status": {"type": "integer", "minimum": 0, "maximum": 180, "example": 90},
                    "datetime": {"type": "string", "format": "date-time"}
                }
            },
            400: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "oneOf": [
                        {"example": "Angle parameter is required."},
                        {"example": "Invalid angle value. Must be an integer."},
                        {"example": "Angle must be between 0 and 180."}
                    ]}
                }
            }
        }
    )
    def post(self, request):
        data = json.loads(request.body)
        angle_value = data.get('angle')
        if angle_value is not None:
            try:
                angle_value = int(angle_value)
                if 0 <= angle_value <= 180:
                    new_entry = Servo.objects.create(datetime=timezone.now(), angle=angle_value)
                    data = {
                        "success": True,
                        'status': new_entry.angle,
                        'datetime': new_entry.datetime
                    }
                    return JsonResponse(data)
                else:
                    return JsonResponse({"success": False, "error": "Angle must be between 0 and 180."}, status=400)
            except ValueError:
                return JsonResponse({"success": False, "error": "Invalid angle value. Must be an integer."}, status=400)
        return JsonResponse({"success": False, "error": "Angle parameter is required."}, status=400)