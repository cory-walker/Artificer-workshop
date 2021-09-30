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

    #! incomplete
    def to_csv_string(self):
        s = '"' + self.name + '",' + self.level + ',"' + self.description + '",'


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


if __name__ == "__main__":
    print("no syntax errors")
    al = ArcaneLab()
    al.load_magic_properties()
