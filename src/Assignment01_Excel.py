#!/usr/bin/python3
import pandas as pd
import numpy as np
import re
import os

def classify(height, weight, classFHW, testHeight, testWeight):
    
    minimumDis = np.sqrt((height[0]-testHeight)**2 + (weight[0]-testWeight)**2)
    testObjClass = classFHW[0]
    for ht, wt, cl in zip(height, weight, classFHW):
        eucledianDis = np.sqrt((ht-testHeight)**2 + (wt-testWeight)**2)
        if eucledianDis < minimumDis:
            minimumDis = eucledianDis
            testObjClass = cl
    return testObjClass


def main():
    height = []
    weight=[]
    classFHW = []

    inputFolder = r'/home/cseku160212/PycharmProjects/PatternRecognition/Input'
    os.chdir(inputFolder)
    df = pd.read_excel('inputFile.xlsx')
    height = df['Height']
    weight = df['Weight']
    classFHW = df['Class']
    while(1):
        testHeight = float(input("Enter Test Height(inch): "))
        testWeight = float(input("Enter Test Weight(kg): "))
        objectClass = classify(height, weight, classFHW, testHeight, testWeight)
        print("\nObject Class is: ", objectClass)
        print()


if __name__ == "__main__":
    main()