def ConvertByteToMapSize(byte):
	if (byte == "$"):
		return "Small"
	elif (byte == "H"):
		return "Meduim"
	elif (byte == "l"):
		return "Large"
	else:
		return "XL"