class NewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before")
        response = self.get_response(request)
        print("After")
        return response

