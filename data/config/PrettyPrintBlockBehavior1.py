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
	print ("**SYSTEMS**")
	print ("```md")
	print ("[BasicEffectConfiguration]")
	print ("[Kinetic][" + BasicEffectKinetic + "]")
	print ("[Heat][" + BasicEffectHeat + "]")
	print ("[EM][" + BasicEffectEM + "]")
	print ("```")
	return

def GetArmorConfig(Tree, Xpath):
	Links = Tree.find(Xpath + "ArmorExponentialIncomingExponent")
	ArmorExponentialIncomingExponent = Links.text
	Links = Tree.find(Xpath + "ArmorExponentialArmorValueTotalExponent")
	ArmorExponentialArmorValueTotalExponent = Links.text
	Links = Tree.find(Xpath + "ArmorExponentialIncomingDamageAddedExponent")
	ArmorExponentialIncomingDamageAddedExponent = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/Kinetic")
	ArmorEffectKinetic = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/Heat")
	ArmorEffectHeat = Links.text
	Links = Tree.find(Xpath + "ArmorEffectConfiguration/EM")
	ArmorEffectEM = Links.text
	print ("**ARMOR**")
	print ("```md")
	print ("Armor formula is : (Incoming_Damage^(" + ArmorExponentialIncomingExponent + "))/(SUM_of_Armor_value_in_line_of_shot^(" + ArmorExponentialArmorValueTotalExponent + ") + Incoming_Damage^(" + ArmorExponentialIncomingDamageAddedExponent + "))")
	print ("\n[ArmorEffectConfiguration]")
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
	Links = Tree.iterfind(Xpath + "UnitCalcMult")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			UnitCalcMult = Iterations.text
	print ("**THRUSTER**")
	print ("```md")
	print ("[ReactorPowerPowerConsumptionPerBlockResting][" + ReactorPowerPowerConsumptionPerBlockResting + "]")
	print ("[ReactorPowerPowerConsumptionPerBlockInUse][" + ReactorPowerPowerConsumptionPerBlockInUse + "]")
	print ("Formula is : " + UnitCalcMult + " x (Nbr^(" + PowTotalThrust + ") x " + MulTotalThrust + ")")
	print ("```")
	return
	
def GetBeamStats(Tree, Xpath):
	XpathBase = Xpath + "/BasicValues"
	# Part for the damage
	Links = Tree.iterfind(XpathBase + "/DamagePerHit")
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd iteration where there is no version attribute
		except:
			BaseDamage = Iterations.text
	# Part for the tick rate/Cooldown time/Burst time
	Links = Tree.find(XpathBase + "/TickRate")
	BaseTickRate = Links.text
	Links = Tree.find(XpathBase + "/CoolDown")
	BaseCooldown = Links.text
	Links = Tree.find(XpathBase + "/BurstTime")
	BaseBurstTime = Links.text
	# Part for the power consumption
	Links = Tree.find(XpathBase + "/ReactorPowerConsumptionResting")
	BasePowerConsumptionResting = Links.text
	Links = Tree.find(XpathBase + "/ReactorPowerConsumptionCharging")
	BasePowerConsumptionCharging = Links.text
	Links = Tree.find(XpathBase + "/PowerConsumptionPerTick")
	BasePowerConsumptionPerTick = Links.text
	# Part for the distance
	XpathRange = XpathBase + "/Distance"
	Links = Tree.find(XpathRange)
	BaseRange = Links.text
	# Part for the distance fall off
	Links = Tree.find(XpathBase + "/MinEffectiveValue")
	BaseMinEffectiveValue = Links.text
	Links = Tree.find(XpathBase + "/MinEffectiveRange")
	BaseMinEffectiveRange = Links.text
	Links = Tree.find(XpathBase + "/MaxEffectiveValue")
	BaseMaxEffectiveValue = Links.text
	Links = Tree.find(XpathBase + "/MaxEffectiveRange")
	BaseMaxEffectiveRange = Links.text
	# Pretty printing base values
	print ("< Base weapon >")
	print ("[Power consumption when resting][" + str(BasePowerConsumptionResting) + "]")
	print ("[Power consumption when charging][" + str(BasePowerConsumptionCharging) + "]")
	print ("[Power consumption when firing][" + str(BasePowerConsumptionPerTick) + "]")
	print ("[Damage per tick][" + str(BaseDamage) + "]")
	print ("[Tick rate][" + str(BaseTickRate) + "]")
	print ("[Burst time][" + str(BaseBurstTime) + "]")
	print ("[Cooldown time][" + str(BaseCooldown) + "]")
	DPS = ((float(BaseBurstTime)/float(BaseTickRate))*float(BaseDamage))/float(BaseCooldown)
	print ("[Damage per seconds of][" + str(DPS) + "]")
	BaseMinEffectiveValuePercent = float(BaseMinEffectiveValue) * 100
	BaseMinEffectiveRangeValue = float(BaseMinEffectiveRange) * SectorRange * float(BaseRange)
	BaseMaxEffectiveValuePercent = float(BaseMaxEffectiveValue) * 100
	BaseMaxEffectiveRangeValue = float(BaseMaxEffectiveRange) * SectorRange * float(BaseRange)
	print ("[Range fall-off]\n- " + str(BaseMinEffectiveValuePercent) + "% at " + str(BaseMinEffectiveRangeValue) + "\n- " + str(BaseMaxEffectiveValuePercent) + "% at " + str(BaseMaxEffectiveRangeValue))
	
	XpathCombination = Xpath + "/Combination/"
	ListWeaponCombination = "Cannon", "Missile", "Beam"
	for i in ListWeaponCombination:
		Damage = GetStats(Tree, XpathCombination + i + "/PowerPerHit", BaseDamage)
		Range = GetStats(Tree, XpathCombination + i + "/Distance", BaseRange)
		TickRate = GetStats(Tree, XpathCombination + i + "/HitSpeed", BaseTickRate)
		BurstTime = GetStats(Tree, XpathCombination + i + "/BurstTime", BaseDamage)
		Cooldown = GetStats(Tree, XpathCombination + i + "/CoolDown", BaseDamage)
		MinEffectiveValue = GetStats(Tree, XpathCombination + i + "/MinEffectiveValue", BaseMinEffectiveValue)
		MinEffectiveRange = GetStats(Tree, XpathCombination + i + "/MinEffectiveRange", BaseMinEffectiveRange)
		MaxEffectiveValue = GetStats(Tree, XpathCombination + i + "/MaxEffectiveValue", BaseMaxEffectiveValue)
		MaxEffectiveRange = GetStats(Tree, XpathCombination + i + "/MaxEffectiveRange", BaseMaxEffectiveRange)
		# Pretty printing slave
		print ("< " + i + " slave >")
		print ("[Damage per tick][" + str(Damage) + "]")
		print ("[Tick rate][" + str(TickRate) + "]")
		print ("[Burst time][" + str(BurstTime) + "]")
		print ("[Cooldown time][" + str(Cooldown) + "]")
		DPS = ((float(BurstTime)/float(TickRate))*float(Damage))/float(Cooldown)
		print ("[Damage per seconds of][" + str(DPS) + "]")
		MinEffectiveValuePercent = float(MinEffectiveValue) * 100
		MinEffectiveRangeValue = float(MinEffectiveRange) * SectorRange * float(Range)
		MaxEffectiveValuePercent = float(MaxEffectiveValue) * 100
		MaxEffectiveRangeValue = float(MaxEffectiveRange) * SectorRange * float(Range)
		print ("[Range fall-off]\n- " + str(MinEffectiveValuePercent) + "% at " + str(MinEffectiveRangeValue) + "\n- " + str(MaxEffectiveValuePercent) + "% at " + str(MaxEffectiveRangeValue))

	
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
	
def GetBlockBehaviorConfigSystems():
	print ("***Systems***")
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	Xpath = ".//General/BasicValues/"
	GetShieldConfig(Tree, Xpath)
	GetArmorConfig(Tree, Xpath)
	GetBasicBlockEffect(Tree, Xpath)
	Xpath = ".//Thruster/BasicValues/"
	GetThrustersConfig(Tree, Xpath)
	return

def GetBlockBehaviorConfigWeapons():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	print ("\n*Remember that for all weapons the numbers are given for 1 module*")
	print ("**Damage Beam**")
	print ("```md")
	Xpath = ".//DamageBeam"
	GetBeamStats(Tree, Xpath)
	print ("```")
	return

if __name__ == "__main__":
	GetBlockBehaviorConfigSystems()
	GetBlockBehaviorConfigWeapons()