import os
import gzip
from ByteToMapSizeConverter import ConvertByteToMapSize
from MapData import MapData

# Run on each maps and prints it's name and size
# Each .h3m file is a gzip compressed file.
# Map size can be found in the 6th byte from the start of the compressed GZ file.
def get_maps_data_list(mapsDirectory):
	mapsList = get_maps_list(mapsDirectory)
	mapDataList = []
	for map in mapsList:
		input = gzip.GzipFile(map, 'rb')
		input.seek(5, 0)
		mapSize = ConvertByteToMapSize(input.read(1))
		mapSize = ConvertByteToMapSize(input.read(1))
		mapName = os.path.splitext(os.path.basename(map))[0]
		mapDataList.append(MapData(mapName, mapSize))
		input.close()	

	print("Done reading HOMM3 maps names and sizes")
	return mapDataList

# Get all the maps which are not used for allies games.
def get_maps_list(mapsDirectory):
	mapsList = []
	for file in os.listdir(mapsDirectory):
	    if file.endswith(".h3m") and "llie" not in file:
	    	mapsList.append(os.path.join(mapsDirectory, file))

	return mapsList

# Get all the maps which include the given extension.
def get_saves_list(savesDirectory, extension):
	savesList = []
	for file in os.listdir(savesDirectory):
		if file.endswith(".GM1"):
			savesList.append(os.path.splitext(os.path.basename(file))[0])
			
	return savesList