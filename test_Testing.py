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
        self.assertTrue(validate_json('{"key": "value"}'))
        self.assertFalse(validate_json('{"key": "value"'))
        self.assertFalse(validate_json('{"key": "value"}"'))
        
if __name__ == '__main__':
    unittest.main()