
import csv
from os import path

property_types = {1: 'attribute', 2: 'minor benefit',
                  3: 'major benefit', 4: 'minor detriment', 5: 'major detriment'}

rarities = {1: 'common', 2: 'uncommon',
            3: 'rare', 4: 'very rare', 5: 'legendary'}
max_attributes = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
max_minor_properties = {1: 0, 2: 1, 3: 2, 4: 2, 5: 3}
max_major_properties = {1: 0, 2: 0, 3: 0, 4: 1, 5: 2}
max_minor_detriments = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
max_major_detriments = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2}
max_plus = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
max_exotic_materials = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
max_spell_lvl = {1: 1, 2: 3, 3: 6, 4: 8, 5: 9}


class MagicItem:

    def __init__(self):
        self.name = ''
        self.description = ''
        self.magic_properties = {}
        self.rarity = 1
        self.is_consumable = 0
        self.is_artifact = 0
        self.exotic_materials = {}


class MagicProperty:

    def __init__(self, property_type=1, name='', description='', requires_attunement='', armour=0, ring=0, rod_staff_wand=0, weapon=0, wonderous=0, plus_attack=0, plus_ac=0, plus_spell=0
                 ):
        self.property_type = int(property_type)
        self.name = str(name)
        self.description = str(description)
        self.requires_attunement = int(requires_attunement)
        self.armour = int(armour)
        self.ring = int(ring)
        self.rod_staff_wand = int(rod_staff_wand)
        self.weapon = int(weapon)
        self.wonderous = int(wonderous)
        self.plus_attack = int(plus_attack)
        self.plus_ac = int(plus_ac)
        self.plus_spell = int(plus_spell)


class lab():

    def __init__(self):
        self.magic_properties = {}

    def load_magic_properties(self):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_item_properties.csv")
        f = open(filepath, "r", encoding="utf8")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            mp = MagicProperty(property_type=l[0], name=l[1], description=l[2], requires_attunement=l[3], armour=l[4],
                               ring=l[5], rod_staff_wand=l[6], weapon=l[7], wonderous=l[8], plus_attack=l[9], plus_ac=l[10], plus_spell=l[11])

            self.magic_properties[mp.name] = mp
        f.close()


if __name__ == '__main__':
    l = lab()
    l.load_magic_properties()
