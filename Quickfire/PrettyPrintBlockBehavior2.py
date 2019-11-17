#Works only in python 3
import xml.etree.ElementTree

global SectorRange
SectorRange = 2000
	
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
	# Part for the effects
	Links = Tree.find(XpathBase + "/EffectConfiguration/Kinetic")
	KineticEffect = Links.text
	Links = Tree.find(XpathBase + "/EffectConfiguration/Heat")
	HeatEffect = Links.text
	Links = Tree.find(XpathBase + "/EffectConfiguration/EM")
	EmEffect = Links.text
	# Part for effect on beam
	Links = Tree.find(XpathBase + "/LatchOn")
	BaseLatchOn = Links.text
	Links = Tree.find(XpathBase + "/Aimable")
	BaseAimable = Links.text
	Links = Tree.find(XpathBase + "/ChargeTime")
	BaseChargeTime = Links.text
	Links = Tree.find(XpathBase + "/DropShieldsOnCharging")
	DropShieldsOnCharging = Links.text
	# Pretty printing base values
	print ("[Kinetic][" + str(KineticEffect) + "]")
	print ("[Heat][" + str(HeatEffect) + "]")
	print ("[EM][" + str(EmEffect) + "]")
	print ("[Power consumption when resting][" + str(BasePowerConsumptionResting) + "]")
	print ("[Power consumption when charging][" + str(BasePowerConsumptionCharging) + "]")
	print ("[Power consumption when firing][" + str(BasePowerConsumptionPerTick) + "]")
	print ("[DropShieldsOnCharging][" + str(DropShieldsOnCharging) + "]")
	print ("< Base weapon >")
	print ("[LatchOn][" + str(BaseLatchOn) + "]")
	print ("[Aimable][" + str(BaseAimable) + "]")
	print ("[ChargeTime][" + str(BaseChargeTime) + "]")
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
		BurstTime = GetStats(Tree, XpathCombination + i + "/BurstTime", BaseBurstTime)
		Cooldown = GetStats(Tree, XpathCombination + i + "/CoolDown", BaseCooldown)
		MinEffectiveValue = GetStats(Tree, XpathCombination + i + "/MinEffectiveValue", BaseMinEffectiveValue)
		MinEffectiveRange = GetStats(Tree, XpathCombination + i + "/MinEffectiveRange", BaseMinEffectiveRange)
		MaxEffectiveValue = GetStats(Tree, XpathCombination + i + "/MaxEffectiveValue", BaseMaxEffectiveValue)
		MaxEffectiveRange = GetStats(Tree, XpathCombination + i + "/MaxEffectiveRange", BaseMaxEffectiveRange)
		LatchOn = GetStats(Tree, XpathCombination + i + "/LatchOn", BaseLatchOn)
		Aimable = GetStats(Tree, XpathCombination + i + "/Aimable", BaseAimable)
		ChargeTime = GetStats(Tree, XpathCombination + i + "/ChargeTime", BaseChargeTime)
		# Pretty printing slave
		print ("< " + i + " slave >")
		print ("[LatchOn][" + str(LatchOn) + "]")
		print ("[Aimable][" + str(Aimable) + "]")
		print ("[ChargeTime][" + str(ChargeTime) + "]")
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
	elif (Links.attrib['style'] == "set"):
		Value = Links.attrib['value']
	else:
		Value = BaseValue
	return Value
	
def GetBlockBehaviorConfigWeapons():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	print ("*Remember that for all weapons the numbers are given for 1 module*")
	print ("**Damage Beam**")
	print ("```md")
	Xpath = ".//DamageBeam"
	GetBeamStats(Tree, Xpath)
	print ("```")
	return
	
if __name__ == "__main__":
	GetBlockBehaviorConfigWeapons()