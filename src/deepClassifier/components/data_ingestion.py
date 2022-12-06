from deepClassifier.entity import DataIngestionConfig
import os
import urllib.request as request
from zipfile import ZipFile
from deepClassifier import logger
from deepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        logger.info("Trying to download files ....")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started>>>>")
            filename,headers = request.urlretrieve(url=self.config.source_URL,
                            filename=self.config.local_data_file)
            logger.info("f{filename} downloded with the following info: \n{headers}")
        else:
            logger.info(f"File already exists :{get_size(Path(self.config.local_data_file))}")


    def _get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if (f.endswith("jpg")) and  ("Cat" in f or "Dog" in f)]
        

    def _preprocess(self,zf:ZipFile,file:str,working_dir:str):
        target_filepath = os.path.join(working_dir,file)
        if not os.path.exists(target_filepath):
            logger.info(f"Extracting files at :{target_filepath}")
            zf.extract(file,working_dir)
        
        if os.path.getsize(target_filepath)==0:
            logger.info(f"Removing file of {target_filepath} size  :{get_size(Path(target_filepath))}")
            os.remove(target_filepath)

            
    def unzip_and_clean(self):
        logger.info(f"unzipping files and removing unwanted files")
        with ZipFile(file=self.config.local_data_file, mode= "r")as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for file in tqdm(updated_list_of_files):
                self._preprocess(zf,file,self.config.unzip_dir)