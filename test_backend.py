# test_backend.py
import unittest
from backend import *

class TestBackendFunctions(unittest.TestCase):
    def test_add_product_to_inventory(self):
        initial_inventory = len(get_inventory())
        add_product_to_inventory("Test Product", 10.0, 100)
        new_inventory = len(get_inventory())
        self.assertEqual(new_inventory, initial_inventory + 1)

    def test_sell_product(self):
        product_id = add_product_to_inventory("Test Product", 10.0, 100)
        self.assertTrue(sell_product(product_id, 50))

if __name__ == "__main__":
    unittest.main()

