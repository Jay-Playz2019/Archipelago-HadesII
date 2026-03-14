from typing import Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from .Locations import setup_location_table_with_settings, location_table_prophecies

class ItemData(NamedTuple):
    code: Optional[int]
    item_classification: ItemClassification
    event: bool = False
    
# Sorry for the abomination of uppercase and underscore here, but I figured it was more 
# readable than `HadesIIItem`
class Hades_II_Item(Item):
    game = "Hades II"

    def __init__(self, name: str, player: int):
        item_data = item_table[name]
        super().__init__(name, item_data.item_classification, item_data.code, player)

hades_ii_base_item_id = 1

fears_base_item_id = hades_ii_base_item_id
item_table_fears: Dict[str, ItemData] = {
    "Item1": ItemData(hades_ii_base_item_id+1, ItemClassification.progression),
    "Item2": ItemData(hades_ii_base_item_id+2, ItemClassification.progression)
}

filler_base_item_id = fears_base_item_id + 2
item_table_filler: Dict[str, ItemData] = {
    "filler1": ItemData(filler_base_item_id+1, ItemClassification.filler),
    "filler2": ItemData(filler_base_item_id+2, ItemClassification.filler)
}

keepsakes_base_item_id  = filler_base_item_id + 2
item_table_keepsakes: Dict[str, ItemData] = {
    "Hecate Keepsake": ItemData(keepsakes_base_item_id + 1, ItemClassification.progression),
    "Odysseus Keepsake": ItemData(keepsakes_base_item_id + 2, ItemClassification.progression),
    "Schelemeus Keepsake": ItemData(keepsakes_base_item_id + 3, ItemClassification.progression),
    "Dora Keepsake": ItemData(keepsakes_base_item_id + 4, ItemClassification.progression),
    "Nemesis Keepsake": ItemData(keepsakes_base_item_id + 5, ItemClassification.progression),
    "Moros Keepsake": ItemData(keepsakes_base_item_id + 6, ItemClassification.progression),
    "Eris Keepsake": ItemData(keepsakes_base_item_id + 7, ItemClassification.progression),
    "Charon Keepsake": ItemData(keepsakes_base_item_id + 8, ItemClassification.progression),
    "Hermes Keepsake": ItemData(keepsakes_base_item_id + 9, ItemClassification.progression),
    "Artemis Keepsake": ItemData(keepsakes_base_item_id + 10, ItemClassification.progression),
    "Selene Keepsake": ItemData(keepsakes_base_item_id + 11, ItemClassification.progression),

    "Zeus Keepsake": ItemData(keepsakes_base_item_id + 12, ItemClassification.progression),
    "Hera Keepsake": ItemData(keepsakes_base_item_id + 13, ItemClassification.progression),
    "Poseidon Keepsake": ItemData(keepsakes_base_item_id + 14, ItemClassification.progression),
    "Demeter Keepsake": ItemData(keepsakes_base_item_id + 15, ItemClassification.progression),
    "Apollo Keepsake": ItemData(keepsakes_base_item_id + 16, ItemClassification.progression),
    "Aphrodite Keepsake": ItemData(keepsakes_base_item_id + 17, ItemClassification.progression),
    "Hephaestus Keepsake": ItemData(keepsakes_base_item_id + 18, ItemClassification.progression),
    "Hestia Keepsake": ItemData(keepsakes_base_item_id + 19, ItemClassification.progression),
    "Ares Keepsake": ItemData(keepsakes_base_item_id + 20, ItemClassification.progression),
    "Athena Keepsake": ItemData(keepsakes_base_item_id + 21, ItemClassification.progression),
    "Dionysus Keepsake": ItemData(keepsakes_base_item_id + 22, ItemClassification.progression),

    "Arachne Keepsake": ItemData(keepsakes_base_item_id + 23, ItemClassification.progression),
    "Narcissus Keepsake": ItemData(keepsakes_base_item_id + 24, ItemClassification.progression),
    "Echo Keepsake": ItemData(keepsakes_base_item_id + 25, ItemClassification.progression),
    "Heracles Keepsake": ItemData(keepsakes_base_item_id + 26, ItemClassification.progression),
    "Medea Keepsake": ItemData(keepsakes_base_item_id + 27, ItemClassification.progression),
    "Circe Keepsake": ItemData(keepsakes_base_item_id + 28, ItemClassification.progression),
    "Icarus Keepsake": ItemData(keepsakes_base_item_id + 29, ItemClassification.progression),

    "Hades/Persephone Keepsake": ItemData(keepsakes_base_item_id + 30, ItemClassification.progression),
    "Zagreus Keepsake": ItemData(keepsakes_base_item_id + 31, ItemClassification.progression),
    "Chronos Keepsake": ItemData(keepsakes_base_item_id + 32, ItemClassification.progression),

    "Chaos Keepsake": ItemData(keepsakes_base_item_id + 33, ItemClassification.progression),
}

weapons_base_item_id = keepsakes_base_item_id + 33
item_table_weapons: Dict[str, ItemData] = {
    "Staff Weapon Unlock Item": ItemData(weapons_base_item_id+1, ItemClassification.progression),
    "Daggers Weapon Unlock Item": ItemData(weapons_base_item_id+2, ItemClassification.progression),
    "Torches Weapon Unlock Item": ItemData(weapons_base_item_id+3, ItemClassification.progression),
    "Axe Weapon Unlock Item": ItemData(weapons_base_item_id+4, ItemClassification.progression),
    "Skull Weapon Unlock Item": ItemData(weapons_base_item_id+5, ItemClassification.progression),
    "Coat Weapon Unlock Item": ItemData(weapons_base_item_id+6, ItemClassification.progression)
}

tools_base_item_id = weapons_base_item_id +6
item_table_tools: Dict[str, ItemData] = {
    "Crescent Pickaxe Tool Unlock Item": ItemData(tools_base_item_id+1, ItemClassification.progression),
    "Crescent Pickaxe Tool Unlock Item": ItemData(tools_base_item_id+1, ItemClassification.progression),
    "Crescent Pickaxe Tool Unlock Item": ItemData(tools_base_item_id+1, ItemClassification.progression),
    "Crescent Pickaxe Tool Unlock Item": ItemData(tools_base_item_id+1, ItemClassification.progression)

}

item_table_aspects: Dict[str, ItemData] = {
    "X Weapon Y Aspect Unlock Item": ItemData(hades_ii_base_item_id+12, ItemClassification.progression)
}

item_table_traps: Dict[str, ItemData] = {
    "trap1": ItemData(hades_ii_base_item_id+13, ItemClassification.trap)
}

item_table_helpers: Dict[str, ItemData] = {
    "helper1": ItemData(hades_ii_base_item_id+14, ItemClassification.progression | ItemClassification.useful)
}

item_table_prophecies_completion = {
    
}

item_table = {
    **item_table_fears,
    **item_table_prophecies_completion,
    **item_table_filler,
    **item_table_keepsakes,
    **item_table_weapons,
    **item_table_tools,
    **item_table_aspects,
    **item_table_traps,
    **item_table_helpers,
}

group_fears = {"fears": item_table_fears.keys()}
group_fillers = {"fillers": item_table_filler.keys()}
group_weapons = {"weapons": item_table_weapons.keys()}
group_tools = {"tools": item_table_tools.keys()}
group_aspects = {"aspects": item_table_aspects.keys()}
group_keepsakes = {"keepsakes": item_table_keepsakes.keys()}

item_name_groups = {
    **group_fears,
    **group_fillers,
    **group_tools,
    **group_weapons,
    **group_aspects,
    **group_keepsakes,
}

def create_items(self) -> None:
    local_location_table = setup_location_table_with_settings(self.options).copy()
    pool = []
    # TODO: Fear
    
    # Keepsakes
    if self.options.keepsakesanity:
        pool.extend(self.create_item(name) for name in item_table_keepsakes)
    
    # Weapons
    if self.options.weaponsanity:
        for name in item_table_weapons:
            if self.should_ignore_weapon(name):
                continue
            item = Hades_II_Item(name, self.player)
            pool.append(item)
            
    # Aspects
    if self.options.aspectsanity:
        for name in item_table_aspects:
            item = Hades_II_Item(name, self.player)
            pool.append(item)
            
    # Tools
    if self.options.toolsanity:
        pool.extend(self.create_item(name) for name in item_table_tools)

    # Prophecies
    if self.options.fatesanity:
        pool.extend(self.create_item(name) for name in item_table_prophecies_completion)
            
    # Handle fillers and traps
    handle_fillers(self, pool, local_location_table)

    # Place in boss event psuedo-items
    place_boss_events(self.world, self.player)
        
    # Add items to pool
    self.multiworld.itempool += pool

# General use function
def create_item(self, name: str) -> Item:
    return Hades_II_Item(name, self.player)

# Places boss event pseudo-items at each location
def place_boss_events(world, player) -> None:
    bosses = [
        "Hecate Victory",
        "Scylla Victory",
        "Cerberus Victory",
        "Chronos Victory",
        "Polyphemus Victory",
        "Eris Victory",
        "Prometheus Victory",
        "Typhon Victory",
    ]

    for boss in bosses:
        location = world.get_location(boss, player)
        item = world.create_event(boss)
        location.place_locked_item(item)

# Calculates percentages of filler materials and traps    
def handle_fillers(self, pool, local_location_table):
    total_fillers_needed = len(local_location_table) - len(pool) - len(location_table_prophecies) 
    
    # Define the percentages in the pool based off options
    # ? Add F. Fabric to speed things up for the player?
    percentages = {
        "ash": self.options.ash_pack_percentage,
        "bones": self.options.bones_pack_percentage,
        "psyche": self.options.psyche_pack_percentage,
        "nectar": self.options.nectar_pack_percentage,
        "ambrosia": self.options.ambrosia_pack_percentage,
        "nightmare": self.options.nightmare_pack_percentage,
        "helpers": self.options.filler_helper_percentage,
        "traps": self.options.filler_trap_percentage,
    }

    total_percentage = sum(percentages.values())

    if total_percentage == 0:
        percentages["bones"] = 100
        total_percentage = 100
        
    correction = 100/total_percentage
    
    # Calculate the needed amounts
    counts = {
        name: int(total_fillers_needed * pct * correction / 100)
        for name, pct in percentages.items()
    }

    # Populate the rest with bones for remainder safety
    counts["bones"] += total_fillers_needed - sum(counts.values())
    
    # For 100% safety to make sure negative numbers don't happen
    counts["bones"] = max(counts["bones"], 0)
    
    # Helpers
    health_helpers = int(counts["helpers"] * self.options.max_health_helper_percentage / 100)
    money_helpers = counts["helpers"] - health_helpers

    # Populate the pool with fillers
    items = {
        "Ash": counts["ash"],
        "Bones": counts["bones"],
        "Psyche": counts["psyche"],
        "Nectar": counts["nectar"],
        "Ambrosia": counts["ambrosia"],
        "Nightmare": counts["nightmare"],
        "Max Health Helper": health_helpers,
        "Initial Money Helper": money_helpers,
    }

    for name, count in items.items():
        pool.extend(self.create_item(name) for _ in range(count))
            
    # Fill traps
    trap_pool = list(item_table_traps.keys())
    for i in range(counts["traps"]):
        item_name = trap_pool[i % len(trap_pool)]
        pool.append(Hades_II_Item(item_name, self.player))