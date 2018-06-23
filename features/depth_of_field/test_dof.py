import unittest
from depth_of_field import DOF
class TestDepthOfField(unittest.TestCase):
    
    def testDepthOfField(self):
       DOF.DepthOfField("./depth_of_field/timg-2.jpeg")
if __name__ == '__main__':
    unittest.main()