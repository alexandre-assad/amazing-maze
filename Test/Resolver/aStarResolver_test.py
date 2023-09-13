import unittest
from src.Materials.Labyrinth import Labyrinth
from src.Generator.kruskalGenerator import *
from src.Resolver.aStarResolver import *
from src.Utils.utils import *
from src.Utils.txt_utils import *


class TestAStarResolver(unittest.TestCase):

    def test_aStarResolver(self):
        Lab1 = aStarResolver("test","lab5.txt")
        self.assertEqual(
            Lab1.displayResolver(),
            """
#o#####
#o o o#
# # # #
#*#*#o#
# ### #
#* *#oo
#######""",
        )
        write_txt(Lab1.displayResolver(), "lab5_resolver.txt","test")
        kruskalGenerator(10, "lab6.txt","test")
        write_txt(aStarResolver("test","lab6.txt").displayResolver(), "lab6_resolver.txt","test")
