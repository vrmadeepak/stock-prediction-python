from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheck(APIView):
    def get(self, request, format=None):
        try:
            return Response(
                {
                    "message": "Servers are running...",
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )


class UserLogin(APIView):
    def post(self, request):
        print(request.data)
        return Response(
            {"message": "User Created", "user_id": None, "new_user": None},
            status=status.HTTP_200_OK,
        )
