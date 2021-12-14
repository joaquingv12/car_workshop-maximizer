import etcd3
from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        try:
            load_dotenv()
            self.etcd_port = os.getenv('ETCD_PORT')
            self.etcd_client = etcd3.client(port=self.etcd_port)
        except:
            self.etcd_port = 3000
            self.etcd_client = etcd3.client(port=self.etcd_port)

        self.logger_config = {'level':os.getenv('LOG_LEVEL'),'format':os.getenv('LOG_FORMAT'),
                    'file':os.getenv('LOG_FILE'), 'rotation':os.getenv('LOG_ROTATION')} 

        self.logger_default_config = {'level':'DEBUG','format':'{time:DD-MM-YYYY at HH:mm:ss} | {level: <8} | {name: ^15}:{line: >3}  | {function: ^15} | {message}',
                    'file':'/var/tmp/car_workshop-maximizer/log.txt', 'rotation':'100MB'}
    
    def get_logger_config(self):
        return self.logger_config

    def get_logger_default_config(self):
        return self.logger_default_config
