import unittest
from hierarchical_config import Config

FILES = (
    "test/test_configs/default.json", 
    "test/test_configs/application.json",
)

class TestConfig(unittest.TestCase):

    def test_get(self):
        test_config = Config(config_files=FILES)

        self.assertEqual(test_config.get(("resource_url", "db"), "test"), "db.com/db")
        self.assertEqual(test_config.get("resource_url_$_$_db", "test"), "db.com/db")
        self.assertEqual(test_config.get(("resource_url", "dba"), "test"), "test")

    def test_get_dunder(self):
        test_config = Config(config_files=FILES)

        self.assertEqual(test_config[("resource_url", "db")], "db.com/db")
        with self.assertRaises(Exception):
            test_config[("resource_url", "dba")]

if __name__ == "__main__":
    unittest.main()