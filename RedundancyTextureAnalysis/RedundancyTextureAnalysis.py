#!/user/bin/env python
# -*- coding:utf8 -*-
import os
import csv
import ConfigParser
import inspect


#version 1
#deprecated
'''
class RedundancyTextureAnalysis(object):
    def __init__(self, configFile):
        self.__inputSectionName = "InputDir"
        self.__inputDir1Key = "dir1"
        self.__inputDir2Key = "dir2"
        self.__outputSectionName = "OutputDir"
        self.__outputFileKey = "saveFileSuffix"
        self.__ignoreSectionName = "Ignore"
        self.__ReadConfig(configFile)
        self.__rootDir = self.__GetRootDir()

    def __GetFileNamesInDir(self, path):
        fileList = []
        if (os.path.isdir(path)):
            tmpFileNames = os.listdir(path)
            if (len(tmpFileNames) > 0):
                for fn in tmpFileNames:
                    if (os.path.isfile(path + '/' + fn)):
                        fileList.append(fn)
                    else:
                        print(fn + " is not a file in the " + path)
            else:
                print("there is no files in the" + path)
        else:
            print(path + " is not a dir name")
        return fileList

    def __GetRedundancyTextures(self, dir1, dir2):
        fileList1 = self.__GetFileNamesInDir(dir1)
        fileList2 = self.__GetFileNamesInDir(dir2)
        ignoreList = self.__configParser.options(self.__ignoreSectionName)
        redundancyTextures = []
        for f1 in fileList1:
            for f2 in fileList2:
                if (cmp(f1, f2) == 0):
                    if f1 in ignoreList:
                        pass
                    else:
                        redundancyTextures.append(f1)
        if (len(redundancyTextures) <= 0):
            print("there is no redundancy textures in the " + dir1 + " and " + dir2)
        return redundancyTextures

    def __ReadConfig(self, filename):
        if (os.path.isfile(filename) == False):
            print("config filename is not a file")
            return
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(filename)

    def __GetValueByName(self, sectionName, keyName):
        return self.__rootDir + self.__configParser.get(sectionName, keyName)

    def __GetRootDir(self):
        return self.__configParser.get("RootDir", "rootDir")

    def SaveAnalysisResultToFile(self):
        osn = self.__rootDir + self.__configParser.get(self.__inputSectionName,
                                                       self.__inputDir1Key) + '_' + self.__configParser.get(
            self.__inputSectionName, self.__inputDir2Key) + self.__configParser.get(self.__outputSectionName,
                                                                                    self.__outputFileKey)
        with open(osn, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            fileList = self.__GetRedundancyTextures(self.__GetValueByName(self.__inputSectionName, self.__inputDir1Key),
                                                    self.__GetValueByName(self.__inputSectionName, self.__inputDir2Key))
            for filename in fileList:
                spamwriter.writerow([filename])

    def CompareAllScenes(self):
        dirList = []
        for dir in os.listdir(self.__rootDir):
            if (os.path.isdir(self.__rootDir + dir)):
                dirList.append(dir)
        dirCount = len(dirList)
        if (dirCount > 0):
            for i in range(0, dirCount):
                for j in range(i + 1, dirCount):
                    osn = self.__rootDir + dirList[i] + '_' + dirList[j] + self.__configParser.get(
                        self.__outputSectionName, self.__outputFileKey)
                    with open(osn, 'wb') as csvfile:
                        spamwriter = csv.writer(csvfile, dialect='excel')
                        fileList = self.__GetRedundancyTextures(self.__rootDir + dirList[i],
                                                                self.__rootDir + dirList[j])
                        for filename in fileList:
                            spamwriter.writerow([filename])

'''

#version 2
class RedundancyTextureAnalysis(object):
    def __init__(self, configFile):
        self.__inputSectionName = "InputDir"
        self.__inputDir1Key = "dir1"
        self.__inputDir2Key = "dir2"
        self.__outputSectionName = "OutputDir"
        self.__outputFileKey = "saveFileSuffix"
        self.__ignoreSectionName = "Ignore"
        self.__ReadConfig(configFile)
        self.__rootDir = self.__GetRootDir()

    def __GetFileNamesInDir(self, path):
        fileList = []
        if (os.path.isdir(path)):
            tmpFileNames = os.listdir(path)
            if (len(tmpFileNames) > 0):
                for fn in tmpFileNames:
                    if (os.path.isfile(path + '/' + fn)):
                        fileList.append(fn)
                    else:
                        print(fn + " is not a file in the " + path)
            else:
                print("there is no files in the" + path)
        else:
            print(path + " is not a dir name")
        return fileList

    def __GetRedundancyTextures(self, dir1, dir2):
        fileList1 = self.__GetFileNamesInDir(dir1)
        fileList2 = self.__GetFileNamesInDir(dir2)
        ignoreList = self.__configParser.options(self.__ignoreSectionName)
        redundancyTextures = []
        for f1 in fileList1:
            for f2 in fileList2:
                if (cmp(f1, f2) == 0):
                    if f1 in ignoreList:
                        pass
                    else:
                        redundancyTextures.append(f1)
        if (len(redundancyTextures) <= 0):
            print("there is no redundancy textures in the " + dir1 + " and " + dir2)
        return redundancyTextures

    def __ReadConfig(self, filename):
        if (os.path.isfile(filename) == False):
            print("config filename is not a file")
            return
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(filename)

    def __GetValueByName(self, sectionName, keyName):
        return self.__rootDir + self.__configParser.get(sectionName, keyName)

    def __GetRootDir(self):
        return self.__configParser.get("RootDir", "rootDir")

    def SaveAnalysisResultToFile(self):
        osn = self.__rootDir + self.__configParser.get(self.__inputSectionName,
                                                       self.__inputDir1Key) + '_' + self.__configParser.get(
            self.__inputSectionName, self.__inputDir2Key) + self.__configParser.get(self.__outputSectionName,
                                                                                    self.__outputFileKey)
        with open(osn, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            fileList = self.__GetRedundancyTextures(self.__GetValueByName(self.__inputSectionName, self.__inputDir1Key),
                                                    self.__GetValueByName(self.__inputSectionName, self.__inputDir2Key))
            for filename in fileList:
                spamwriter.writerow([filename])

    def CompareAllScenes(self):
        dirList = []
        for dir in os.listdir(self.__rootDir):
            if (os.path.isdir(self.__rootDir + dir)):
                dirList.append(dir)
        dirCount = len(dirList)
        if (dirCount > 0):
            for i in range(0, dirCount):
                for j in range(i + 1, dirCount):
                    osn = self.__rootDir + dirList[i] + '_' + dirList[j] + self.__configParser.get(
                        self.__outputSectionName, self.__outputFileKey)
                    with open(osn, 'wb') as csvfile:
                        spamwriter = csv.writer(csvfile, dialect='excel')
                        fileList = self.__GetRedundancyTextures(self.__rootDir + dirList[i],
                                                                self.__rootDir + dirList[j])
                        for filename in fileList:
                            spamwriter.writerow([filename])

if __name__ == '__main__':
    # configName = raw_input("please input the config name")
    configName = "config.ini"
    if (os.path.isfile(configName)):
        ana = RedundancyTextureAnalysis(configName)
        # ana.SaveAnalysisResultToFile()
        ana.CompareAllScenes()
