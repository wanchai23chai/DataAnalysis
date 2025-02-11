######### Check Sampling Rate #############
from os import listdir
from os.path import isfile, join
import pyedflib
import numpy as np
from scipy.stats import kurtosis
import os
#import shutil

### You must create folder name = "edf" and put file .edf in folder ###
mypath ="..\edf\edf"
FileName = [f for f in listdir(mypath) if f.endswith(".edf")]
print(FileName)
for numFile in np.arange(len(FileName)):
	fullpath = mypath+"\\"+FileName[numFile]
	print(numFile+1,"-----------------"+FileName[numFile]+"-----------------")
	###################  Section read EDF file ##################
	f = pyedflib.EdfReader(fullpath)
	n = f.signals_in_file
	sampleN =f.getNSamples()[2]/min(f.getNSamples())
	if (sampleN==125):
		print("125")
		
	if (sampleN==128):
		print("128")
		f._close()
		os.rename("..\\edf\\edf\\"+FileName[numFile],"..\\edf\\EDF_8Hz\\"+FileName[numFile])
		print("move complete"+FileName[numFile])
	#shutil.move("..\\edf\\edf\\test.txt", "..\\edf\\EDF_8Hz\\")
	

	############### end section read file EDF ##############

