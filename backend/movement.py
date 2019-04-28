import csv
import math
import pandas as pd
import numpy as np
def writeTofile(filename,Elbows):
    file = open(filename, "w")
    file.write("Elbow_extension\n")
    for i in Elbows:
        file.write(str(i)+"\n")
    file.close()
def calsegments(x1,y1,z1,x2,y2,z2):
    '''math.sqrt(((pt4x - pt5x) * (pt4x - pt5x)) + ((pt4y - pt5y) * (pt4y - pt5y)) + ((pt4z - pt5z) * (pt4z - pt5z)))'''
    segment = math.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))+((z1-z2)*(z1-z2)))
    return segment


'''Calculating all the segments and angles'''
def segs(array):
    together=[];
    Humeral=[]
    Extension=[]
    Retraction=[]
    for i in range(len(array[0])):
        pt1x = array[0][i]
        pt1y = array[1][i]
        pt1z = array[2][i]
        pt2x = array[3][i]
        pt2y = array[4][i]
        pt2z = array[5][i]
        pt3x = array[6][i]
        pt3y = array[7][i]
        pt3z = array[8][i]
        pt4x = array[9][i]
        pt4y = array[10][i]
        pt4z = array[11][i]
        pt5x = array[12][i]
        pt5y = array[13][i]
        pt5z = array[14][i]
        pt6x = array[15][i]
        pt6y = array[16][i]
        pt6z = array[17][i]


        """Calculating all the segments"""
        segmentA=calsegments(pt4x,pt4y,pt4z,pt5x,pt5y,pt5z)
        segmentB=calsegments(pt5x,pt5y,pt5z,pt6x,pt6y,pt6z)
        segmentC=calsegments(pt4x,pt4y,pt4z,pt6x,pt6y,pt6z)
        '''The extension angle calculated and appended to the array of all the extension angles'''
        ElboFelectionExtentio = math.degrees(math.acos((((segmentC * segmentC) - (segmentA * segmentA) - (segmentB * segmentB))/((-2) * segmentA * segmentB))))
        compElboFelectionExtentio = 180-ElboFelectionExtentio
        Extension.append(compElboFelectionExtentio)

        pt5xPrime = (pt5x + (pt2x - pt4x))
        pt5yPrime = (pt5y + (pt2y - pt4y))
        pt5zPrime = (pt5z + (pt2z - pt4z))

        pt5xPrime2 = (pt5x + (pt3x - pt4x))
        pt5yPrime2 = (pt5y + (pt3y - pt4y))
        pt5zPrime2 = (pt5z + (pt3z - pt4z))

        segmentD = calsegments(pt1x, pt1y, pt1z, pt2x, pt2y, pt2z)
        segmentE = calsegments(pt2x, pt2y, pt2z, pt5xPrime, pt5yPrime, pt5zPrime)
        segmentF = calsegments(pt5xPrime, pt5yPrime, pt5zPrime, pt1x, pt1y, pt1z)

        '''The retractioion angle calculated and appended to the array of all the retraction angles'''
        ComplementOfHumeralProRet = math.degrees(math.acos((((segmentF * segmentF) - (segmentD * segmentD) - (segmentE * segmentE)) / ((-2) * segmentD * segmentE))))
        HumeProRetr=180-ComplementOfHumeralProRet
        Humeral.append(HumeProRetr)

        segmentG = calsegments(pt3x,pt3y,pt3z,pt2x,pt2y,pt2z)
        segmentH = calsegments(pt3x,pt3y,pt3z,pt5xPrime2,pt5yPrime2,pt5zPrime2)
        SegmentI = calsegments(pt5xPrime2,pt5yPrime2,pt5zPrime2,pt2x,pt2y,pt2z)

        """The Depression angle calculated and appended to the array of all the retraction angles"""
        HumeralDepressionElevation = math.degrees(math.acos((((SegmentI * SegmentI) - (segmentH * segmentH) - (segmentG * segmentG))/(-2 * segmentG * segmentH))))
        humeralPR=180-HumeralDepressionElevation
        Retraction.append(humeralPR)
    data={'el_fle-ext':Extension,
          'hum_dep_ele':Humeral,'hum_pro_retra':Retraction}
    df=pd.DataFrame(data)
    print(df[['el_fle-ext','hum_dep_ele','hum_pro_retra']])

    df.to_csv("CSVdata/angles.csv", encoding='utf-8', index=False)
    writeTofile("CSVdata/humeral.csv", Extension)
    writeTofile("CSVdata/humeralpro.csv", Humeral)
    #writeTofile("CSVdata/TaloseHopExtensionAngles1.csv",together)
    #writeTofile("CSVdata/TaloseHopReatractionAngles1.csv",together)
def fileread(file):
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
    allpoints=fileread("CSVdata/atlashopS.csv")
    segs(allpoints)
if __name__== '__main__':
        main()
