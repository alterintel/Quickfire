#Works only in python 3
import xml.etree.ElementTree

global SectorRange
SectorRange = 2000

def GetBlockBehaviorConfigWeapons():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	WeaponsList = "Cannon", "Missile"
	for i in WeaponsList:
		Xpath = ".//" + i
		print ("**" + i + "**```md")
		GetWeaponStats(Tree, Xpath)
		print ("```")
	return
	
def GetWeaponStats(Tree, Xpath):
	XpathBase = Xpath + "/BasicValues"
	# Part for the damage
	Links = Tree.iterfind(XpathBase + "/Damage")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			BaseDamage = Iterations.text
	# Part for the power consumption
	Links = Tree.find(XpathBase + "/ReactorPowerConsumptionResting")
	BasePowerConsumptionResting = Links.text
	Links = Tree.find(XpathBase + "/ReactorPowerConsumptionCharging")
	BasePowerConsumptionCharging = Links.text
	# Part for the distance
	Links = Tree.find(XpathBase + "/Distance")
	BaseRange = Links.text
	# Part for the speed
	Links = Tree.find(XpathBase + "/Speed")
	BaseSpeed = Links.text
	# Part for the reload time
	Links = Tree.find(XpathBase + "/ReloadMs")
	BaseReload = Links.text
	# Part for the effects
	Links = Tree.find(XpathBase + "/EffectConfiguration/Kinetic")
	KineticEffect = Links.text
	Links = Tree.find(XpathBase + "/EffectConfiguration/Heat")
	HeatEffect = Links.text
	Links = Tree.find(XpathBase + "/EffectConfiguration/EM")
	EmEffect = Links.text
	# Pretty printing base values
	print ("< Base weapon >")
	print ("[Kinetic][" + str(KineticEffect) + "]")
	print ("[Heat][" + str(HeatEffect) + "]")
	print ("[EM][" + str(EmEffect) + "]")
	print ("[Power consumption when resting][" + str(BasePowerConsumptionResting) + "]")
	print ("[Power consumption when charging][" + str(BasePowerConsumptionCharging) + "]")
	print ("[Damage per shot][" + str(BaseDamage) + "]")
	print ("[Reload time of][" + str(float(BaseReload)/1000) + "]")
	print ("[Damage per seconds of][" + str((float(BaseDamage)*1000)/(float(BaseReload))) + "]")
	print ("[Range of][" + str(float(BaseRange) * SectorRange) + "]")
	print ("[Projectile speed of][" + str(BaseSpeed) + "]")
	
	# Part for the slaves
	XpathCombination = Xpath + "/Combination/"
	ListWeaponCombination = "Cannon", "Missile", "Beam"
	for i in ListWeaponCombination:
		Damage = GetStats(Tree, XpathCombination + i + "/Damage", BaseDamage)
		Reload = GetStats(Tree, XpathCombination + i + "/Reload", BaseReload)
		Range = GetStats(Tree, XpathCombination + i + "/Distance", BaseRange)
		Speed = GetStats(Tree, XpathCombination + i + "/Speed", BaseSpeed)
		# Pretty printing slave
		print ("< " + i + " slave >")
		print ("[Damage per shot][" + str(Damage) + "]")
		print ("[Reload time of][" + str(float(Reload)/1000) + "]")
		print ("[Damage per seconds of][" + str((float(Damage)*1000)/(float(Reload))) + "]")
		print ("[Range of][" + str(float(Range) * SectorRange) + "]")
		print ("[Projectile speed of][" + str(Speed) + "]")
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

if __name__ == "__main__":
	GetBlockBehaviorConfigWeapons()