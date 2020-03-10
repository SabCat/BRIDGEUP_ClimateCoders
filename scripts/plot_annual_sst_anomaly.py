#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	#Navigates to our data folder
<<<<<<< HEAD
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
=======
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2017.nc')

<<<<<<< HEAD
	#Setting variables
=======
	# Setting variables
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]
<<<<<<< HEAD
	
	#Slicing
=======

	#Slicing 
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	#Creates average temperature
	temp_mean = temp_sliced.mean()
	
	#Calculate anomalies
	temp_anom = temp[:,condition_depth,:,:] - temp_mean
<<<<<<< HEAD
	temp_anom_yr = temp_anom.mean(axis = 0).shape
		#temp_anom_yr: (2, 330, 720)
	temp_anom_depth = temp_anom.mean(axis = 0).mean(axis=0).shape
		#temp_anom_depth: (330, 720)
	#print(temp_anom_yr)
	#print(temp_anom_depth)
	print(temp_anom.mean(axis=0))

	plt.figure()
	plt.title("Sea Temperature Anomalies (2015)")
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')
	cm=plt.cm.get_cmap("viridis")
	plt.contour(lon,lat,depth,cmap=cm)
	plt.colorbar(label='--------->')
	plt.show()
=======
	#temp_anom = (12,2,330,720)
	temp_anom_yr = temp_anom.mean(axis = 0)
	print(temp_anom_yr.shape)
>>>>>>> 6b5fa747cbdf77c3660bfa173fe4f7c49eb59627

#Execute main script
if __name__ == '__main__':
	main()
