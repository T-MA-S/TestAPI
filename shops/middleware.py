from django.http import JsonResponse

# возможно слишком буквально, НО все, что не 200, то 400)) все по тз
class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 200 and response.status_code != 400:
            return JsonResponse({"error": "An error occurred"}, status=400)
        return response
