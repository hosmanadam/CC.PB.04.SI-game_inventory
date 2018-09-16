import unittest
import csv
from gameInventory import *


# DO NOT EDIT THIS FILE!
# This file contains tests to check if your code is working correctly.
# Run this file to check whether you have a good solution!
# (note: passing all tests does not mean that your code is correct)
class GameInventoryTests(unittest.TestCase):

    def test_add_single_item(self):
        _inventory = {'rope': 1, 'torch': 6}
        loot = ['torch']
        add_to_inventory(_inventory, loot)

        self.assertDictEqual(_inventory, {'rope': 1, 'torch': 7})

    def test_add_multiple_items(self):
        _inventory = {'rope': 1, 'torch': 6}
        loot = ['torch', 'torch', 'torch']
        add_to_inventory(_inventory, loot)

        self.assertDictEqual(_inventory, {'rope': 1, 'torch': 9})

    def test_import_inventory(self):
        _inventory = {'rope': 1, 'torch': 6}
        import_inventory(_inventory, "test_inventory.csv")

        self.assertDictEqual(_inventory, {
            'rope': 1,
            'torch': 6,
            'battleaxe': 1,
            'dagger': 3,
            'gold coin': 1
        })

    def test_export_inventory(self):
        export_inventory({'dagger': 3, 'gold coin': 1, "battleaxe": 1},
                         "test_inventory_export.csv")

        with open("test_inventory_export.csv", newline='') as csvfile:
            expected = ["dagger", "gold coin", "battleaxe", "dagger", "dagger"]
            expected.sort()
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                row.sort()
                self.assertListEqual(expected, row)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
