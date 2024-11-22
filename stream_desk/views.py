from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from django.conf import settings
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os

class StreamDeskView(View):
    def get(self, request, filename):
        file_path = os.path.join(settings.HLS_DESK_DIR, filename)

        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return HttpResponseNotFound("File not found.")

@method_decorator(csrf_exempt, name='dispatch')
class StreamDeskUploadView(View):
    def post(self, request):
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file provided.'}, status=400)
        
        uploaded_file = request.FILES['file']
        filename = uploaded_file.name
        file_path = os.path.join(settings.HLS_DESK_DIR, filename)

        # Ensure the directory exists
        os.makedirs(settings.HLS_DESK_DIR, exist_ok=True)

        # Save the uploaded file
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({'success': True, 'message': f'File {filename} saved successfully.'}, status=201)