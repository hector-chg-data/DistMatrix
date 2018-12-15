#!/usr/bin/env python3

import pandas as pd 	# read csv (deprecated, too slow)
import numpy as np 		# arrange data
import csv				# read csv (GOOD one)

import googlemaps 						# to obtain travel times
import geopy 							# easier loc wrangling
from geopy.geocoders import Nominatim 	# from address to coordinates

from itertools import tee	# not used by the moment
import time 				# to measure code execution speeds

# Setting working directory:
dirClases="/home/hector/Dropbox/Proyectos/ClasesParticulares/old/2018-2019/csvs/"
csvFile = dirClases + "Alumnos.csv"
# Calling APIKey ubication:
dirAPI = "/home/hector/Dropbox/DOCUMENTOS IMPORTANTES/Seguridad/"
APIFile = dirAPI + "API_Key-DistMatrix-maps.txt"


## Read and load csv with pandas. Time it:
#t_i_pd = time.time()
## My code:
#Alumnos_pd = pd.read_csv(csvFile, engine="python", sep=",", skiprows = 1, skipfooter = 2)
#t_f_pd = time.time()
#t_pd = t_f_pd - t_i_pd
#print("Pandas dataframe:\n", Alumnos_pd.head()) # Testing data
#print("Time elapsed reading a csv with pandas:\n", t_pd, " seconds.\n\n")

# Read and load csv with csv. Time it:
t_i_csv = time.time()
with open(csvFile, "r") as dest_f:
	data_iter = csv.reader(dest_f, delimiter = ",")
	data = [data for data in data_iter]
Alumnos_csv = np.asarray(data)
t_f_csv = time.time()
t_csv = t_f_csv - t_i_csv
print("csv:\n", Alumnos_csv[1:5, :], "\n") # Testing data
print("Time elapsed reading a csv using csv module:\n", t_csv, " seconds.\n\n")

# Cleaning dataset: REMOVING NOT USEFUL INFO: 
# rows_to_keep = [2:] #trying to make it auto (remove only those rows that are empty in 0 position)
cols_to_keep = [3, 10, 11, 12, 14]
Alumnos = Alumnos_csv[2:, cols_to_keep] # selected data to keep
print("Rows kept:\n", Alumnos[0, :], "\n")
Alumnos = Alumnos[~(Alumnos == "").all(axis=1)] # removed those rows that are not empty
print("Alumnos de los que poseo datos:\n", Alumnos[:, 0], "\n\n")
print("Dataset final:\n", Alumnos, "\n\n")

direcciones = Alumnos[:, 1]
print("Direcciones:\n", direcciones, "\n\n")
distancias = Alumnos[:, 2]
print("Distancias:\n", distancias, "\n\n")
tiempos = Alumnos[:, 3]
print("Tiempos:\n", tiempos, "\n\n")

# Loading API
with open(APIFile) as f:
	content = f.readlines()
	content = [i.strip() for i in content]
APIKey = content[0]

# Making connection to maps API. Time it:
t_i_gmapsAPI = time.time()
#gmaps = googlemaps.Client(key=API_key)
t_f_gmapsAPI = time.time()
t_gmapsAPI = t_f_gmapsAPI - t_i_gmapsAPI
print("Time elapsed connecting to google maps API:\n", t_gmapsAPI, "seconds.\n\n")
print(len(Alumnos))



#def pairwise(iterable):
#	a, b = tee(iterable)
#	next(b, None)
#	return zip(a, b)
	
#def Direction2Coordinates(location):
#	try:
#		sdfs
#	geolocator = Nominatim(user_agent="app_name")
#	location = geolocator.geocode(location)
#	return (location.latitude, location.longitude)

#type_of_transport = input()

empty_matrix = np.zeros(shape=(len(Alumnos)+1, len(Alumnos)+1))
print(empty_matrix.shape)
#for i in range(len(Alumnos)):
#	for j in range(len(Alumnos)):
#		LatOrigin = Direction2Coordinates()
