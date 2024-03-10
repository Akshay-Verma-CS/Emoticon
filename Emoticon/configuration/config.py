import json
import os

class configHelper:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(configHelper,cls).__new__(cls)
            cls._instance.loadConfig()
        return cls._instance
    
    def loadConfig(self):
        configPath  = os.getcwd() + "/Emoticon/configuration/config.json"
        with open(configPath,"r") as f:
            self.__config = json.load(f)
            for key,value in self.__config.items():
                self.__setattr__(key,value)

    def getConfig(self):
        return self.__config