# Load the Python Standard and DesignScript Libraries
import sys
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitNodes')
import Revit
from Revit.Elements import *

from random import randrange
import random

import re

# The inputs to this node will be stored as a list in the IN variables.
df = IN[0]
room_num = IN[1]
families = IN[2]
level = IN[3]
room_bound = IN[4]
roomz = IN[5]
category = IN[6]
pattern = IN[7]
month = IN[8]
year = IN[9]


# Place your code below this line

def WO_classifier(dataset):
    if category == 'Total':
        if df[i][20] == 1:
            WO = FamilyInstance.ByPointAndLevel(families[0], rnd_point, level)
        if df[i][21] == 1:
            WO = FamilyInstance.ByPointAndLevel(families[1], rnd_point, level)
        if df[i][22] == 1:
            WO = FamilyInstance.ByPointAndLevel(families[2], rnd_point, level)
        if df[i][23] == 1:
            WO = FamilyInstance.ByPointAndLevel(families[3], rnd_point, level)

        FamilyInstance.SetParameterByName(WO, 'ID_wo', str(df[i][2]))
        FamilyInstance.SetParameterByName(WO, 'Descrp_wo', df[i][3])
        FamilyInstance.SetParameterByName(WO, 'Room_wo', df[i][26])
        FamilyInstance.SetParameterByName(WO, 'Trade_wo', str(df[i][6]))
        FamilyInstance.SetParameterByName(WO, 'Date_wo', str(df[i][13]))

    if category == 'Mechanical' and df[i][20] == 1:
        WO = FamilyInstance.ByPointAndLevel(families[0], rnd_point, level)
        FamilyInstance.SetParameterByName(WO, 'ID_wo', str(df[i][2]))
        FamilyInstance.SetParameterByName(WO, 'Descrp_wo', df[i][3])
        FamilyInstance.SetParameterByName(WO, 'Room_wo', df[i][26])
        FamilyInstance.SetParameterByName(WO, 'Trade_wo', str(df[i][6]))
        FamilyInstance.SetParameterByName(WO, 'Date_wo', str(df[i][13]))

    if category == 'General' and df[i][21] == 1:
        WO = FamilyInstance.ByPointAndLevel(families[1], rnd_point, level)
        FamilyInstance.SetParameterByName(WO, 'ID_wo', str(df[i][2]))
        FamilyInstance.SetParameterByName(WO, 'Descrp_wo', df[i][3])
        FamilyInstance.SetParameterByName(WO, 'Room_wo', df[i][26])
        FamilyInstance.SetParameterByName(WO, 'Trade_wo', str(df[i][6]))
        FamilyInstance.SetParameterByName(WO, 'Date_wo', str(df[i][13]))

    if category == 'Electrical' and df[i][22] == 1:
        WO = FamilyInstance.ByPointAndLevel(families[2], rnd_point, level)
        FamilyInstance.SetParameterByName(WO, 'ID_wo', str(df[i][2]))
        FamilyInstance.SetParameterByName(WO, 'Descrp_wo', df[i][3])
        FamilyInstance.SetParameterByName(WO, 'Room_wo', df[i][26])
        FamilyInstance.SetParameterByName(WO, 'Trade_wo', str(df[i][6]))
        FamilyInstance.SetParameterByName(WO, 'Date_wo', str(df[i][13]))

    if category == 'Construction' and df[i][23] == 1:
        WO = FamilyInstance.ByPointAndLevel(families[3], rnd_point, level)
        FamilyInstance.SetParameterByName(WO, 'ID_wo', str(df[i][2]))
        FamilyInstance.SetParameterByName(WO, 'Descrp_wo', df[i][3])
        FamilyInstance.SetParameterByName(WO, 'Room_wo', df[i][26])
        FamilyInstance.SetParameterByName(WO, 'Trade_wo', str(df[i][6]))
        FamilyInstance.SetParameterByName(WO, 'Date_wo', str(df[i][13]))


output = []

for i in range(len(df)):
    for j in range(len(room_num)):
        if df[i][26] == room_num[j]:
            rnd_point = []
            num_faces = len(room_bound[j][0])
            rnd_face = room_bound[j][0][randrange(num_faces)]
            offst_range = randrange(1000, 2000)
            offst1 = rnd_face.Offset(offst_range)
            offst2 = rnd_face.Offset(-offst_range)
            rnd = random.uniform(0, 1)
            if roomz[j].IsInsideRoom(offst1.PointAtParameter(rnd)):
                rnd_point = offst1.PointAtParameter(rnd)
            else:
                rnd_point = offst2.PointAtParameter(rnd)

            if 1 <= month <= 12 and df[i][15] == month and df[i][14] == year:
                if pattern == '':
                    WO_classifier(df)
                elif sum(x == pattern for x in df[i][3].split()) > 0:
                    WO_classifier(df)

            if month == 0 and df[i][14] == year:
                if pattern == '':
                    WO_classifier(df)
                elif sum(x == pattern for x in df[i][3].split()) > 0:
                    WO_classifier(df)

# Assign your output to the OUT variable.
OUT = i