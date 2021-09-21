
eldrict_property_levels = {1: "Attribute", 2: "Minor", 3: "Major"}
magic_item_rarities = {1: "Common", 2: "Uncommon",
                       3: "Rare", 4: "Very Rare", 5: "Legendary"}


class magicItem:
    def __init__(self, name="new item", description="", eldrict_properties=[], rarity="common", is_artifact=False, is_consumable=False, eldrict_materials=[]):
        self.name = name
        self.description = description
        self.eldrict_properties = eldrict_properties
        self.rarity = rarity
        self.is_artifact = is_artifact
        self.is_consumable = is_consumable

        self.eldrict_materials = eldrict_materials

    def get_properties(self):
        l = self.eldrict_properties
        for material in self.eldrict_materials())
            if material.eldrict_property is not None:
                l.append(material.eldrict_property)
        return l

class eldrictProperty:

    def __init__(self, name = "new property", description = "", property_level = 1, positive_property = True, req_attunement = False, weapon_plus = 0, armour_plus = 0, spell_plus = 0

                 ):
        self.name=name
        self.description=description
        self.property_level=property_level
        self.positive_property=positive_property

        self.req_attunement=req_attunement
        self.weapon_plus=weapon_plus
        self.armour_plus=armour_plus
        self.spell_plus=spell_plus


class eldrictMaterial:

    def __init__(self, name = "new material", description = "", eldrict_property = eldrictProperty()):
        self.name=name
        self.description=description
        self.eldrict_property=eldrict_property
