import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig():
    # I can call the method with out creating objects
    @staticmethod
    def getApplicationURL():
        url = config.get("common data", 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userName = config.get("common data", "username")
        return userName

    @staticmethod
    def getUserPassword():
        password = config.get("common data", "password")
        return password
