from math import radians, cos, sin, asin, sqrt
import unittest,logging

logging.basicConfig(filename="loginfo.log",  format='%(asctime)s %(message)s',  filemode='w') 
logger=logging.getLogger()  
logger.setLevel(logging.DEBUG) 

""" Function to validate the points"""
def lat_and_lon_validator(lat1, lat2, lon1, lon2):
    if (abs(lat1)<=90 and abs(lat2)<=90 and abs(lon1)<=180 and abs(lon2)<=180):
        return True    
    else:
        logging.warning("The passed values are not in range ")
        return False 
    
""" Function to find distance b|w two points on earth"""
def distance(lat1, lat2, lon1, lon2):
    if lat_and_lon_validator(lat1, lat2, lon1, lon2):
        if((abs(lat1)==abs(lat2) and abs(lon1)==abs(lon2))or (abs(lat1)==abs(lat2)==abs(lon1)==abs(lon2))):
            return 0
        else:
            lon1 = radians(lon1)
            lon2 = radians(lon2)
            lat1 = radians(lat1)
            lat2 = radians(lat2)
      
            # Haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            distance_in_radians = 2 * asin(sqrt(a))
            
            # Radius of earth in kilometers. 
            radius = 6371
            distance_in_km=distance_in_radians*radius
            return(distance_in_km)
            logging.info("The distance between two points is: " +distance_in_km)
    else:
        logging.warning("Passed wrong arguments")
        return "Invalid Input"


""" Testing the function "distance" b|w two points on earth""" 
  
class test_distance(unittest.TestCase):
    logging.info("TestCases started to run")
    
    """Testing the distance function with all different values """
    def test_distance_with_all_distinct_values(self):
         result=distance(20,30,-180,180)
         self.assertEqual(result,1111.9492664455872)
         
    """Testing the distance with same latitude values and same longitude values"""
    def test_distance_between_same_points(self):
         result=distance(30,30,170,170)
         self.assertEqual(result,0)
      
    """Testing the distance with invalid values """
    def test_invalid_latitude(self):
         result=distance(100,30,170,170)
         self.assertEqual(result,"Invalid Input")

    """Testing the distance with all same values """
    def test_distance_between_same_points_01(self):
         result=distance(30,30,30,30)
         self.assertEqual(result,0)
         




if __name__ == '__main__':  
    unittest.main()  #invoking the unit test framework  

