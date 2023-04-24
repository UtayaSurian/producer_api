from rest_framework.decorators import api_view
from rest_framework.response import Response
from .producer import RabbitMQProducer
@api_view(['POST'])
def process_data(request):
    """
    To handle POST request
    :param request: POST data sends by sender
    :return: response code
    """
    producer = RabbitMQProducer()
    producer.publish_message(request.data)
    producer.close_connection()
    return Response("Success!", status=200)
