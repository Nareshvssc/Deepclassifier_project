import os
import yaml
from box.exceptions import BoxValueError
from deepClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        os.chdir(Path('f:\\Deepclassifier_project'))
        with open(Path(path_to_yaml)) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file at: {path_to_yaml} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")

@ensure_annotations
def create_directories(path_to_directores:list , verbose =True):
    for path in path_to_directores:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at :{path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at :{path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path,"r") as f:
        content= json.load(f)

    logger.info(f"json data loaded from  :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"