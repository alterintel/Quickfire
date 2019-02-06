#Works only in python 3
import xml.etree.ElementTree

global SectorRange
SectorRange = 2000

def GetBlocksConfig():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/BlockConfig.xml")

	# Basic armor
	Xpath = ".//Basic/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	BasicArmor = "```md< Basic_armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]"
	# Standard armor
	Xpath = ".//Standard/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	StandardArmor = "< Standard_armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]"
	# Advanced armor
	Xpath = ".//Advanced/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	AdvancedArmor = "< Advanced_armor >\n[Mass][" + Mass + "]\n[Hitpoints][" + HP + "]\n[ArmorValue][" + Armor + "]```"
	
	print ("**ARMOR**")
	print (BasicArmor)
	print (StandardArmor)
	print (AdvancedArmor)
	
	return BasicArmor, StandardArmor, AdvancedArmor
	
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
	return BlockMass, BlockHP, BlockArmor
	
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
	
def GetBlockBehaviorConfig():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	WeaponsList = "Cannon", "Missile"
	for i in WeaponsList:
		Xpath = ".//" + i
		print ("\n\n>>>>>> For " + i + " :")
		BaseDamage = GetWeaponStats(Tree, Xpath)
		
	return
	
def GetWeaponStats(Tree, Xpath):
	XpathBase = Xpath + "/BasicValues"
	# Part for the damage
	XpathDamage = XpathBase + "/Damage"
	Links = Tree.iterfind(XpathDamage)
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			BaseDamage = Iterations.text
	# Part for the power consumption
	XpathPowerConsumptionResting = XpathBase + "/ReactorPowerConsumptionResting"
	Links = Tree.find(XpathPowerConsumptionResting)
	BasePowerConsumptionResting = Links.text
	XpathPowerConsumptionCharging = XpathBase + "/ReactorPowerConsumptionCharging"
	Links = Tree.find(XpathPowerConsumptionCharging)
	BasePowerConsumptionCharging = Links.text
	# Part for the distance
	XpathRange = XpathBase + "/Distance"
	Links = Tree.find(XpathRange)
	BaseRange = Links.text
	# Part for the speed
	XpathSpeed = XpathBase + "/Speed"
	Links = Tree.find(XpathSpeed)
	BaseSpeed = Links.text
	# Part for the reload time
	XpathReload = XpathBase + "/ReloadMs"
	Links = Tree.find(XpathReload)
	BaseReload = Links.text
	# Pretty printing base values
	print (">>> Base weapon :")
	print ("- Power consumption when resting : " + str(BasePowerConsumptionResting))
	print ("- Power consumption when charging : " + str(BasePowerConsumptionCharging))
	print ("- Damage per shot : " + str(BaseDamage))
	print ("- Reload time of : " + str(BaseReload))
	BaseDPS = (float(BaseDamage)*1000)/(float(BaseReload))
	print ("- Damage per seconds of : " + str(BaseDPS))
	FinalRange = float(BaseRange) * SectorRange
	print ("- Range of : " + str(FinalRange))
	print ("- Projectile speed of : " + str(BaseSpeed))
	
	# Part for the slaves
	XpathCombination = Xpath + "/Combination/"
	ListWeaponCombination = "Cannon", "Missile", "Beam"
	for i in ListWeaponCombination:
		XpathDamage = XpathCombination + i + "/Damage"
		Damage = GetStats(Tree, XpathDamage, BaseDamage)
		XpathReload = XpathCombination + i + "/Reload"
		Reload = GetStats(Tree, XpathReload, BaseReload)
		XpathRange = XpathCombination + i + "/Distance"
		Range = GetStats(Tree, XpathRange, BaseRange)
		XpathSpeed = XpathCombination + i + "/Speed"
		Speed = GetStats(Tree, XpathSpeed, BaseSpeed)
		# Pretty printing slave
		print (">>> " + i + " slave :")
		print ("- Damage per shot : " + str(Damage))
		print ("- Reload time of : " + str(Reload))
		DPS = (float(Damage)*1000)/(float(Reload))
		print ("- Damage per seconds of : " + str(DPS))
		FinalRange = float(Range) * SectorRange
		print ("- Range of : " + str(FinalRange))
		print ("- Projectile speed of : " + str(Speed))
	return

def GetStats(Tree, Xpath, BaseValue):
	Links = Tree.find(Xpath)
	if (Links.attrib['style'] == "nerf"):
		Value = float(BaseValue) / float(Links.attrib['value'])
	elif (Links.attrib['style'] == "buff"):
		Value = float(BaseValue) * ( 1 + float(Links.attrib['value']))
	else:
		Value = BaseValue
	return Value
	
def GetWeaponDamage(Tree, Xpath):
	XpathCannon = Xpath + "Cannon"
	XpathBeam = Xpath + "Beam"
	XpathMissile = Xpath + "Missile"
	return CannonDamage, BeamDamage, MissileDamage

if __name__ == "__main__":
	GetBlocksConfig()
	print ("\n*Remember that for all weapons the numbers are given for 1 module*")
	GetBlockBehaviorConfig()