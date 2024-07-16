# chatgpt_automation_mac

ChatGPT Automation is a Python project that aims to automate interactions with OpenAI's ChatGPT using Selenium WebDriver. Currently, it requires human interaction for log-in and human verification. It handles connecting to ChatGPT, sending prompts, and retrieving responses. This tool can be useful for experimenting with ChatGPT or building similar web automation tools.

## What it do
- Automated messaging to ChatGPT
- File(s) uploads
- Storing conversations


## What it don't do so well currently
- Having to the browser with the command below
- I haven't quite nailed down the delay timings for waiting for a response. For now a prompt of "update" retrieves the latest message without updating the conversation.

## Prerequisites

### Download Google Chrome for Testing

1. Go to the [Google Chrome for Testing download page](https://www.google.com/chrome/).
2. Download the version appropriate for your operating system.
3. Install the downloaded version of Chrome.

### Download ChromeDriver

1. Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads).
2. Download the version of ChromeDriver that matches your version of Google Chrome.
3. Extract the downloaded file and move the `chromedriver` executable to a known location on your system, e.g., `/usr/local/bin`.


### Install the Python Package

You can install the package using pip:

```sh
pip install git+https://github.com/lxwooxy/chatgpt_automation_mac.git
```

### Launch Chrome with Remote Debugging

To enable remote debugging and use a custom user data directory, run the following command in your terminal:

```sh
"/Users/yourusername/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing" --remote-debugging-port=9222 --user-data-dir="/Users/yourusername/ChromeProfile"
```

Replace /Users/yourusername/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing with the path to your Chrome for Testing executable, and /Users/yourusername/ChromeProfile with the path to your desired user data directory.

## Example Usage
### Basic Usage

```python

from chatgpt_automation_mac.handler import ChatGPTAutomation

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
```
### Continuous Interaction with ChatGPT

This example demonstrates how to continuously interact with ChatGPT in a loop, allowing the user to input messages until they choose to exit.

```python

from chatgpt_automation_mac.handler import ChatGPTAutomation

# Define the path where the Chrome driver is installed on your computer
chrome_driver_path = "/path/to/chromedriver"

# Create an instance to connect to the existing Chrome for Testing instance
chatgpt = ChatGPTAutomation(chrome_driver_path=chrome_driver_path, remote_debugging_port=9222)

file_name = "conversation.txt"

try:
    while True:
        # Get input from the user
        prompt = input("Message ChatGPT (or type 'exit' to leave): ")
        if prompt.lower() in ['exit', 'quit', 'goodbye', 'leave']:
            break
        
        # Send the prompt to ChatGPT
        chatgpt.send_prompt_to_chatgpt(prompt)

        # Retrieve the last response from ChatGPT
        response = chatgpt.return_last_response()
        print(f"ChatGPT: {response}")

        # Save the conversation to a text file
        chatgpt.save_conversation(file_name, prompt, response)
        print("Conversation updated.")
finally:
    # Close the browser and terminate the WebDriver session
    chatgpt.quit()
    print("Goodbye!")
```
### Uploading Files

This example demonstrates how to upload a file to ChatGPT during the interaction.

```python

from chatgpt_automation_mac.handler import ChatGPTAutomation

# Define the path where the Chrome driver is installed on your computer
chrome_driver_path = "/path/to/chromedriver"

# Create an instance to connect to the existing Chrome for Testing instance
chatgpt = ChatGPTAutomation(chrome_driver_path=chrome_driver_path, remote_debugging_port=9222)

file_name = "conversation.txt"

try:
    while True:
        # Get input from the user
        prompt = input("Message ChatGPT (or type 'upload' to upload a file, 'exit' to leave): ")
        if prompt.lower() in ['exit', 'quit', 'goodbye', 'leave']:
            break
        elif prompt.lower() == 'upload':
            file_path = input("Enter the file path to upload: ")
            chatgpt.upload_file(file_path)
            print("File uploaded.")
            continue
        
        # Send the prompt to ChatGPT
        chatgpt.send_prompt_to_chatgpt(prompt)

        # Retrieve the last response from ChatGPT
        response = chatgpt.return_last_response()
        print(f"ChatGPT: {response}")

        # Save the conversation to a text file
        chatgpt.save_conversation(file_name, prompt, response)
        print("Conversation updated.")
finally:
    # Close the browser and terminate the WebDriver session
    chatgpt.quit()
    print("Goodbye!")
```
## License

This project is licensed under the MIT License.