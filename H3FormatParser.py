import os
import gzip

class MapData:
	def __init__(self, name, size):
		self.name = name
		self.size = size
	
mapsDirectory = "C:\Users\Dor Shaar\Desktop\work\Maps"
mapsList = []

# Get all the maps which are not used for allies games.
for file in os.listdir(mapsDirectory):
    if file.endswith(".h3m") and "Allie" not in file:
    	mapsList.append(os.path.join(mapsDirectory, file))

mapDataList = []

# Run on each maps and prints it's name and size
# Each .h3m file is a gzip compressed file.
# Map size can be found in the 6th byte from the start of the compressed GZ file.
# Map name can be found 
for map in mapsList:
	input = gzip.GzipFile(map, 'rb')
	input.seek(5, 0)
	mapSize = input.read(1)
	mapName = os.path.splitext(os.path.basename(map))[0]
	mapDataList.append(MapData(mapName, mapSize))
	input.close()

for mapData in mapDataList:
	print("Map name: " + mapData.name)
	print("Map size: " + mapData.size)
	print("\n")

print("Done reading HOMM3 maps names and sizes")