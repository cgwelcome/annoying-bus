from annoyingbus.core import AnnoyingBus
from annoyingbus.information import Information 
import os
import sys
import unittest

class TestInformation(unittest.TestCase):
    
    def test_instance(self):
        f = open(os.devnull, 'w') 
        sys.stdout = f      # Removing side-effects of print

        b = AnnoyingBus()
        info = b.search()
        self.assertEqual(isinstance(info, Information), True)
         
