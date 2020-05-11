# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:33:13 2020

@author: lajamu
"""
import re, openpyxl

f = open("pentabase4_5.txt", "r")
x = f.read()



rx  = r"Transferring 200.0 from [A-D][1-6] of Opentrons 24 Well Aluminum Block with Generic 2 mL Screwcap on [0-9]+ to [A-H][0-9]+ of Nunc 96 Well Plate 1300 µL on [0-9]"

transfer_list = re.findall(rx, x)

def get_pos(s):
    rackWell = s[24:26]
    rackSlot = re.findall("Screwcap on ([0-9]+)", s)[0]
    plateWell = re.findall("([A-H][0-9]+) of Nunc", s)[0]
    plateSlot = s[-1]
    x = [rackSlot, rackWell, plateSlot, plateWell]
    return(x)

transfer_indices = []

for i in transfer_list:
    transfer_indices.append(get_pos(i))

wb = openpyxl.Workbook()
ws = wb.active
for x in transfer_indices:
    ws.append(x)
    
wb.save("Transfer.xlsx")