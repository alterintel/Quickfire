#Works only in python 3
import xml.etree.ElementTree

def GetBlocksConfig():
	Tree = xml.etree.ElementTree.ElementTree()
	Tree.parse("/home/starmade/starmade/StarMade/data/config/BlockConfig.xml")

	# Basic armor
	Xpath = ".//Basic/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	BasicArmor = ">>> Basic armor :\nMass : " + Mass + "\nHitpoints : " + HP + "\nArmorValue : " + Armor
	# Standard armor
	Xpath = ".//Standard/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	StandardArmor = ">>> Standard armor :\nMass : " + Mass + "\nHitpoints : " + HP + "\nArmorValue : " + Armor
	# Advanced armor
	Xpath = ".//Advanced/Grey/Block"
	Mass, HP, Armor = GetArmorBlockValue(Tree, Xpath)
	AdvancedArmor = ">>> Advanced armor :\nMass : " + Mass + "\nHitpoints : " + HP + "\nArmorValue : " + Armor
	
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
	Tree.parse("blockBehaviorConfig.xml")
	Xpath = ".//Cannon/BasicValues/Damage"
	CDamage = GetBaseWeaponDamage(Tree, Xpath)
		
	print (CDamage)
	return
	
def GetBaseWeaponDamage(Tree, Xpath):
	Links = Tree.iterfind(Xpath)
	for Iterations in Links:
		try:
			Iterations.attrib['version'] # will throw an exception for the 2nd exception where there is no version attribute
		except:
			Damage = Iterations.text
		
	return Damage


if __name__ == "__main__":
	GetBlocksConfig()
	#GetBlockBehaviorConfig()
	
	'''
	# Basic armor
	Xpath = ".//Basic/Grey/Block/Mass"
	Links = Tree.find(Xpath)
	BasicArmorMass = Links.text
	Xpath = ".//Basic/Grey/Block/Hitpoints"
	Links = Tree.find(Xpath)
	BasicArmorHp = Links.text
	Xpath = ".//Basic/Grey/Block/ArmorValue"
	Links = Tree.find(Xpath)
	BasicArmorArmorValue = Links.text
	BasicArmor = ">>> Basic armor :\nMass : " + BasicArmorMass + "\nHitpoints : " + BasicArmorHp + "\nArmorValue : " + BasicArmorArmorValue
	print (BasicArmor)
	
	# Standard armor
	Xpath = ".//Standard/Grey/Block/Mass"
	Links = Tree.find(Xpath)
	StandardArmorMass = Links.text
	Xpath = ".//Standard/Grey/Block/Hitpoints"
	Links = Tree.find(Xpath)
	StandardArmorHp = Links.text
	Xpath = ".//Standard/Grey/Block/ArmorValue"
	Links = Tree.find(Xpath)
	StandardArmorArmorValue = Links.text
	StandardArmor = ">>> Standard armor :\nMass : " + StandardArmorMass + "\nHitpoints : " + StandardArmorHp + "\nArmorValue : " + StandardArmorArmorValue
	print (StandardArmor)
	
	# Advanced armor
	Xpath = ".//Advanced/Grey/Block/Mass"
	Links = Tree.find(Xpath)
	AdvancedArmorMass = Links.text
	Xpath = ".//Advanced/Grey/Block/Hitpoints"
	Links = Tree.find(Xpath)
	AdvancedArmorHp = Links.text
	Xpath = ".//Advanced/Grey/Block/ArmorValue"
	Links = Tree.find(Xpath)
	AdvancedArmorArmorValue = Links.text
	AdvancedArmor = ">>> Advanced armor :\nMass : " + AdvancedArmorMass + "\nHitpoints : " + AdvancedArmorHp + "\nArmorValue : " + AdvancedArmorArmorValue
	print (AdvancedArmor)
	'''