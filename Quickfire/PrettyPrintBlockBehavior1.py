#Works only in python 3
import xml.etree.ElementTree

global SectorRange
SectorRange = 2000

def GetBasicBlockEffect(Tree, Xpath):
	Links = Tree.find(Xpath + "BasicEffectConfiguration/Kinetic")
	BasicEffectKinetic = Links.text
	Links = Tree.find(Xpath + "BasicEffectConfiguration/Heat")
	BasicEffectHeat = Links.text
	Links = Tree.find(Xpath + "BasicEffectConfiguration/EM")
	BasicEffectEM = Links.text
	print ("\n**SYSTEMS**")
	print ("```md")
	print ("[BasicEffectConfiguration]")
	print ("[Kinetic][" + BasicEffectKinetic + "]")
	print ("[Heat][" + BasicEffectHeat + "]")
	print ("[EM][" + BasicEffectEM + "]")
	print ("```")
	return

def GetArmorConfig(Tree, Xpath):
	Links = Tree.find(Xpath + "CannonArmorExponentialIncomingExponent")
	CannonArmorExponentialIncomingExponent = Links.text
	Links = Tree.find(Xpath + "CannonArmorExponentialArmorValueTotalExponent")
	CannonArmorExponentialArmorValueTotalExponent = Links.text
	Links = Tree.find(Xpath + "CannonArmorExponentialIncomingDamageAddedExponent")
	CannonArmorExponentialIncomingDamageAddedExponent = Links.text
	Links = Tree.find(Xpath + "BeamArmorExponentialIncomingExponent")
	BeamArmorExponentialIncomingExponent = Links.text
	Links = Tree.find(Xpath + "BeamArmorExponentialArmorValueTotalExponent")
	BeamArmorExponentialArmorValueTotalExponent = Links.text
	Links = Tree.find(Xpath + "BeamArmorExponentialIncomingDamageAddedExponent")
	BeamArmorExponentialIncomingDamageAddedExponent = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/Kinetic")
	ArmorEffectKinetic = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/Heat")
	ArmorEffectHeat = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/EM")
	ArmorEffectEM = Links.text
	print ("**ARMOR**")
	print ("```md")
	print ("< Cannon formula >")
	print ("Armor formula is : (Incoming_Damage^(" + CannonArmorExponentialIncomingExponent + "))/(SUM_of_Armor_value_in_line_of_shot^(" + CannonArmorExponentialArmorValueTotalExponent + ") + Incoming_Damage^(" + CannonArmorExponentialIncomingDamageAddedExponent + "))\n")
	print ("< Beam formula >")
	print ("Armor formula is : (Incoming_Damage^(" + BeamArmorExponentialIncomingExponent + "))/(SUM_of_Armor_value_in_line_of_shot^(" + BeamArmorExponentialArmorValueTotalExponent + ") + Incoming_Damage^(" + BeamArmorExponentialIncomingDamageAddedExponent + "))\n")
	print ("[ArmorEffectConfiguration]")
	print ("[Kinetic][" + ArmorEffectKinetic + "]")
	print ("[Heat][" + ArmorEffectHeat + "]")
	print ("[EM][" + ArmorEffectEM + "]")
	print ("```")
	return
	
def GetShieldConfig(Tree, Xpath):
	Links = Tree.find(Xpath + "ShieldLocalCapacityPerBlock")
	ShieldLocalCapacityPerBlock = Links.text
	Links = Tree.find(Xpath + "ShieldLocalRechargePerBlock")
	ShieldLocalRechargePerBlock = Links.text
	Links = Tree.find(Xpath + "ShieldUpkeepPerSecondOfTotalCapacity")
	ShieldUpkeepPerSecondOfTotalCapacity = Links.text
	Links = Tree.find(Xpath + "ShieldLocalPowerConsumptionPerRechargePerSecondResting")
	ShieldLocalPowerConsumptionPerRechargePerSecondResting = Links.text
	Links = Tree.find(Xpath + "ShieldLocalPowerConsumptionPerRechargePerSecondCharging")
	ShieldLocalPowerConsumptionPerRechargePerSecondCharging = Links.text
	Links = Tree.find(Xpath +  "ShieldEffectConfiguration/Kinetic")
	ShieldEffectKinetic = Links.text
	Links = Tree.find(Xpath +  "ShieldEffectConfiguration/Heat")
	ShieldEffectHeat = Links.text
	Links = Tree.find(Xpath +  "ShieldEffectConfiguration/EM")
	ShieldEffectEM = Links.text
	print ("**SHIELDS**")
	print ("```md")
	print ("[Shield capacity per block][" + ShieldLocalCapacityPerBlock + "]")
	print ("[Shield upkeep per block][" + str(float(ShieldUpkeepPerSecondOfTotalCapacity)*float(ShieldLocalCapacityPerBlock)) + "]")
	print ("[Shield recharge per block][" + ShieldLocalRechargePerBlock + "]")
	print ("[Shield power consumption per block when resting][" + str(float(ShieldLocalPowerConsumptionPerRechargePerSecondResting)*float(ShieldLocalRechargePerBlock)) + "]")
	print ("[Shield power consumption per block when charging][" + str(float(ShieldLocalPowerConsumptionPerRechargePerSecondCharging)*float(ShieldLocalRechargePerBlock)) + "]")
	print ("")
	print ("[Kinetic][" + ShieldEffectKinetic + "]")
	print ("[Heat][" + ShieldEffectHeat + "]")
	print ("[EM][" + ShieldEffectEM + "]")
	print ("```")
	return
	
def GetThrustersConfig(Tree, Xpath):
	Links = Tree.find(Xpath + "ReactorPowerPowerConsumptionPerBlockResting")
	ReactorPowerPowerConsumptionPerBlockResting = Links.text
	Links = Tree.find(Xpath + "ReactorPowerPowerConsumptionPerBlockInUse")
	ReactorPowerPowerConsumptionPerBlockInUse = Links.text
	Links = Tree.iterfind(Xpath + "MulTotalThrust")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			MulTotalThrust = Iterations.text
	Links = Tree.iterfind(Xpath + "PowTotalThrust")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			PowTotalThrust = Iterations.text
	'''Links = Tree.iterfind(Xpath + "UnitCalcMult")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			UnitCalcMult = Iterations.text'''
	print ("**THRUSTER**")
	print ("```md")
	print ("[ReactorPowerPowerConsumptionPerBlockResting][" + ReactorPowerPowerConsumptionPerBlockResting + "]")
	print ("[ReactorPowerPowerConsumptionPerBlockInUse][" + ReactorPowerPowerConsumptionPerBlockInUse + "]")
	print ("Formula is : (Nbr^(" + PowTotalThrust + ") x " + MulTotalThrust + ")")
	print ("```")
	return


def GetStats(Tree, Xpath, BaseValue):
	Links = Tree.find(Xpath)
	if (Links.attrib['style'] == "nerf"):
		Value = float(BaseValue) / float(Links.attrib['value'])
	elif (Links.attrib['style'] == "buff"):
		Value = float(BaseValue) * ( 1 + float(Links.attrib['value']))
	elif (Links.attrib['style'] == "set"):
		Value = Links.attrib['value']
	else:
		Value = BaseValue
	return Value

def GetMissileCapacity(Tree, Xpath):
	# Stats part
	Links = Tree.find(Xpath + "BasicMissileCapacity")
	BasicMissileCapacity = Links.text
	Links = Tree.find(Xpath + "ReactorPowerConsumptionResting")
	ReactorPowerConsumptionResting = Links.text
	Links = Tree.find(Xpath + "ReactorPowerConsumptionCharging")
	ReactorPowerConsumptionCharging = Links.text
	Links = Tree.find(Xpath + "MissileCapacityPerSec")
	MissileCapacityPerSec = Links.text
	Links = Tree.find(Xpath + "MissileCapacityReloadMode")
	MissileCapacityReloadMode = Links.text
	print ("**MISSILE CAPACITY**")
	print ("```md")
	print ("[ReactorPowerConsumptionResting][" + ReactorPowerConsumptionResting + "]")
	print ("[ReactorPowerConsumptionCharging][" + ReactorPowerConsumptionCharging + "]")
	print ("\n[BasicMissileCapacity][" + BasicMissileCapacity + "]")
	print ("[MissileCapacityPerSec][" + MissileCapacityPerSec + "]")
	print ("[MissileCapacityReloadMode][" + MissileCapacityReloadMode + "]")
	if (MissileCapacityReloadMode == "ALL"):
		Links = Tree.find(Xpath + "MissileCapacityReloadConstant")
		MissileCapacityReloadConstant = Links.text
		Links = Tree.find(Xpath + "MissileCapacityReloadResetOnFireManual")
		MissileCapacityReloadResetOnFireManual = Links.text
		Links = Tree.find(Xpath + "MissileCapacityReloadResetOnFireAI")
		MissileCapacityReloadResetOnFireAI = Links.text
		print ("[MissileCapacityReloadConstant][" + MissileCapacityReloadConstant + "]")
		print ("[MissileCapacityReloadResetOnFireManual][" + MissileCapacityReloadResetOnFireManual + "]")
		print ("[MissileCapacityReloadResetOnFireAI][" + MissileCapacityReloadResetOnFireAI + "]")
	# Formula part
	Links = Tree.find(Xpath + "MissileCapacityCalcStyle")
	MissileCapacityCalcStyle = Links.text
	print ("\n[MissileCapacityCalcStyle][" + MissileCapacityCalcStyle + "]")
	if (MissileCapacityCalcStyle == "LINEAR"):
		Links = Tree.find(Xpath + "MissileCapacityPerBlock")
		MissileCapacityPerBlock = Links.text
		print ("[MissileCapacityPerBlock][" + MissileCapacityPerBlock + "]")
	elif (MissileCapacityCalcStyle == "EXP"):
		Links = Tree.find(Xpath + "MissileCapacityExp")
		MissileCapacityExp = Links.text
		print ("[MissileCapacityExp][" + MissileCapacityExp + "]")
		Links = Tree.find(Xpath + "MissileCapacityExpMult")
		MissileCapacityExpMult = Links.text
		print ("[MissileCapacityExpMult][" + MissileCapacityExpMult + "]")
	elif (MissileCapacityCalcStyle == "DOUBLE_EXP"):
		Links = Tree.find(Xpath + "MissileCapacityExpMultFirstHalf")
		MissileCapacityExpMultFirstHalf = Links.text
		print ("[MissileCapacityExpMultFirstHalf][" + MissileCapacityExpMultFirstHalf + "]")
		Links = Tree.find(Xpath + "MissileCapacityExpFirstHalf")
		MissileCapacityExpFirstHalf = Links.text
		print ("[MissileCapacityExpFirstHalf][" + MissileCapacityExpFirstHalf + "]")
		Links = Tree.find(Xpath + "MissileCapacityExpThreshold")
		MissileCapacityExpThreshold = Links.text
		print ("[MissileCapacityExpThreshold][" + MissileCapacityExpThreshold + "]")
		Links = Tree.find(Xpath + "MissileCapacityExpMultSecondHalf")
		MissileCapacityExpMultSecondHalf = Links.text
		print ("[MissileCapacityExpMultSecondHalf][" + MissileCapacityExpMultSecondHalf + "]")
		Links = Tree.find(Xpath + "MissileCapacityExpSecondHalf")
		MissileCapacityExpSecondHalf = Links.text
		print ("[MissileCapacityExpSecondHalf][" + MissileCapacityExpSecondHalf + "]")
	elif (MissileCapacityCalcStyle == "LOG"):
		Links = Tree.find(Xpath + "MissileCapacityLogFactor")
		MissileCapacityLogFactor = Links.text
		print ("[MissileCapacityLogFactor][" + MissileCapacityLogFactor + "]")
		Links = Tree.find(Xpath + "MissileCapacityLogOffset")
		MissileCapacityLogOffset = Links.text
		print ("[MissileCapacityLogOffset][" + MissileCapacityLogOffset + "]")
	print ("```\n")
	return

	
def GetBlockBehaviorConfigSystems():
	print ("\n***Systems***")
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	Xpath = ".//General/BasicValues/"
	GetShieldConfig(Tree, Xpath)
	GetArmorConfig(Tree, Xpath)
	GetBasicBlockEffect(Tree, Xpath)
	Xpath = ".//Thruster/BasicValues/"
	GetThrustersConfig(Tree, Xpath)
	Xpath = ".//MissileCapacity/BasicValues/"
	GetMissileCapacity(Tree, Xpath)
	return


if __name__ == "__main__":
	GetBlockBehaviorConfigSystems()