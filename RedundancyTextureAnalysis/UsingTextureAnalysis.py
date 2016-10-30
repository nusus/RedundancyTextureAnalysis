#!/user/bin/env python
# -*- coding:utf8 -*-
import os
import csv
import ConfigParser
import inspect
import re

class UsingTextureAnalysis(object):
    def __init__(self, configFile):
        self.__executeModeSectionName = "ExecuteMode"     
        self.__ReadConfig(configFile)
        self.__rootDir = self.__GetRootDir()
        os.chdir(self.__rootDir)
        self.__executeMode = self.__GetExecuteMode()

    def __ReadConfig(self, filename):
        if(os.path.isfile(filename) == False):
            print("config filename is not a file")
            return
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(filename)


    def __GetRootDir(self):
        return self.__configParser.get("RootDir", "rootDir")

    def __GetExecuteMode(self):
        return self.__configParser.get(self.__executeModeSectionName, self.__executeModeSectionName)

    def Analyze(self):
        getattr(self, self.__executeMode)()

    def AllScene(self):
        dirList = []
        for dir in os.listdir('./'):
            if(os.path.isdir(dir)):
                os.chdir(dir)
                for fn in os.listdir('./'):
                    self.__WriteResult(fn, self.__AnalyzeCommandFile(fn))
                os.chdir('../')

    def SpecificScene(self):
        speScene = self.__configParser.items('SpecificScene')
        for sceneUnit in speScene:
            scene = sceneUnit[1]
            if(os.path.isdir(scene)):
                os.chdir(scene)
                for fn in os.listdir('./'):
                    self.__WriteResult(fn, self.__AnalyzeCommandFile(fn))
                os.chdir('../')

    def __WriteResult(self, filename, usingTextureList):
        osn = 'result_' + filename
        with open(osn, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect = 'excel')
            for filename in usingTextureList:
                filename[0] = 'ID_' + filename[0] + '.bmp'
                spamwriter.writerow(filename)

    def __AnalyzeCommandFile(self, fileName):
        usingTextueList = []
        count = 0
        if(os.path.isfile(fileName)):
            with open(fileName) as f:
                csvReader = csv.reader(f)
                for row in csvReader:
                    if(len(row) > 1 ):
                        command = row[1]
                        id = self.__verifyCommand(command, row[0])
                        if(id):
                            usingTextueList.append(id)
                    
        else:
            print("Analyze Command File Failed " + fileName + " is not a file")
        return usingTextueList

    def __verifyCommand(self, command, commandOrder):
        ret = []
        patternStr = r'glBindTexture\( target =GL_TEXTURE_2D  texture =(\d+)\)'
        pattern = re.compile(patternStr)
        match = pattern.search(command)
        if match:
            ret.append(match.group(1))
            ret.append(commandOrder)
            return ret
        else:
            return match


if __name__ == '__main__':
    configName = 'UsingTextureAnalysis.config.ini'
    if(os.path.isfile(configName)):
        ana = UsingTextureAnalysis(configName)
        #ana.SaveAnalysisResultToFile()
        ana.Analyze()
