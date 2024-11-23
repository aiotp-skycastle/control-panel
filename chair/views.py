from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema

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
        request={
        'application/json': {
            'type': 'object',
            'properties': {
                'status': {
                    'type': 'string',
                    'enum': ['on', 'off'],
                    'description': 'Chair status to set'
                }
            },
            'required': ['status']
        }
        },
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

class StudyTimeView(APIView):
    @extend_schema(
        summary="Get today's study time",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "today_study_time_seconds": {"type": "number", "example": 3600}
                },
            },
        },
    )

    def get(self, request, *args, **kwargs):
        # 현재 날짜의 시작과 끝 시간 계산
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timezone.timedelta(days=1)

        # 오늘 날짜에 해당하는 Chair 객체 가져오기
        chair_records = Chair.objects.filter(datetime__range=(today_start, today_end)).order_by('datetime')

        total_time = 0
        on_time = None

        # Chair 기록 순회하며 앉아있던 시간 계산
        for record in chair_records:
            if record.status == 'on':
                on_time = record.datetime
            elif record.status == 'off' and on_time:
                total_time += (record.datetime - on_time).total_seconds()
                on_time = None

        # 현재 'on' 상태로 앉아 있는 경우 현재 시간까지의 시간 계산
        if on_time:
            total_time += (timezone.now() - on_time).total_seconds()

        return Response({'today_study_time_seconds': total_time})
