import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. They go
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # They notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # They are invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # They type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When they hit enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys('Keys.Enter')
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting them to add another item. They
        # enter "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Continue writing the functional test ;)')


        # The page updates again, and now shows both items on their list

        # Edith wonders whether the site will remember their list. Then they see
        # that the site has generated a unique URL for them -- there is some
        # explanatory text to that effect.

        # They visit that URL - their to-do list is still there.

        # Satisfied, they go back to sleep


if __name__ == '__main__':
    unittest.main()
