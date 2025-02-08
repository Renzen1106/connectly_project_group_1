import logging

class LoggerSingleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.logger = logging.getLogger('TaskManagementAPI')
        self.logger.setLevel(logging.DEBUG)
        # You can add more handlers like file handlers here if needed
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
    
    def log(self, message):
        self.logger.debug(message)
    
    def error(self, message):
        self.logger.error(message)
