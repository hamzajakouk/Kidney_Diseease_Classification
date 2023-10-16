import gdown
import os
import zipfile
from cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf  

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''
        Fetch data from url 
        '''
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data
            os.makedirs("artifacts/data_ingestion", exist_ok=True) 
            logger.info(f"downloading data from {dataset_url} into {zip_download_dir}")
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"downloading data from {dataset_url} into {zip_download_dir}")

        except Exception as e:
            raise e    
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True) 
        with zipfile.ZipFile(self.config.local_data, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)   


          