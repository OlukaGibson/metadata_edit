from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import SensorData

@csrf_exempt
def update_data(request):
    if request.method == 'POST':
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        

        updated_temperature = float(temperature) + 1.2
        updated_humidity = float(humidity) + 1.2
        # # Update the database
        # SensorData.objects.all().delete()  # Remove old data
        # SensorData.objects.create(temperature=temperature, humidity=humidity)
        
        response_data = {
            'message': 'Data updated successfully',
            'temperature': updated_temperature,
            'humidity': updated_humidity
            }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})    
    
def index(request):
    # sensor_data = SensorData.objects.all().first()
    # temperature = sensor_data.temperature
    # humidity = sensor_data.humidity
    temperature = 1
    humidity = 2
    return JsonResponse({'temperature': temperature, 'humidity': humidity})