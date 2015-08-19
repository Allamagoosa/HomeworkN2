#!/usr/bin/python
import harvester
import unittest
import os

""" unit test for harvester.py """

class TestHarvester(unittest.TestCase):

    def setUp(self):
        pass 
      
    def tearDown(self):
        reload (harvester)
    
    def test_unit(self):
        h = harvester.Harvester("/home/pm/work/x/")
        self.assertEqual(h.dir_path, "/home/pm/work/x/")
        
    def test_list_files(self):
        h = harvester.Harvester("/etc/")
        listtest = h.list_files
        self.assertIsNotNone(listtest)
        
    def test_trim(self):
        h = harvester.Harvester(os.getcwd())
        trim_res = h.trim("/harvester")
        self.assertEqual(trim_res, "This module collect docstrings from root folder")
        
if __name__ == "__main__":
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestHarvester))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
