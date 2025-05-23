# Script for DICOM processing

from pydicom import dcmread
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

file_name = filedialog.askopenfilename()

print("Selected file:", file_name)

ds = dcmread(file_name)
description = ds[0x0008103E]
series_num = ds[0x00200011]
patients_name = ds[0x00100010]
patients_ID = ds[0x00100020]
coords = ds[0x00200032]
im_num = ds[0x00200013]
age = ds[0x00100010]
birthday = ds[0x00100030]
sex = ds[0x00100040]

description_value = str(vars(description)["_value"])
series_num_value = str(vars(series_num)["_value"])
patients_name_value = str(vars(patients_name)["_value"])
patients_ID_value = str(vars(patients_ID)["_value"])
coords_value = str(vars(coords)["_value"])
im_num_value = str(vars(im_num)["_value"])
age_value = str(vars(age)["_value"])
birthday_value = str(vars(birthday)["_value"])
sex_value = str(vars(sex)["_value"])

print("Serie:", series_num_value + "-" + description_value)
print("Patient´s Name:", patients_name_value)
print("Patient´s ID:", patients_ID_value)
print("Image Position Patient:", coords_value)
print("Image Number:", im_num_value)
print("Age:", age_value)
print("Birthday:", birthday_value)
print("Sex:", sex_value)

# Další možnosti

"""for element in ds:
    print(element)"""
