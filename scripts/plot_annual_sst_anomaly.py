#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	#Navigates to our data folder
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2015.nc')

	#Setting variables
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]
	
	#Slicing
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	#Creates average temperature
	temp_mean = temp_sliced.mean()
	
	#Calculate anomalies
	temp_anom = temp[:,condition_depth,:,:] - temp_mean
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

#Execute main script
if __name__ == '__main__':
	main()
