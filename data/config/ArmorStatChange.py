#Works only in python 3
import xml.etree.ElementTree

def run():

	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("BlockConfig.xml")

	# Basic armor
	Hp = "400"
	Armor = "0"
	Mass = "0.05"
	Description = "Cheap but resilient structural blocks."
	ListBasicArmor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown", "Glass"
	for i in ListBasicArmor:
		Xpath = ".//Basic/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Basic/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Basic/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
		Xpath = ".//Basic/" + i + "/Block/Description"
		ReplaceEverythingInPath(Tree, Xpath, Description)
	#Basic Doors
	Mass = "0.05"
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Doors/Basic/Block/Mass", Mass)

	# Standard armor
	Hp = "200"
	Armor = "4.4"
	Mass = "0.1"
	Description = "Factory processing of basic armor blocks with special hardening compound yields Standard Armor. Standard Armor has less HP per block, but has an internal structure which resists more damage from projectiles and beam weapons when stacked in layers."
	ListArmorColor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown"
	for i in ListArmorColor:
		Xpath = ".//Standard/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Standard/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Standard/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
		Xpath = ".//Standard/" + i + "/Block/Description"
		ReplaceEverythingInPath(Tree, Xpath, Description)
	Description = "Further processing of basic armor blocks yields Standard Armor. Standard Armor has less HP per block, but has an internal structure which resists more damage from projectiles and beam weapons when stacked. These specially-painted Standard Armor blocks have been emblazoned with a caution stripe pattern."
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/Mass", Mass)
	ReplaceEverythingInPath(Tree, ".//Hazard/Block/Description", Description)
	
	# Standard Equiv. Doors
	Mass = "0.15"
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/Hitpoints", Hp)
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/ArmorValue", Armor)
	ReplaceEverythingInPath(Tree, ".//Doors/Standard/Block/Mass", Mass)

	# Advanced armor
	Hp = "100"
	Armor = "15.63"
	Mass = "0.2"
	Description = "Further processing and hardening of Standard Armor results in Advanced Armor. While seemingly very brittle in terms of hitpoints, Advanced Armor's hardened composition gives much greater reinforcement per block when layered."
	ListArmorColor = "Grey", "White", "DarkGrey", "Black", "Yellow", "Orange", "Red", "Pink", "Purple", "Blue", "Teal", "Green", "Brown"
	for i in ListArmorColor:
		Xpath = ".//Advanced/" + i + "/Block/Hitpoints"
		ReplaceEverythingInPath(Tree, Xpath, Hp)
		Xpath = ".//Advanced/" + i + "/Block/ArmorValue"
		ReplaceEverythingInPath(Tree, Xpath, Armor)
		Xpath = ".//Advanced/" + i + "/Block/Mass"
		ReplaceEverythingInPath(Tree, Xpath, Mass)
		Xpath = ".//Advanced/" + i + "/Block/Description"
		ReplaceEverythingInPath(Tree, Xpath, Description)
	# Advanced Doors
	Mass = "0.3"
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