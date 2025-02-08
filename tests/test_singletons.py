import unittest
from singletons.config_manager import ConfigManager
from singletons.logger_singleton import LoggerSingleton

class TestSingletons(unittest.TestCase):

    def test_config_manager_singleton(self):
        config1 = ConfigManager()
        config2 = ConfigManager()
        
        self.assertIs(config1, config2, "ConfigManager instances are different")
        self.assertEqual(config1.get_task_priorities(), ["Low", "Medium", "High"], "Task priorities don't match")

    def test_logger_singleton(self):
        logger1 = LoggerSingleton()
        logger2 = LoggerSingleton()
        
        self.assertIs(logger1, logger2, "LoggerSingleton instances are different")
        
        logger1.log("Test message")
        logger1.error("Test error")

if __name__ == '__main__':
    unittest.main()
