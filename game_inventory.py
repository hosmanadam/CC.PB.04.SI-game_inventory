def display_inventory(inventory):
  """Prints inventory in a plain form."""
  print("Inventory:")
  for item in inventory.items():
    print(f"{item[1]} {item[0]}")
  print(f"Total number of items: {sum(inventory.values())}")


def add_to_inventory(inventory, added_items):
  """Returns inventory after adding items in added_items
  BAD NAMING: past tense of added_items makes no sense
  SUGGESTION: new_items or items_to_add"""
  for thing in added_items:
    if thing in inventory:
      inventory[thing] += 1
    else:
      inventory.update({thing: 1})
  return inventory


def print_table(inventory, order=''):
  """Prints inventory in a neat form.
  Optional keyword arguments:
  order='count,desc' to sort in descending order
  order='count,asc' to sort in ascending order"""
  # TODO - refactor?
  # Very long, but logical and readable.
  # Breaking it into smaller functions seems counterintuitive,
  # as none of its parts are reuseable.
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


def import_inventory(inventory, filename='import_inventory.csv'):
  """Returns inventory after adding items in CSV file.
  BAD NAMING: doesn't describe full functionality
  SUGGESTION: add_to_inventory_from_file()"""
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


if __name__ == '__main__':
  def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    print("\n\nINITIAL STATE:\n")
    print_table(inv, 'count,asc')

    inv = add_to_inventory(inv, dragon_loot)
    print("\n\nAFTER ADDING DRAGON LOOT:\n")
    print_table(inv, 'count,asc')

    inv = import_inventory(inv)
    print("\n\nAFTER ADDING IMPORT:\n")
    print_table(inv, 'count,asc')

    export_inventory(inv)
    print("\n\nEXPORT COMPLETE\n")


  main()