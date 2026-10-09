from configparser import ConfigParser


def getLocator(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\config.ini")
    return config.get(section, key)


def getTestData(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\testData.ini")
    return config.get(section, key)
