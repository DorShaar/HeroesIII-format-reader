from H3FormatParser import get_maps_data_list
from H3FormatParser import get_saves_list

mapsDirectory = "C:\Users\Dor Shaar\Desktop\work\Maps"
savesDirectory = "C:\Users\Dor Shaar\Desktop\work\games"

class CompletedData:
	def __init__(self, total, completed):
		self.total = total
		self.completed = completed

maps_has_only_allias = {"One Bad Day - Allied"}

maps_has_different_allies_symbol = {
	"WarlordsA",
	"Rumble in the BogsA", 
	"Realm of ChaosA", 
	"Emerald IslesA", 
	"Divided LoyaltiesA", 
	"Crimson and CloverA",
	"Barbarian BreakoutA",
}

unknown_saves = {"Rithen Falls"}

known_problematic_names_converted = {
	"A Terrible Rumor": "Terrible Rumor",
	"Darwin_s Prize": "Darwin's Prize",
	"Fearies!": "Faeries",
	"Gelea_s Champions": "Gelea's Champions",
	"Hatchet, Axe and Saw": "Hatchet Axe and Saw",
	"Heroes of Might, Not Magic": "Heroes of Might not Magic",
	"Holding the Middle": "Hold the middle",
	"Judgment Day": "Judgement Day",
	"Marchant Princes": "Merchant Princes",
	"Marshland Menance": "Marshland Menace",
	"Monk_s Retreat": "Monk's Retreat",
	"Noah_s Ark": "Noahs Ark",
	"One Bad Day": "One Bad Day - Allied",
	"Reclamination": "Reclamation",
	"Sangraal_s Thief": "Sangraal's Thief",
	"Serpent_s Treasure": "Serpents Treasure",
	"Times Up": "Time's Up",
	"Titan_s Winter": "Titans Winter",
	"Viking We Shall Go !": "A Viking We Shall Go",
	"Warlords!": "Warlords",
	"Warmongers": "Warmongers",
	"Wing Of War": "Wings of War",
	"Xathras_s Prize": "Xathras Prize"
}

maps_on_time = {
	"Back For Revenge",
	"Last Chance",
	"Land of Titans",
	"Pandora's Box",
	"Good Witch, Bad Witch",
	"Gorlam's Tentacle Swampland",
	"Twins",
	"Peacemaker",
	"Race for Ardintinny",
	"Island of Fire",
	"The Challenge",
	"The Gauntlet"
}

completed_maps_on_time = {
	"Good Witch, Bad Witch",
	"Peacemaker",
	"Island of Fire",
	"Twins",
	"Race for Ardintinny",
	"The Challenge",
}

def print_maps(accomplished_dict, status):
	for map_name, is_done in accomplished_dict.items():
		if(is_done == status):
			print "{arg0}".format(arg0=map_name)

def collect_accomplished_dictionary(mapsDirectory, savesDirectory):
	mapDataList = get_maps_data_list(mapsDirectory)

	accomplishedDict = {}
	# Inserts non alias maps-data into a dicrionary with default value false.
	for mapData in mapDataList:
		if mapData.name not in maps_has_different_allies_symbol:
			accomplishedDict[mapData.name.lower()] = False

	savesList = get_saves_list(savesDirectory, ".GM1")

	# Set values for completed maps as true.
	# In case map is misspelled, searachs in known_problematic_names_converted.
	for save in savesList:
		lowerCasedSave = save.lower()
		if lowerCasedSave in accomplishedDict:
			accomplishedDict[lowerCasedSave] = True
		elif save in known_problematic_names_converted:
			accomplishedDict[known_problematic_names_converted[save].lower()] = True

	return accomplishedDict

def collect_data(accomplishedDict):
	total_maps = 0
	maps_completed = 0
	for map, is_done in accomplishedDict.items():
		total_maps +=1
		if is_done:
			maps_completed +=1

	return CompletedData(total_maps, maps_completed)

def percentage(part, whole):
  return 100 * float(part)/float(whole)

# Start of app run.
accomplished_dict = collect_accomplished_dictionary(mapsDirectory, savesDirectory)
data = collect_data(accomplished_dict)

print "Total: {arg0}".format(arg0=data.total)
total_maps_without_time_limit = data.total-len(maps_on_time.difference(completed_maps_on_time))
print "Total maps without time limit: {arg0}".format(arg0=total_maps_without_time_limit)
print "completed: {arg0}".format(arg0=data.completed)
percentage = percentage(data.completed, total_maps_without_time_limit)
print "Percentage: {arg0}%\n".format(arg0=percentage)

print_maps(accomplished_dict, False)


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
