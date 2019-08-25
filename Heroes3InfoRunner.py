from H3FormatParser import get_maps_data_list
from H3FormatParser import get_saves_list

mapsDirectory = "C:\Users\Dor Shaar\Desktop\work\Maps"
savesDirectory = "C:\Users\Dor Shaar\Desktop\work\games"

def collect_accomplished_dictionary(mapsDirectory, savesDirectory):
	mapDataList = get_maps_data_list(mapsDirectory)

	accomplishedDict = {}
	for mapData in mapDataList:
		accomplishedDict[mapData.name.lower()] = False

	saves = get_saves_list(savesDirectory, ".GM1")

	for save in saves:
		if save.lower() in accomplishedDict:
			accomplishedDict[save] = True
		# else:
		# 	print(save)

	return accomplishedDict

def calculate_complete_percentage(accomplishedDict):
	totalMaps = 0
	mapsCompleted = 0
	for map, isDone in accomplishedDict.items():
		totalMaps +=1
		if isDone == True:
			mapsCompleted +=1

	return percentage(mapsCompleted, totalMaps)

def percentage(part, whole):
  return 100 * float(part)/float(whole)


percentage = calculate_complete_percentage(collect_accomplished_dictionary(mapsDirectory, savesDirectory))
print(percentage)

# count = 0
# mapSize = "XL"
# for mapData in mapDataList:
# 	if(mapData.size == mapSize):
# 		print("Map name: " + mapData.name)
# 		print("Map size: " + mapData.size)
# 		count += 1
# 		print("\n")

# print("There are", count, " maps of size ", mapSize)

# for mapData in specificSizeList:
# 	print("Map name: " + mapData.name)
# 	print("Map size: " + mapData.size)
# 	print("\n")
