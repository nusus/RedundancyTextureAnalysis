#!/user/bin/env python
# -*- coding:utf8 -*-
import os
import ConfigParser
import xlwt
from SingleSceneMultiAnalyze import SingleSceneMultiAnalyze

class MultiSceneMultiAnalyze(object):
    def __init__(self, configName):
        self.__ReadConfig(configName)
        self.__RootDir = self.__GetRootDir()
        if(os.path.isdir(self.__RootDir)):
            os.chdir(self.__RootDir)
        else:
            print(self.__RootDir + ' is not a dir')

    def __ReadConfig(self, filename):
        if (os.path.isfile(filename) == False):
            print("config filename is not a file")
            return
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(filename)

    def __GetRootDir(self):
        return self.__configParser.get("RootDir", "rootDir")

    def AnalyzeAll(self):     
        for folder in os.listdir('./'):
            if(os.path.isdir(folder)):
                os.chdir(folder)
                self.AnalyzeSingleScene(folder)           
                os.chdir('../')

    def AnalyzeSingleScene(self, sceneName):
        ssma = SingleSceneMultiAnalyze(sceneName)
        ssma.AnalyzeAllSamples()
        ssma.WriteResult2Excel()


if __name__ == '__main__':
    configFile = 'multiSceneMultiAnalyze.config.ini'
    if(os.path.isfile(configFile)):
        msma = MultiSceneMultiAnalyze(configFile)
        msma.AnalyzeAll()