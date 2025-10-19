#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_assessment_value, get_tax_assessed

class Test_get_assessment_value(unittest.TestCase):
    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000),6000)
        self.assertEqual(get_assessment_value(20000),12000)

class Test_get_tax_assessed(unittest.TestCase):
    def test_get_tax_assessed(self):
        self.assertEqual(get_tax_assessed(6000),(60*.72))
        self.assertEqual(get_tax_assessed(10000),72)


import unittest

from src.question_b.question_b import get_miles_per_hour

class Test_get_miles_per_hour(unittest.TestCase):
    def test_get_miles_per_hour(self):
        self.assertEqual(get_miles_per_hour(32,60),19.883872 )

import unittest

from src.question_c.question_c import use_global

class Test_use_global(unittest.TestCase):
    def test_use_global(self):
        self.assertEqual(use_global(),5)


import unittest

from src.question_d.question_d import is_prime

class Test_is_prime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(4),False)
        self.assertEqual(is_prime(5),True)
        self.assertEqual(is_prime(11),True)



