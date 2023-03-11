import unittest
from unittest.mock import MagicMock, patch
import about


class TestAboutpage(unittest.TestCase):
    
    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.load', return_value={'app_description': {'appname': 'My App'}, 'statusbar': {'KT': 'All rights reserved'}})
    def test_init(self, mock_load, mock_open):
        about.Aboutpage()
        
        # check that the window title is set correctly
        self.assertEqual(about.about.title(), 'About Page')
        
        # check that the window size is set correctly
        self.assertEqual(about.about.geometry(), '620x450+360+120')
        
        # check that the icon image is set correctly
        self.assertIsInstance(about.about.tk.call_args[0][1], str)
        self.assertIn('logo_04.png', about.about.tk.call_args[0][1])
        
        # check that the Exit button has the correct text
        self.assertEqual(about.home_button1.cget('text'), 'Exit')
        
        # check that the default textbox has the correct initial text
        self.assertIn('About the application\n*------------------------*\n\nMy App', about.default_textbox.get('1.0', 'end'))
        
        # check that the footer label has the correct text
        self.assertEqual(about.footer_text.cget('text'), 'All rights reserved')
        
        about.about.destroy()
    



if __name__ == '__main__':
    unittest.main()
