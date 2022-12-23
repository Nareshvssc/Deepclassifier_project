from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation

try:
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()
    evaluation.log_into_mlflow()
    
except Exception as e:
   raise e