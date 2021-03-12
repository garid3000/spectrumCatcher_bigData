import pandas as pd
import numpy as np
import os
hdrPATH = "/data1/inoveco/inoveco_reference/"
wvFNAME = "Wavelength1-5and1-3.csv"

class Device():
	"""class for 1 day folder in the ..../data1/... folder """
	def __init__(self, sc_id):
		super(Device, self).__init__()
		self.sc_id   = sc_id
		self.dir     = os.path.join(hdrPATH, sc_id)
		self.wvFname = os.path.join(hdrPATH, wvFNAME)
		if not os.path.isdir(self.dir):
			print("there is no directory at:", self.dir)
			return False
		ret = self.read_wavelenghtCalibration()
		if not ret:
			print("Failed to get: ", self.wvFname)
			return False	
		self.fnames  = os.listdir(self.dir)


	def read_wavelenghtCalibration(self):
		if not os.path.isfile(self.wvFname):
			return False
		self.wave_pd = pd.read_csv(d)
		return True

	def set_curM_date(self, str_yyymmdd):
		tmp = os.path.join(self.dir, str_yyymmdd)
		if not os.path.isdir(tmp):
			print("didn't find date folder:", tmp)
			return False
		self.curM_dir = tmp 			#curM_dir: current Measurement Directory
		self.curM_fnames = os.listdir(self.curM_dir) 
		