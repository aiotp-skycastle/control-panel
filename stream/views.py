from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
from django.views import View
import os

class StreamView(View):
    def get(self, request, filename):
        file_path = os.path.join(settings.HLS_DIR, filename)

        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return HttpResponseNotFound("File not found.")