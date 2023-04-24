import logging
import datetime
import pika
import json
from app import env_var
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',
                    handlers=[logging.StreamHandler(), logging.FileHandler('system.log')])

class RabbitMQProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=env_var.host, port=env_var.port))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=env_var.queue, durable=True)

    def publish_message(self, request):
        json_data = json.dumps(request)
        self.channel.basic_publish(
            exchange="",
            routing_key="basic_queue",
            body=json_data,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        logging.info('Message sent!')

    def close_connection(self):
        self.connection.close()

