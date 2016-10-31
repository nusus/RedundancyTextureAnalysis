#!/user/bin/env python
# -*- coding:utf8 -*-


class SingleSceneAnalyze(object):
    def __init__(self, fileList, commandList):
        self.__FileList = fileList
        self.__CommandList = commandList

    def Analyze(self):
        fileSet = set(self.__FileList)
        commandSet = set(self.__CommandList)
        self.__UsingTextures = list(fileSet & commandSet)
        self.__RedundancyTextures = list(fileSet - commandSet)
        self.__UsingTextures.sort()
        self.__RedundancyTextures.sort()

    def GetUsingTextures(self):
        return self.__UsingTextures

    def GetRedundancyTextures(self):
        return self.__RedundancyTextures

    def GetAllTextures(self):
        return self.__FileList


