def display_inventory(inventory):
  """Prints inventory in a plain form."""
  print("Inventory:")
  for item in inventory.items():
    print(f"{item[1]} {item[0]}")
  print(f"Total number of items: {sum(inventory.values())}")


# NOTE: Past tense of name added_items makes no sense
# Suggestion: new_items or items_to_add
def add_to_inventory(inventory, added_items):
  """Returns inventory after adding items in added_items"""
  for thing in added_items:
    if thing in inventory:
      inventory[thing] += 1
    else:
      inventory.update({thing: 1})
  return inventory


# TODO: Refactor?
# Very long, but logical and readable.
# Breaking it into smaller functions seems counterintuitive,
# as none of its parts are reuseable.
def print_table(inventory, order=''):
  """Prints inventory in a neat form.
  Optional keyword arguments:
  order='count,desc' to sort in descending order
  order='count,asc' to sort in ascending order"""

  header1 = 'count'
  header2 = 'item name'
  side_padding = 1
  center_padding = 4
  net_width1 = max(max(len(str(count)) for count in inventory.values()), len(header1))
  net_width2 = max(max(len(item_name) for item_name in inventory.keys()), len(header2))
  total_width = net_width1 + net_width2 + side_padding*2 + center_padding

  # format and sort inventory
  inventory = [(item[1], item[0]) for item in inventory.items()]
  if order == 'count,asc':
    inventory = sorted(inventory)
  elif order == 'count,desc':
    inventory = sorted(inventory, reverse=True)

  # print headers
  print("Inventory:")
  print(f"{' ' * side_padding}"
        f"{' ' * (net_width1-len(header1))}"
        f"{header1}"
        f"{' ' * center_padding}"
        f"{' ' * (net_width2-len(header2))}"
        f"{header2}"
        f"{' ' * side_padding}")
  print('-' * total_width)

  # print items
  for item in inventory:
      print(f"{' ' * side_padding}"
            f"{' ' * (net_width1-len(str(item[0])))}"
            f"{item[0]}"
            f"{' ' * center_padding}"
            f"{' ' * (net_width2-len(item[1]))}"
            f"{item[1]}"
            f"{' ' * side_padding}")

  # print footers
  print('-' * total_width)
  print(f"Total number of items: {sum(item[0] for item in inventory)}")


# NOTE: Function name doesn't describe full functionality
# Suggestion: add_to_inventory_from_file()
def import_inventory(inventory, filename='import_inventory.csv'):
  """Returns inventory after adding items in CSV file."""
  with open(filename) as file:
    data = file.read()
    items = data.split(',')
    return add_to_inventory(inventory, items)


def export_inventory(inventory, filename='export_inventory.csv'):
  """Saves value instances of keys into target file as CSV.
  May be imported back using import_inventory()"""
  with open(filename, 'w') as file:
    stuff = []
    for item in inventory.items():
      for i in range(item[1]):
        stuff.append(item[0])
    file.write(','.join(stuff))
