#!/usr/bin/python3
import numpy as np
import re

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

    n = int(input("Enter The Total Number Of Test Data: "))

    for i in range(0, n):
        print("Enter Training Value", i+1, "Height(inch), Weight(kg), Class with space / comma between them: ", end='')
        value = input()
        value = re.split(" |,", value)

        height.append(float(value[0]))
        weight.append(float(value[1]))
        classFHW.append(value[2])

    while True:
        testHeight = float(input("Enter Test Height(inch): "))
        testWeight = float(input("Enter Test Weight(kg): "))
        objectClass = classify(height, weight, classFHW, testHeight, testWeight)
        print("\nObject Class is: ", objectClass)



if __name__ == "__main__":
    main()