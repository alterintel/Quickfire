#Works only in python 3
import xml.etree.ElementTree

def GetBlocksConfig():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/BlockConfig.xml")

	# Basic armor
	Xpath = ".//Basic/Grey/Block"
	Mass, HP, Armor, Heat, Kinetic, EM = GetArmorBlockValue(Tree, Xpath)
	BasicArmor = "< Basic armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]\n[Heat][" + Heat + "]\n[Kinetic][" + Kinetic + "]\n[EM][" + EM + "]"
	# Standard armor
	Xpath = ".//Standard/Grey/Block"
	Mass, HP, Armor, Heat, Kinetic, EM = GetArmorBlockValue(Tree, Xpath)
	StandardArmor = "< Standard armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]\n[Heat][" + Heat + "]\n[Kinetic][" + Kinetic + "]\n[EM][" + EM + "]"
	# Advanced armor
	Xpath = ".//Advanced/Grey/Block"
	Mass, HP, Armor, Heat, Kinetic, EM = GetArmorBlockValue(Tree, Xpath)
	AdvancedArmor = "< Advanced armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]\n[Heat][" + Heat + "]\n[Kinetic][" + Kinetic + "]\n[EM][" + EM + "]"
	
	#Reactors + stabilizers
	Xpath = ".//Power/Block"
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		if ("Reactor Power" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			Reactor = "< Reactor Power >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
		if ("Reactor Stabilizer" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			Stabilizers = "< Reactor Stabilizer >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
	#Chambers
	Xpath = ".//Power/GeneralChamber/Block"
	Mass, HP = GetBlockValue(Tree, Xpath)
	Chambers = "< Chambers >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
	#Shields
	Xpath = ".//Ship/Shields/Block"
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		if ("Shield Capacitor" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			ShieldCapacitor = "< Shield Capacitor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
		if ("Shield-Recharger" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			ShieldRecharger = "< Shield-Recharger >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
	#Thrusters
	Xpath = ".//Ship/Block"
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		if ("Thruster Module" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			Thruster = "< Thruster Module >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
			break
	#Weapons/Support Tools + computer
	Xpath = ".//Ship/Weapons/Block"
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		if ("Cannon Computer" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			WeaponComputer = "< Weapon Computer >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
		if ("Cannon Barrel" == Iterations.attrib['name']):
			Mass = Iterations.find("Mass").text
			HP = Iterations.find("Hitpoints").text
			WeaponBarrel = "< Weapon Barrel >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]"
	
	print ("**ARMOR**")
	print ("```md")
	print (BasicArmor)
	print (StandardArmor)
	print (AdvancedArmor)
	print ("```")
	print ("**SYSTEM BLOCKS**")
	print ("```md")
	print (Reactor)
	print (Stabilizers)
	print (Chambers)
	print (ShieldCapacitor)
	print (ShieldRecharger)
	print (Thruster)
	print (WeaponComputer)
	print (WeaponBarrel)
	print ("```")
	
	return
	
def GetArmorBlockValue(Tree, Xpath):
	# Mass
	XpathMass = Xpath + "/Mass"
	Links = Tree.find(XpathMass)
	BlockMass = Links.text
	# Hitpoints
	XpathHP = Xpath + "/Hitpoints"
	Links = Tree.find(XpathHP)
	BlockHP = Links.text
	# Armor value
	XpathArmor = Xpath + "/ArmorValue"
	Links = Tree.find(XpathArmor)
	BlockArmor = Links.text
	# Heat
	XpathMass = Xpath + "/EffectArmor/Heat"
	Links = Tree.find(XpathMass)
	BlockHeat = Links.text
	# Kinetic
	XpathMass = Xpath + "/EffectArmor/Kinetic"
	Links = Tree.find(XpathMass)
	BlockKinetic = Links.text
	# EM
	XpathMass = Xpath + "/EffectArmor/EM"
	Links = Tree.find(XpathMass)
	BlockEM = Links.text
	return BlockMass, BlockHP, BlockArmor, BlockHeat, BlockKinetic, BlockEM
	
def GetBlockValue(Tree, Xpath):
	# Mass
	XpathMass = Xpath + "/Mass"
	Links = Tree.find(XpathMass)
	BlockMass = Links.text
	# Hitpoints
	XpathHP = Xpath + "/Hitpoints"
	Links = Tree.find(XpathHP)
	BlockHP = Links.text
	return BlockMass, BlockHP
	
if __name__ == "__main__":
	GetBlocksConfig()