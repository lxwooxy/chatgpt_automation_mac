import unittest
from chatgpt_automation_mac.handler import ChatGPTAutomation

class TestChatGPTAutomation(unittest.TestCase):
    def setUp(self):
        self.chrome_driver_path = '/path/to/chromedriver'
        self.chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        self.chatgpt = ChatGPTAutomation(self.chrome_path, self.chrome_driver_path)

    def test_send_prompt(self):
        prompt = "What are the benefits of exercise?"
        self.chatgpt.send_prompt_to_chatgpt(prompt)
        response = self.chatgpt.return_last_response()
        self.assertIsNotNone(response)

    def tearDown(self):
        self.chatgpt.quit()

if __name__ == '__main__':
    unittest.main()
