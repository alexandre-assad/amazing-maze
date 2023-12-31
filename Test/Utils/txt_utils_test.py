import unittest 
from Utils.os_utils import *
from Utils.txt_utils import *

class TestTxtUtils(unittest.TestCase):

    def test_read_txt(self):
        self.assertEqual(read_txt("lab1.txt")[0:2],"##")

    def test_write_txt(self):
        write_txt("######\n#####","lab2.txt")
        self.assertEqual(read_txt("lab2.txt")[0:2],"##")