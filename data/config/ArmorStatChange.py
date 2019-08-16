#Works only in python 3
import xml.etree.ElementTree

def run():

	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("BlockConfig.xml")

	# Basic armor
	Hp = "200"
	Armor = "0"
	Mass = "0.025"
	ListBasicArmor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown", "Glass"
	for i in ListBasicArmor:
		Xpath = ".//Basic/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Basic/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Basic/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/Mass", Mass)

	# Standard armor
	Hp = "1500"
	Armor = "100"
	Mass = "0.05"
	ListArmorColor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown"
	for i in ListArmorColor:
		Xpath = ".//Standard/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Standard/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Standard/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/Mass", Mass)
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/Mass", Mass)

	# Advanced armor
	Hp = "2000"
	Armor = "250"
	Mass = "0.1"
	ListArmorColor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown"
	for i in ListArmorColor:
		Xpath = ".//Advanced/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Advanced/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Advanced/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
	ReplaceEverythingInPath(Tree, ".//Doors/Advanced/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Doors/Advanced/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Doors/Advanced/Block/Mass", Mass)

	Tree.write("New_BlockConfig.xml")
	return


def ReplaceEverythingInPath(Tree, Xpath, Value):
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		Iterations.text = Value
	return


if __name__ == "__main__":
	run()