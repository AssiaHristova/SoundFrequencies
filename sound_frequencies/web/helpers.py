from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def upload_file_view(request):
 #   request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
  #  return _upload_file_view(request)
    pass


@csrf_protect
def _upload_file_view(request):
    pass
