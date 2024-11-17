from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
import os

def stream(request, filename):
    file_path = os.path.join(settings.HLS_DIR, filename)

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    else:
        return HttpResponseNotFound("File not found.")