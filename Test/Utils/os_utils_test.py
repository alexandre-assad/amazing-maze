import unittest
from Utils.os_utils import *


class TestOsUtils(unittest.TestCase):

    def test_path_Txt(self):
        self.assertEqual(path_txt("lab1.txt"),"Labyrinth_files/lab1.txt")