
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

    def __init__(self, name="empty", property_type="attribute", description="", requires_attunement=False, weapon_bonus=0, ac_bonus=0, spell_bonus=0, cantrips=0, spell_levels_once_a_day=0, Spell_levels_3_times_a_day=0, Spell_levels_infinte_times_a_day=0, damage_d6=0, damage_type=0):
        self.name = name.replace('"', '')
        self.property_type = property_type.replace('"', '')
        self.description = description.replace('"', '')
        self.requires_attunement = bool(requires_attunement)
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

    def __init__(self, name="new item", rarity_name="common", is_artifact=False, is_consumable=False, property_names=[], special_materials=[]):
        self.name = name.replace('"', '')
        self.rarity_name = rarity_name.replace('"', '')
        self.is_artifact = bool(is_artifact)
        self.is_consumable = bool(is_consumable)
        self.property_names = property_names
        self.special_materials = special_materials

        self.properties = {}
        self.rarity_stats = None

    def to_string(self):
        s = '"' + self.name + '",' + \
            '"' + str(self.rarity_name) + '",' + str(self.is_artifact) + \
            "," + str(self.is_consumable)

        s += ",["+",".join(self.property_names)+"]"
        s += ",["+",".join(self.special_materials)+"]"
        s += "\n"
        return s

    def load_properties(self, magic_item_properties):
        self.properties = {}
        for pn in self.property_names:
            self.properties[pn] = magic_item_properties[pn]

    def load_rarity_stats(self, rarities):
        self.rarity_stats = rarities(self.rarity_name)

    def property_count(self, property_type):
        i = 0
        for ip in self.properties:
            if ip.property_type == property_type:
                i += 1
        return i

    def remaining_property_slots(self, property_type):
        cur = self.property_count(property_type)
        caps = {"attribute": self.rarity_stats.attributes, "minor": self.rarity_stats.minor_properties, "major": self.rarity_stats.major_properties, "bonus": self.rarity_stats.max_bonus_properties
                }
        cap = caps[property_type]
        return cap - cur


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

        self.load_rarities()
        self.load_magic_item_properties()
        self.load_magic_items()

    def load_rarities(self, filepath=".\\data\\rarities.dat"):
        self.rarities = {}
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            r = rarity(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])
            self.rarities[r.name] = r

        f.close()

    def load_magic_item_properties(self, filepath=".\\data\\magic_item_properties.dat"):
        self.magic_item_properties = {}
        f = open(filepath, "r")

        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            mp = magic_item_property(
                l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11])
            self.magic_item_properties[mp.name] = mp
        f.close()

    def string_to_list(self, x):
        lst = list(x.strip("[]").split(","))
        return [] if lst[0] == '' else lst

    def load_magic_items(self, filepath=".\\data\\magic_items.dat"):
        self.magic_items = {}
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            property_names = self.string_to_list(l[4])
            special_materials = self.string_to_list(l[5])
            mi = magic_item(l[0], l[1], l[2], l[3],
                            property_names, special_materials)
            self.magic_items[mi.name] = mi
        f.close()

    def new_item(self):
        self.current_item = magic_item

    def save_item(self, filepath=".\\data\\magic_items.dat"):
        f = open(filepath, "a")
        f.write(self.current_item().to_string())
        f.close()
        return 0

    def load_item(self, magic_item_name="new item"):
        if magic_item_name in self.magic_items.keys():
            self.current_item = self.magic_items[magic_item_name]

    def set_rarity_of_item(self, rarity_id=0):
        self.current_item().rarity = rarity_id

    def add_property_to_item(self, property_name="none"):
        #! Needs validation step to see if already at max for property type
        if property_name in self.magic_item_properties.keys():
            self.current_item.property_names.append(property_name)
            self.current_item.properties.append(
                self.magic_item_properties[property_name])

    def remove_property_from_item(self, property_name="none"):
        if property_name in self.current_item().property_names:
            self.current_item().property_names.remove(property_name)
