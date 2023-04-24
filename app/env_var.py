from dotenv import load_dotenv
import os
load_dotenv()

host = os.environ.get('host', 'localhost')  # rabbitmq host
queue = os.environ.get('queue', 'basic_queue')  # queue name
port = os.environ.get('port', '5672')  # rabbitmq queue port
