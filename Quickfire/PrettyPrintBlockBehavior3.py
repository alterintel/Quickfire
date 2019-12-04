#Works only in python 3
import xml.etree.ElementTree

global SectorRange
SectorRange = 2000

def GetBlockBehaviorConfigWeapons():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/blockBehaviorConfig.xml")
	WeaponsList = "Cannon", "Missile"
	print("") # Just so we jump a line
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
	print ("[Kinetic][" + str(KineticEffect) + "]")
	print ("[Heat][" + str(HeatEffect) + "]")
	print ("[EM][" + str(EmEffect) + "]")
	print ("[Power consumption when resting][" + str(BasePowerConsumptionResting) + "]")
	print ("[Power consumption when charging][" + str(BasePowerConsumptionCharging) + "]")
	if ("Missile" in Xpath):
		Links = Tree.find(XpathBase + "/MissileHPCalcStyle")
		MissileHPCalcStyle = Links.text
		Links = Tree.find(XpathBase + "/MissileHPMin")
		MissileHPMin = Links.text
		print ("[MissileHPMin][" + str(MissileHPMin) + "]")
		print ("[MissileHPCalcStyle][" + str(MissileHPCalcStyle) + "]")
		if (MissileHPCalcStyle == "LINEAR"):
			Links = Tree.find(XpathBase + "/MissileHPPerDamage")
			MissileHPPerDamage = Links.text
			#print ("[MissileHPPerDamage][" + str(MissileHPPerDamage) + "]")
			print ("MissileHP = MissileDamage * " + str(MissileHPPerDamage))
		if (MissileHPCalcStyle == "EXP"):
			Links = Tree.find(XpathBase + "/MissileHPExp")
			MissileHPExp = Links.text
			Links = Tree.find(XpathBase + "/MissileHPExpMult")
			MissileHPExpMult = Links.text
			print ("[MissileHPExp][" + str(MissileHPExp) + "]")
			print ("[MissileHPExpMult][" + str(MissileHPExpMult) + "]")
		if (MissileHPCalcStyle == "LOG"):
			Links = Tree.find(XpathBase + "/MissileHPLogOffset")
			MissileHPLogOffset = Links.text
			Links = Tree.find(XpathBase + "/MissileHPLogFactor")
			MissileHPLogOffset = Links.text
			print ("[MissileHPLogOffset][" + str(MissileHPLogOffset) + "]")
			print ("[MissileHPLogFactor][" + str(MissileHPLogFactor) + "]")
		Links = Tree.find(XpathBase + "/BombActivationTimeSec")
		BombActivationTimeSec = Links.text
		print ("[BombActivationTimeSec][" + str(BombActivationTimeSec) + "]")
	print ("< Base weapon >")
	if ("Cannon" in Xpath):
		Links = Tree.find(XpathBase + "/ImpactForce")
		BaseImpactForce = Links.text
		Links = Tree.find(XpathBase + "/Aimable")
		BaseAimable = Links.text
		Links = Tree.find(XpathBase + "/AcidFormulaDefault")
		AcidFormulaDefault = Links.text
		print ("[ImpactForce][" + str(BaseImpactForce) + "]")
		print ("[Aimable][" + str(BaseAimable) + "]")
		if (AcidFormulaDefault == "0"):
			print ("[Equalized cone]")
		elif (AcidFormulaDefault == "1"):
			print ("[Cone start wide]")
		elif (AcidFormulaDefault == "2"):
			print ("[Cone end wide]")
		Links = Tree.find(XpathBase + "/DamageChargeMax")
		DamageChargeMax = Links.text
		Links = Tree.find(XpathBase + "/DamageChargeSpeed")
		DamageChargeSpeed = Links.text
		if (float(DamageChargeMax) != 0 and float(DamageChargeSpeed) != 0):
			print ("[DamageChargeMax][" + str(DamageChargeMax) + "]")
			print ("[DamageChargeSpeed][" + str(DamageChargeSpeed) + "]")
	elif ("Missile" in Xpath):
		#Waiting for cleaner configs to have this code
		Links = Tree.find(XpathBase + "/LockOnTimeSec")
		BaseLockOnTimeSec = Links.text
		#print ("[LockOnTimeSec][" + str(LockOnTimeSec) + "]")
		print ("[Mode][Dumbfire]")
		#print ("[Split][1]")
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
		if ("Cannon" in Xpath):
			ImpactForce = GetStats(Tree, XpathCombination + i + "/ImpactForce", BaseImpactForce)
			Aimable = GetStats(Tree, XpathCombination + i + "/Aimable", BaseAimable)
			AcidFormula = GetStats(Tree, XpathCombination + i + "/AcidFormula", AcidFormulaDefault)
			print ("[ImpactForce][" + str(ImpactForce) + "]")
			print ("[Aimable][" + str(Aimable) + "]")
			if (AcidFormula == "0"):
				print ("[Equalized cone]")
			elif (AcidFormula == "1"):
				print ("[Cone start wide]")
			elif (AcidFormula == "2"):
				print ("[Cone end wide]")
			ChargeMax = GetStats(Tree, XpathCombination + i + "/ChargeMax", DamageChargeMax)
			ChargeSpeed = GetStats(Tree, XpathCombination + i + "/ChargeSpeed", DamageChargeSpeed)
			if (float(ChargeMax) != 0 and float(ChargeSpeed) != 0):
				print ("[ChargeMax][" + str(ChargeMax) + "]")
				print ("[ChargeSpeed][" + str(ChargeSpeed) + "]")
		if ("Missile" in Xpath):
			Mode = GetStats(Tree, XpathCombination + i + "/Mode", 0)
			Links = Tree.find(XpathBase + "/LockOnTimeSec")
			LockOnTimeSec = GetStats(Tree, XpathCombination + i + "/Mode", BaseLockOnTimeSec)
			#<!-- Dumb = 0, Heat = 1, TargetChasing = 2, Bomb = 3 -->
			if (Mode == "0"):
				print ("[Mode][Dumbfire]")
			elif (Mode == "1"):
				print ("[Mode][Heatseeker]")
			elif (Mode == "2"):
				print ("[Mode][lock-on]")
				print ("[LockOnTimeSec][" + str(LockOnTimeSec) + "]")
			elif (Mode == "3"):
				print ("[Mode][Bomb]")
			Split = GetStats(Tree, XpathCombination + i + "/Split", 1)
			if (Split != 1):
				print ("[Split][" + str(Split-1) + "]")
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
	elif (Links.attrib['style'] == "set"):
		Value = Links.attrib['value']
	else:
		Value = BaseValue
	return Value

if __name__ == "__main__":
	GetBlockBehaviorConfigWeapons()