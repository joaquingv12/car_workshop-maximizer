import etcd3
from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv(dotenv_path='src/config.env')
        try:
            self.etcd_port = os.getenv('ETCD_PORT')
            self.etcd_client = etcd3.client(port=self.etcd_port)
        except:
            self.etcd_port = 3000
            self.etcd_client = etcd3.client(port=self.etcd_port)

        self.logger_config = {'level':os.getenv('LOG_LEVEL'),'format':os.getenv('LOG_FORMAT'),
                    'file':os.getenv('LOG_FILE'), 'rotation':os.getenv('LOG_ROTATION')} 

    def get_logger_config(self):
        return self.logger_config
