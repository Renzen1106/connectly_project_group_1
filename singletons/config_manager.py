class ConfigManager:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        print("Creating ConfigManager instance...")
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.task_priorities = ["Low", "Medium", "High"]
        self.notifications_enabled = True
        # Add any other global configuration items here
    
    def get_task_priorities(self):
        return self.task_priorities
    
    def is_notifications_enabled(self):
        return self.notifications_enabled
