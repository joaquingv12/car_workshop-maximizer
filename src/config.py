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

        self.logger_config = {'dir':os.getenv('LOG_DIR'), 'level':os.getenv('LOG_LEVEL'),
                            'file':os.getenv('LOG_FILE'), 'format':os.getenv('LOG_FORMAT'), 
                            'date_format':os.getenv('LOG_DATE_FORMAT')} 

    def get_logger_config(self):
        return self.logger_config
