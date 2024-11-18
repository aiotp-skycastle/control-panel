from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Chair
from django.utils import timezone


class ChairView(APIView):
    @extend_schema(
        summary="Retrieve the latest chair status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "status": {"type": "string", "example": "on"},
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
        latest_chair = Chair.objects.order_by('-datetime').first()

        if latest_chair:
            return Response({
                "success": True,
                "status": latest_chair.status,
                "datetime": latest_chair.datetime.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return Response({
                "success": False,
                "error": "No status found"
            }, status=404)

    @extend_schema(
        summary="Create a new chair status",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean"},
                    "status": {"type": "string", "example": True}
                },
            },
            400: {
                "type": "object",
                "properties": {
                    "success": {"type": "boolean", "example": False},
                    "error": {"type": "string", "example": "Invalid status"}
                },
            }
        },
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        status = data.get('status')

        if status not in ['on', 'off']:
            raise ValidationError({"error": "Invalid status"})

        chair = Chair(datetime=timezone.now(), status=status)
        chair.save()

        return Response({"success": True, "status": status})
