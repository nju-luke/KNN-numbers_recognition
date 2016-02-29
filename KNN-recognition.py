# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:20:02 2016

@author: nju-hyhb
"""
from numpy import *
import operator
from os import listdir

def fileSize(filename):
    fr=open(filename)
    rowNums=int(len(fr.readlines()))
    fr=open(filename)
    colNums=int(len(fr.readline()))-1
    return rowNums,colNums

def image2array(filename,rowNums,colNums):
    fr=open(filename)
    returnArray=zeros((rowNums,colNums))
    for row in range(rowNums):
        line=fr.readline()
        for col in range(colNums):
            returnArray[row,col]=int(line[col])    
    return returnArray

def classifyNum(ArrUnderTest,ArrTraining,LabelsTraining,k):
    trainShape=shape(ArrTraining)
    trainNums=trainShape[2]
    distence=zeros(trainNums)
    for index in range(trainNums):
        distence[index]=sqrt(sum((ArrUnderTest-ArrTraining[:,:,index])**2))
    disAddLab=sorted(zip(distence,LabelsTraining))
    labelsTest=0
    for index in range(k):
        labelsTest+=disAddLab[k][1]
    labelsTest/=k
    return labelsTest    

def main():
    k=3
    trainingList=listdir('trainingDigits')
    trainSize=len(trainingList)
    rows,cols=fileSize(trainingList[0])
    trainingData=zeros((rows,cols,trainSize))
    trainingLabels=zeros(trainSize)
    
    for index in range(trainSize):
        filename=trainingList[index]    
        trainingData[:,:,index]=image2array('trainingDigits/%s' % filename,rows,cols)
        trainingLabels[index]=int(filename.split('_')[0])
       
    testingList=listdir('testDigits')
    testSize=len(testingList)
    testingData=zeros((rows,cols))
    testLabels = zeros(testSize)
    testLabels_rec=zeros(testSize)
    
    for index in range(testSize):
        filename=testingList[index]    
        testingData=image2array('testDigits/%s' % filename,rows,cols)
        testLabels[index]=int(filename.split('_')[0])
        testLabels_rec[index]=classifyNum(testingData,trainingData,trainingLabels,k)
     
    count=0
    for index in range(testSize):
        if testLabels[index]==testLabels_rec[index]:
            break
        count+=1
    accu=(1-count/testSize)*100
    
    print 'The accuracy  of the classifier is:%s%%' % accu

if __name__=='__main__':
    main()





