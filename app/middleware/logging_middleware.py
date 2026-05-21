from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        print(f"Request Method: {request.method}")

        print(f"Request URL: {request.url}")

        response = await call_next(request)

        print(f"Response Status Code: {response.status_code}")

        return response