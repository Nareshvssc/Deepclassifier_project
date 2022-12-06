import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

class Test_read_yaml:
    yaml_files = ["tests/unit/data/empty.yaml","tests/unit/data/demo.yaml"]
    
    def __init__(self):
        pass

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(yaml_files[0]))

    def test_read_yaml_return_type(self):
        response = read_yaml(Path(yaml_files[1]))
        assert isinstance(response,ConfigBox)

    @pytest.mark.parametrize("path_to_yaml",yaml_files)
    def test_read_yaml_bad_data_inputdtype(self,path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)    