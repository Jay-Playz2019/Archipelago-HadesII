from worlds.generic.Rules import set_rule, add_rule, add_item_rule

def set_rules(world, player: int, number_items: int, location_table, options) -> None:
    # Set up some logic in areas to avoid having all heats "stack up" as batch in other games.
    total_routine_inspection = int(options.routine_inspection_pact_amount.value)

    # Rule checks
    

        