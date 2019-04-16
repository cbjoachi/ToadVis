import csv
import math
#import os
#def calculatingSegments():
def writeTofile(filename,Elbows):
    file = open(filename, "w")
    for i in Elbows:
        file.write(str(i) + ',')
    file.close()
def segs(array):
    Elbows=[]
    Humeral=[]
    for row in array:  # reading in all the points from the file
        for i in range(len(array)):
            pt1x = array[i][0]
            pt1y = array[i][1]
            pt1z = array[i][2]
            pt2x = array[i][3]
            pt2y = array[i][4]
            pt2z = array[i][5]
            pt3x = array[i][6]
            pt3y = array[i][7]
            pt3z = array[i][8]
            pt4x = array[i][9]
            pt4y = array[i][10]
            pt4z = array[i][11]
            pt5x = array[i][12]
            pt5y = array[i][13]
            pt5z = array[i][14]
            pt6x = array[i][15]
            pt6y = array[i][16]
            pt6z = array[i][17]
            """Calculating all the segments"""
            segmentA = math.sqrt(((pt4x - pt5x) * (pt4x - pt5x)) + ((pt4y - pt5y) * (pt4y - pt5y)) + ((pt4z - pt5z) * (pt4z - pt5z)))
            # print(segmentA)
            segmentB = math.sqrt(((pt5x - pt6x) * (pt5x - pt6x)) + ((pt5y - pt6y) * (pt5y - pt6y)) + ((pt5z - pt6z) * (pt5z - pt6z)))
            segmentC = math.sqrt(((pt4x - pt6x) * (pt4x - pt6x)) + ((pt4y - pt6y) * (pt4y - pt6y)) + ((pt4z - pt6z) * (pt4z - pt6z)))

            segmentD= math.sqrt(((pt1x - pt2x) * (pt1x - pt2x)) + ((pt1y - pt2y) * (pt1y - pt2y))+ ((pt1z - pt2z) * (pt1z - pt2z)))

            pt5xPrime = (pt5x + (pt2x - pt4x))
            pt5yPrime = (pt5x + (pt2y - pt4y))
            pt5zPrime = (pt5x + (pt2z - pt4z))

            pt5xPrime2 = (pt5x + (pt3x - pt4x))
            pt5yPrime2 = (pt5x + (pt3y - pt4y))
            pt5zPrime2 = (pt5x + (pt3z - pt4z))

            segmentE = math.sqrt(((pt2x - pt5xPrime) * (pt2x - pt5xPrime)) + ((pt2y - pt5yPrime) * (pt2y - pt5yPrime)) + ((pt2z - pt5zPrime) * (pt2z - pt5zPrime)))
            segmentF = math.sqrt(((pt5xPrime - pt1x) * (pt5xPrime - pt1x)) + ((pt5yPrime - pt1y) * (pt5yPrime - pt1y)) + ((pt5zPrime - pt1z) * (pt5zPrime - pt1z)))

            segmentG = math.sqrt(((pt3x - pt2x) * (pt3x - pt2x)) + ((pt3y - pt2y) * (pt3y - pt2y)) + ((pt3z - pt2z) * (pt3z - pt2z)))
            segmentH = math.sqrt(((pt3x - pt5xPrime) * (pt3x - pt5xPrime)) + ((pt3y - pt5yPrime) * (pt3y - pt5yPrime)) + ((pt3z - pt5zPrime) * (pt3z - pt5zPrime)))
            segmentI = math.sqrt(((pt5xPrime2 - pt2x) * (pt5xPrime2 - pt2x)) + ((pt5yPrime2 - pt2y) * (pt5yPrime2 - pt2y)) + ((pt5zPrime2 - pt2z) * (pt5zPrime2 - pt2z)))

            """calculating the complements"""
            ElboFelectionExtentio = math.acos((((segmentC * segmentC) - (segmentA * segmentA) - (segmentB * segmentB)) / (-2 * segmentA * segmentB)))
            #ComplementOfHumeralProRet = math.acos((((segmentF)*(segmentF)) - ((segmentD)*(segmentD)) - ((segmentE) * (segmentD))) / (-2 * segmentD * segmentE))
            #HumeralDepressionElevation = math.acos((((segmentI * segmentI) - (segmentH * segmentH) - (segmentG * segmentG))/(-2 * segmentG * segmentB)))

           # humeralPR=180-ComplementOfHumeralProRet
            Elbows.append(ElboFelectionExtentio)
            #Humeral.append(ComplementOfHumeralProRet)

    writeTofile("TaloseHoplbowAngles1.csv", Elbows)
def fileread(file):
    #print(math.pi)
    pt1X = []
    pt1Y = []
    pt1Z = []
    pt2X = []
    pt2Y = []
    pt2Z = []
    pt3X = []
    pt3Y = []
    pt3Z = []
    pt4X = []
    pt4Y = []
    pt4Z = []
    pt5X = []
    pt5Y = []
    pt5Z = []
    pt6X = []
    pt6Y = []
    pt6Z = []
    AlltehPoints=[]
    with open(file,'r') as csvFile:
        csvReader=csv.reader(csvFile)
        next(csvReader)
        for row in csvReader: #reading in all the points from the file
            pt1X.append(float(row[0]))
            pt1Y.append(float(row[1]))
            pt1Z.append(float(row[2]))
            pt2X.append(float(row[3]))
            pt2Y.append(float(row[4]))
            pt2Z.append(float(row[5]))
            pt3X.append(float(row[6]))
            pt3Y.append(float(row[7]))
            pt3Z.append(float(row[8]))
            pt4X.append(float(row[9]))
            pt4Y.append(float(row[10]))
            pt4Z.append(float(row[11]))
            pt5X.append(float(row[12]))
            pt5Y.append(float(row[13]))
            pt5Z.append(float(row[14]))
            pt6X.append(float(row[15]))
            pt6Y.append(float(row[16]))
            pt6Z.append(float(row[17]))

    AlltehPoints.append(pt1X)
    AlltehPoints.append(pt1Y)
    AlltehPoints.append(pt1Z)
    AlltehPoints.append(pt2X)
    AlltehPoints.append(pt2Y)
    AlltehPoints.append(pt2Z)
    AlltehPoints.append(pt3X)
    AlltehPoints.append(pt3Y)
    AlltehPoints.append(pt3Z)
    AlltehPoints.append(pt4X)
    AlltehPoints.append(pt4Y)
    AlltehPoints.append(pt4Z)
    AlltehPoints.append(pt5X)
    AlltehPoints.append(pt5Y)
    AlltehPoints.append(pt5Z)
    AlltehPoints.append(pt6X)
    AlltehPoints.append(pt6Y)
    AlltehPoints.append(pt6Z)
    return AlltehPoints
def main():
    allpoints=fileread("atlashopS.csv")
    segs(allpoints)
if __name__== '__main__':
        main()
