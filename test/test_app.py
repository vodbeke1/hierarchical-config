import unittest
from hierarchical_config import Config

FILES = (
    "test/test_configs/default.json", 
    "test/test_configs/application.json",
)

class TestConfig(unittest.TestCase):

    def test_config(self):
        test_config = Config(config_files=FILES)
        print(test_config.flat_dicts)

if __name__ == "__main__":
    unittest.main()


 