# chatgpt_selenium_automation

ChatGPT Automation is a Python project that aims to automate interactions with OpenAI's ChatGPT using Selenium WebDriver. Currently, it requires human interaction for log-in and human verification. It handles launching Chrome, connecting to ChatGPT, sending prompts, and retrieving responses. This tool can be useful for experimenting with ChatGPT or building similar web automation tools.

## Prerequisites

- Install the library: `pip install git+https://github.com/yourusername/chatgpt_selenium_automation.git`
- Download the appropriate version of `chromedriver` and save it to a known location on your system.

## Example Usage

```python
from chatgpt_selenium_automation.handler import ChatGPTAutomation

# Define the path where the Chrome driver is installed on your computer
chrome_driver_path = "/path/to/chromedriver"

# Define the path where the Chrome browser is installed
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to ChatGPT
prompt = "What are the benefits of exercise?"
chatgpt.send_prompt_to_chatgpt(prompt)

# Retrieve the last response from ChatGPT
response = chatgpt.return_last_response()
print(response)

# Save the conversation to a text file
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)

# Close the browser and terminate the WebDriver session
chatgpt.quit()
