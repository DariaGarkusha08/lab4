import unittest
import geometry

class TestGeometryFunctions(unittest.TestCase):
    """
    Test cases for geometry functions.
    """
    
    # Tests for area function
    def test_area_positive_integers(self):
        """Test area calculation with positive integers"""
        self.assertEqual(geometry.area(5, 3), 15)
    
    def test_area_positive_floats(self):
        """Test area calculation with positive floats"""
        self.assertAlmostEqual(geometry.area(2.5, 4.2), 10.5)
    
    def test_area_zero_values(self):
        """Test area calculation with zero values"""
        self.assertEqual(geometry.area(0, 5), 0)
        self.assertEqual(geometry.area(5, 0), 0)
        self.assertEqual(geometry.area(0, 0), 0)
    
    def test_area_negative_values(self):
        """Test area calculation with negative values"""
        with self.assertRaises(ValueError):
            geometry.area(-5, 3)
        with self.assertRaises(ValueError):
            geometry.area(5, -3)
    
    def test_area_invalid_types(self):
        """Test area calculation with invalid types"""
        with self.assertRaises(TypeError):
            geometry.area("5", 3)
        with self.assertRaises(TypeError):
            geometry.area(5, "3")
        with self.assertRaises(TypeError):
            geometry.area([5], 3)
    
    # Tests for perimeter function
    def test_perimeter_positive_integers(self):
        """Test perimeter calculation with positive integers"""
        self.assertEqual(geometry.perimeter(5, 3), 16)
    
    def test_perimeter_positive_floats(self):
        """Test perimeter calculation with positive floats"""
        self.assertAlmostEqual(geometry.perimeter(2.5, 4.2), 13.4)
    
    def test_perimeter_zero_values(self):
        """Test perimeter calculation with zero values"""
        self.assertEqual(geometry.perimeter(0, 5), 10)
        self.assertEqual(geometry.perimeter(5, 0), 10)
        self.assertEqual(geometry.perimeter(0, 0), 0)
    
    def test_perimeter_negative_values(self):
        """Test perimeter calculation with negative values"""
        with self.assertRaises(ValueError):
            geometry.perimeter(-5, 3)
        with self.assertRaises(ValueError):
            geometry.perimeter(5, -3)
    
    def test_perimeter_invalid_types(self):
        """Test perimeter calculation with invalid types"""
        with self.assertRaises(TypeError):
            geometry.perimeter("5", 3)
        with self.assertRaises(TypeError):
            geometry.perimeter(5, "3")

    # Edge cases
    def test_area_large_numbers(self):
        """Test area calculation with large numbers"""
        self.assertEqual(geometry.area(1000000, 1000000), 1000000000000)
    
    def test_perimeter_large_numbers(self):
        """Test perimeter calculation with large numbers"""
        self.assertEqual(geometry.perimeter(1000000, 1000000), 4000000)

if __name__ == '__main__':
    unittest.main()
