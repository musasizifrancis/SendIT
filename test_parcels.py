import json
from parcels import app
import pytest

class MyFirstTests(unittest.TestCase):

 def test_hello(self):
        self.assertEqual( 'Welcome to our Parcel Delivery Order ')

