class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, PATCH, DELETE"  # Allowed HTTP methods
        # response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Allowed headers
        response["Access-Control-Allow-Credentials"] = True
        response["Access-Control-Max-Age"] = 3600
        return response