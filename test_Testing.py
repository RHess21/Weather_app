import unittest

from CleanUp import zipSanitize
class testZipSanitize(unittest.TestCase):
    def test_zipSanitize(self):
        self.assertTrue(zipSanitize('12345'))
        self.assertFalse(zipSanitize('1234'))
        self.assertFalse(zipSanitize('d1234'))


from CleanUp import validate_json
class testValidateJson(unittest.TestCase):
    def test_validate_json(self):
        json_data_bad = {
            "location": "New York",
            "temperature": "25°C",
            "humidity": 70,
            "wind_speed": 10
        }
        json_data_good = {
            "location": "New York",
            "temperature": 25,
            "humidity": 70,
            "wind_speed": 10
        }
        json_data_badFormat = {
            "city": "New York",
            "current_conditions": {
                "temperature": 25,
                "humidity": 70,
                "wind_speed": 10
            }
        }
        self.assertTrue(validate_json(json_data_good))
        self.assertFalse(validate_json(json_data_bad))
        self.assertFalse(validate_json(json_data_badFormat))
        
if __name__ == '__main__':
    unittest.main()