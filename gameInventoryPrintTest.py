from gameInventory import *

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

if __name__ == '__main__':
  main()