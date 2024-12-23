import unittest
from unittest.mock import patch, MagicMock
from src.autojs_py.opearation import clicktext

class TestClickText(unittest.TestCase):
    @patch('src.autojs_py.opearation.screenshot')
    @patch('src.autojs_py.opearation.ocr2box')
    @patch('pyautogui.click')
    def test_patch_clicktext(self, mock_click, mock_ocr2box, mock_screenshot):
        # Mock the screenshot function to return a dummy image
        mock_screenshot.return_value = 'dummy_image'

        # Mock the ocr2box function to return a dummy OCR result
        mock_ocr2box.return_value = {
            'text': ['example text'],
            'conf': [95],
            'left': [100],
            'top': [200],
            'width': [50],
            'height': [20]
        }

        # Call the clicktext function with the text to click
        clicktext('example text')

        # Assert that pyautogui.click was called with the correct coordinates
        mock_click.assert_called_once_with(125, 210)

    def test_clicktext(self):
        # Call the clicktext function with the text to click
        clicktext('即将')
if __name__ == '__main__':
    unittest.main()