import unittest
from unittest.mock import patch, MagicMock
from Question2 import FermosaExtracter

class TestFermosaExtracter(unittest.TestCase):
    """ Unit Tests for the FermosaExtractor class """
    
    @patch("requests.get")
    def test_initialization(self, mock_get):
        mock_get.return_value.text = "<html></html>"
        extractor = FermosaExtracter("https://example.com", 2)
        self.assertEqual(extractor.totalpages, 2)
        self.assertEqual(extractor.url, "https://example.com")
        self.assertIsInstance(extractor.result, list)
    
    @patch("requests.get")
    def test_makeData(self, mock_get):
        # Test the makeData method to check it fetches the correct plant details

        mock_get.return_value.text = '<div class="pd_summary"><p>1. Snake Plant</p></div>'
        extractor = FermosaExtracter("https://example.com", 1)
        data_dict = extractor.makeData("https://example.com", "plant", "Snake Plant", "$20", "YES")
        
        self.assertIsInstance(data_dict, dict)
        self.assertEqual(data_dict["URL"], "https://example.com")
        self.assertEqual(data_dict["Type"], "plant")
        self.assertEqual(data_dict["Price"], "$20")
        self.assertEqual(data_dict["Variegated"], "YES")
        self.assertEqual(data_dict["Name1"], "Snake Plant")
    
    @patch("requests.get")
    def test_saveDataToExcel(self, mock_get):
        # Test the saveDataToExcel() method to check it stores data into excel file or not
        
        mock_get.return_value.text = "<html></html>"
        extractor = FermosaExtracter("https://example.com", 1)
        extractor.result = [
            {"URL": "https://example.com", "Type": "plant", "Price": "$20", "Variegated": "YES", "Name1": "Snake Plant"}
        ]
        
        extractor.saveDataToExcel("test_output.xlsx")

if __name__ == "__main__":
    unittest.main()