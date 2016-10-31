#!/user/bin/env python
# -*- coding:utf8 -*-
import os
import re
import xlwt
import csv
from SingleSceneAnalyze import SingleSceneAnalyze
#every single scene will be sampled several times
class SingleSceneMultiAnalyze(object):
    def __init__(self, sceneName):
        self.__SceneName = sceneName
        self.__Folders = []

        #get per sample data
        for fn in os.listdir("./"):
            if(os.path.isdir(fn)):
                self.__Folders.append(fn)

    def AnalyzeAllSamples(self):

        self.__Samples = {}

        textureSuffixName = '.bmp'
        excelSuffixName = '.csv'
        
        for folder in self.__Folders:
            textureList = []
            commandList = []
            os.chdir(folder)
            for fn in os.listdir('./'):
                if(os.path.isfile(fn)):
                    if(fn.endswith(textureSuffixName)):
                        textureList.append(fn)
                    if(fn.endswith(excelSuffixName)):
                        commandList = self.__AnalyzeCommandFile(fn)
            if(len(textureList) == 0 or len(commandList) == 0):
                print("len(textureList) = " + str(len(textureList)) + " len(commandList) = " + str(len(commandList)))
                return 
            else:
                sample = SingleSceneAnalyze(textureList, commandList)
                sample.Analyze()
                self.__Samples[folder] = sample
            os.chdir("../")



    def __AnalyzeCommandFile(self, fileName):
        usingTextueList = []
        count = 0
        if(os.path.isfile(fileName)):
            with open(fileName) as f:
                csvReader = csv.reader(f)
                for row in csvReader:
                    if(len(row) > 1 ):
                        command = row[1]
                        id = self.__VerifyCommand(command)
                        if(id):
                            id = 'ID_' + id + '.bmp'
                            usingTextueList.append(id)
                    
        else:
            print("Analyze Command File Failed " + fileName + " is not a file")
        return usingTextueList

    def __VerifyCommand(self, command):
        patternStr = r'glBindTexture\( target =GL_TEXTURE_2D  texture =(\d+)\)'
        pattern = re.compile(patternStr)
        match = pattern.search(command)
        if match:
            return match.group(1)
        else:
            return match

    def WriteResult2Excel(self):
        excelSuffix = '.xls'

        allTextureSet = set()
        usingTextureSet = set()
        
        for folder, sample in self.__Samples.iteritems():
            redundancyTextureSet = set(sample.GetRedundancyTextures())
            break

        for folder, sample in self.__Samples.iteritems():
            os.chdir(folder)
            wb = xlwt.Workbook(encoding='utf-8')

            allTextureSheet = wb.add_sheet("allTexture")
            count = 0
            for allTexture in sample.GetAllTextures():
                allTextureSheet.write(count, 0, allTexture)
                count  = count + 1
            allTextureSet.union(set(sample.GetAllTextures()))

            usingTextureSheet = wb.add_sheet("usingTexture")
            count = 0
            for usingTexture in sample.GetUsingTextures():
                usingTextureSheet.write(count, 0, usingTexture)
                count = count + 1
            usingTextureSet.union(set(sample.GetUsingTextures()))

            redundancyTextureSheet = wb.add_sheet("redundancyTexture")
            count = 0
            for redundancyTexture in sample.GetRedundancyTextures():
                redundancyTextureSheet.write(count, 0, redundancyTexture)
                count = count + 1
            redundancyTextureSet.intersection(set(sample.GetRedundancyTextures()))

            wb.save(folder + excelSuffix)
            os.chdir('../')

        totalWB = xlwt.Workbook(encoding='utf-8')
        totalAllTextureSheet = totalWB.add_sheet("allTexture")
        totalUsingTextureSheet = totalWB.add_sheet("usingTexture")
        totalRedundancyTextureSheet = totalWB.add_sheet("redundancyTexture")
        totalWB.save(self.__SceneName + excelSuffix)


