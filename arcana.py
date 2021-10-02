import csv
from os import path

magic_property_levels = {1: "attribute",
                         2: "minor", 3: "major", 4: "detriment"}
rarities = {1: "common", 2: "uncommon",
            3: "rare", 4: "very rare", 5: "kegendary"}

damage_types = {1: "slashing", 2: "piercing", 3: "bludgeoning", 4: "poison", 5: "acid", 6: "fire",
                7: "cold", 8: "radiant", 9: "necrotic", 10: "lightning", 11: "thunder", 12: "force", 13: "psychic"}


class MagicMaterial:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.magic_properties = []


class MagicProperty:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.description = ""
        self.req_attunement = False
        self.bonuses = {}
        self.cantrips = 0
        self.spell_lvl_1_a_day = 0
        self.spell_lvl_3_a_day = 0
        self.spell_lvl_inf_a_day = 0
        self.dmg_d6 = 0
        self.dmg_type = 0

    def has_bonus(self, bonus_type):
        if bonus_type in self.bonuses.keys():
            return True
        return False

    def to_csv_string(self):
        s = '"' + self.name + '",' + str(self.level) + ',"' + self.description + '",' + str(self.req_attunement) + ',' + str(self.has_bonus('weapon')) + ',' + str(self.has_bonus('ac')) + "," + str(self.has_bonus(
            'spell')) + ',' + str(self.cantrips) + ',' + str(self.spell_lvl_1_a_day) + ',' + str(self.spell_lvl_3_a_day) + ',' + str(self.spell_lvl_inf_a_day) + ',' + str(self.dmg_d6) + ',' + str(self.dmg_type)
        return s


class MagicItemFactory():
    def list_to_magic_item(lst):
        '''"item name","description","rarity name","is artifact","is consumable","property names","special materials"'''
        mi = MagicItem()
        mi.name = str(lst[0])
        mi.description = str(lst[1])
        mi.rarity = int(lst[2])
        mi.is_artifact = bool(lst[3])
        mi.is_consumable = bool(lst[4])
        for p in lst[5].split(","):
            mi.magic_properties.append(str(p))
        for p in lst[6].split(","):
            mi.magic_materials.append(str(p))
        return mi


class MagicItem:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.rarity = 1
        self.is_consumable = False
        self.is_artifact = False
        self.magic_properties = []
        self.magic_materials = []


class MagicItemPropertyFactory:
    def list_to_magic_item_property(lst):
        mi = MagicProperty()
        mi.name = lst[0]
        mi.level = lst[1]
        mi.description = lst[2]
        mi.req_attunement = bool(lst[3])
        if int(lst[4]) > 0:
            mi.bonuses["weapon"] = int(lst[4])
        if int(lst[5]) > 0:
            mi.bonuses["ac"] = int(lst[5])
        if int(lst[6]) > 0:
            mi.bonuses["spell"] = int(lst[6])
        mi.cantrips = int(lst[7])
        mi.spell_lvl_1_a_day = int(lst[8])
        mi.spell_lvl_3_a_day = int(lst[9])
        mi.spell_lvl_inf_a_day = int(lst[10])
        mi.dmg_d6 = int(lst[11])
        mi.dmg_type = int(lst[12])
        return mi


class ArcaneLab:
    def __init__(self):
        self.current_item = None
        self.magic_properties = {}
        self.magic_materials = {}
        self.magic_items = {}

    def load_magic_properties(self):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_item_properties.csv")
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        mfact = MagicItemPropertyFactory
        for l in reader:
            mp = mfact.list_to_magic_item_property(l)
            self.magic_properties[mp.name] = mp
        f.close()

    def load_magic_items(self):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_items.csv")
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        mfact = MagicItemFactory
        for l in reader:
            mi = mfact.list_to_magic_item(l)
            self.magic_items[mi.name] = mi
        f.close()

    def fetch_magic_properties(self, magic_item_name):
        return self.magic_items[magic_item_name].magic_properties

    def magicItemBonus(self, magic_item_name, bonus_type):
        bon = 0
        props = self.fetch_magic_properties(magic_item_name)
        for p in props:
            if self.magic_properties[p].has_bonus(bonus_type):
                bon += self.magic_properties[p].bonuses[bonus_type]
        return bon

    def magicItemDamage(self, magic_item_name, damage_type):
        d6 = 0
        props = self.fetch_magic_properties(magic_item_name)
        for p in props:
            if self.magic_properties[p].dmg_type == damage_type:
                d6 += self.magic_properties[p].dmg_d6

    def magicItemSpellsLevels(self, magic_item_name, spell_times_a_day):
        spell_levels = 0
        props = self.fetch_magic_properties(magic_item_name)
        for p in props:
            if spell_times_a_day == 1:
                spell_levels += self.magic_properties[p].spell_lvl_1_a_day
            elif spell_times_a_day == 3:
                spell_levels += self.magic_properties[p].spell_lvl_3_a_day
            elif spell_times_a_day == 99:
                spell_levels += self.magic_properties[p].spell_lvl_inf_a_day
        return spell_levels


'''self.spell_lvl_1_a_day = 0
        self.spell_lvl_3_a_day = 0
        self.spell_lvl_inf_a_day = 0
        '''


if __name__ == "__main__":
    print("no syntax errors")
    al = ArcaneLab()
    al.load_magic_properties()
    print(al.magic_properties['Easily lost'].to_csv_string())
    al.load_magic_items()
    print("loading complete")
    print(al.magicItemBonus("new item1", "weapon"))
