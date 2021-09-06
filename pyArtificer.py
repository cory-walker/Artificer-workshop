
from typing import Mapping


class rarity:
    def __init__(self, id, name, attributes, minor_properties, major_properties, max_bonus_properties, max_spell_level, max_plus):
        self.id = int(id)
        self.name = name.replace('"', '')
        self.attributes = int(attributes)
        self.minor_properties = int(minor_properties)
        self.major_properties = int(major_properties)
        self.max_bonus_properties = int(max_bonus_properties)
        self.max_spell_level = int(max_spell_level)
        self.max_plus = int(max_plus)


class magic_item_property:

    def __init__(self, name="empty", property_type="attribute", description="", weapon_bonus=0, ac_bonus=0, spell_bonus=0, cantrips=0, spell_levels_once_a_day=0, Spell_levels_3_times_a_day=0, Spell_levels_infinte_times_a_day=0, damage_d6=0, damage_type=0):
        self.name = name.replace('"', '')
        self.property_type = property_type.replace('"', '')
        self.description = description.replace('"', '')
        self.weapon_bonus = int(weapon_bonus)
        self.ac_bonus = int(ac_bonus)
        self.spell_bonus = int(spell_bonus)
        self.cantrips = int(cantrips)
        self.spell_levels_once_a_day = int(spell_levels_once_a_day)
        self.spell_levels_3_times_a_day = int(Spell_levels_3_times_a_day)
        self.spell_levels_infinite_times_a_day = int(
            Spell_levels_infinte_times_a_day)
        self.damage_d6 = int(damage_d6)
        self.damage_type = int(damage_type)


class magic_item:

    def __init__(self, name="new item", rarity=0, is_artifact=False, is_consumable=False, property_names=[]):
        self.name = name
        self.rarity = rarity
        self.is_artifact = is_artifact
        self.is_consumable = is_consumable
        self.property_names = property_names

    def rarity_str(self):
        return self.rarities[self.rarity].name


class special_material:

    def __init__(self, name="", minor_property_name="", minor_detriment_name=""):
        self.name = name
        self.minor_property_name = minor_property_name
        self.minor_detriment_name = minor_detriment_name


class workbench:

    def __init__(self):
        self.rarities = {}
        self.magic_item_properties = {}
        self.magic_items = {}
        self.special_materials = {}
        self.current_item = None

        self.load_rarities(".\\data\\rarities.dat")
        self.load_magic_item_properties(".\\data\\magic_item_properties.dat")

    def load_rarities(self, filepath):
        self.rarities = {}
        f = open(filepath, "r")
        for l in f.readlines()[1:]:
            spl = l.split(",")
            r = rarity(spl[0], spl[1], spl[2], spl[3],
                       spl[4], spl[5], spl[6], spl[7])
            self.rarities[r.name] = r
        f.close()

    def load_magic_item_properties(self, filepath):
        self.magic_item_properties = {}
        f = open(filepath, "r")
        for l in f.readlines()[1:]:
            spl = l.split(",")
            mp = magic_item_property(
                spl[0], spl[1], spl[2], spl[3], spl[4], spl[5], spl[6], spl[7], spl[8], spl[9], spl[10], spl[11])
            self.magic_item_properties[mp.name] = mp
        f.close()

    def new_item(self):
        self.current_item = magic_item


if __name__ == "__main__":
    wb = workbench()
    i = 1
