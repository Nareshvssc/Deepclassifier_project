from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallback
from deepClassifier import logger

STAGE_NAME="Preparation of call back "

def main():
    config = ConfigurationManager()
    prepare_callbacks_config= config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()   
    

if __name__=="__main__":
    try:
        logger.info(f"<<< stage {STAGE_NAME} started")
        main()
        logger.info(f"<<< stage {STAGE_NAME} ended")
    except Exception as e:
        raise e