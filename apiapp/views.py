from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class UpdateSensorDataView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            temperature = float(request.query_params.get('temperature'))
            humidity = float(request.query_params.get('humidity'))
        except (ValueError, TypeError):
            return Response({'error': 'Invalid input data'}, status=400)

        updated_temperature = temperature + 1.2
        updated_humidity = humidity + 1.2

        response_data = {
            'message': 'Data updated successfully',
            'updated_temperature': updated_temperature,
            'updated_humidity': updated_humidity
        }
        return JsonResponse(response_data)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # from .models import SensorData


# @api_view(['GET'])
# def index(request):
#     # sensor_data = SensorData.objects.all().first()
#     # temperature = sensor_data.temperature
#     # humidity = sensor_data.humidity
#     temperature = 1
#     humidity = 2
#     context ={
#         'temperature': temperature,
#         'humidity': humidity
#         }
#     return Response(context)

# @csrf_exempt
# def update_data(request):
#     if request.method == 'GET':
#         temperature = request.POST.get('temperature')
#         humidity = request.POST.get('humidity')
        

#         updated_temperature = float(temperature) + 1.2
#         updated_humidity = float(humidity) + 1.2
#         # # Update the database
#         # SensorData.objects.all().delete()  # Remove old data
#         # SensorData.objects.create(temperature=temperature, humidity=humidity)
        
#         response_data = {
#             'message': 'Data updated successfully',
#             'temperature': updated_temperature,
#             'humidity': updated_humidity
#             }
#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Invalid request method'})    
    
# # def index(request):
# #     # sensor_data = SensorData.objects.all().first()
# #     # temperature = sensor_data.temperature
# #     # humidity = sensor_data.humidity
# #     temperature = 1
# #     humidity = 2
# #     return JsonResponse({'temperature': temperature, 'humidity': humidity})