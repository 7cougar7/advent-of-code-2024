## Part 1 Solution ##
rules = {}
updates = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        trimmed_line = line.strip()
        potentially_split_rule = trimmed_line.split('|')
        # If is a rule:
        if len(potentially_split_rule) == 2:
            try:
                rules[potentially_split_rule[0]].append(potentially_split_rule[1])
            except:
                rules[potentially_split_rule[0]] = [potentially_split_rule[1]]
        elif len(trimmed_line) > 0:
            updates.append(trimmed_line.split(','))

def is_valid_update(update):
    pages_seen = []
    for page in update:
        rule_for_page = rules.get(page)
        if rule_for_page is None:
            pages_seen.append(page)
            continue
        for page_seen in pages_seen:
            if page_seen in rule_for_page:
                return False
        pages_seen.append(page)
    return True

processed_updates = [(update, is_valid_update(update)) for update in updates]
valid_updates = [update[0] for update in processed_updates if update[1]]
middle_values = [int(update[(len(update)//2)]) for update in valid_updates]

print("Day 5, Part 1 Answer: " + str(sum(middle_values)))


## Part 2 Solution ##

def fix_update(update):
    valid_update = []
    for value in update:
        rules_for_current_value = rules.get(value)
        value_inserted = False
        for valid_val in valid_update:
            if rules_for_current_value is None:
                break
            if valid_val in rules_for_current_value:
                valid_update.insert(valid_update.index(valid_val), value)
                value_inserted = True
                break
        if not value_inserted:
            valid_update.append(value)
    return valid_update

invalid_updates = [update[0] for update in processed_updates if not update[1]]
fixed_updates = [fix_update(update) for update in invalid_updates]
fixed_middle_values = [int(update[(len(update)//2)]) for update in fixed_updates]

print("Day 5, Part 2 Answer: " + str(sum(fixed_middle_values)))
