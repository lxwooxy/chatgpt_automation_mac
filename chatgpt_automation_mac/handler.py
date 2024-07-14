import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatGPTAutomation:
    def __init__(self, chrome_driver_path: str, remote_debugging_port=9222):
        options = Options()
        options.debugger_address = f"127.0.0.1:{remote_debugging_port}"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.conversation = []
        self.last_response = ""
        # Ensure we're on the ChatGPT page
        self.driver.get('https://chat.openai.com/chat')

    def send_prompt_to_chatgpt(self, prompt: str, num_files: int = 0):
        try:
            #print(f"num_files: {num_files}")
            #remove any aprostrophes from the prompt
            prompt = prompt.replace("'", "")
            # Locate the input field and send the prompt
            input_box = self.driver.find_element(By.XPATH, '//textarea[contains(@id, "prompt-textarea")]')
            self.driver.execute_script(f"arguments[0].value = '{prompt}';", input_box)
            input_box.send_keys(Keys.RETURN)
            input_box.submit()
            #logging.info("Prompt sent to ChatGPT")
            # Wait until the response is done
            #print(f"Waiting for {num_files * 1.5} seconds for response to finish...")
            time.sleep(num_files * 1.5)
            if num_files == 0:
                time.sleep(5)
  
            self.check_response_ended(prompt)
        except Exception as e:
            logging.error(f"Error sending prompt: {e}")

    
    def check_response_ended(self, prompt: str):
        """Checks if ChatGPT response ended"""
        #print("Checking if response ended...")
        start_time = time.time()
        last_text = ""
        last_check_time = time.time()
    
        while True:
            response_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.text-base')
            # Filter out empty responses and the prompt itself
            response_elements = [response for response in response_elements if response.text.strip() and response.text.strip() != prompt]
            
            # Print out everything in the response_elements
            # for response in response_elements:
            #     print(f"while true loop response: {response.text}")

            if response_elements:
                current_text = response_elements[-1].text
                if current_text.strip() != last_text.strip():
                    #print(f"Current text: {current_text!r} (len: {len(current_text)}) != Last text: {last_text!r} (len: {len(last_text)})")
                    last_text = current_text
                    last_check_time = time.time()
                    #print("It's still cooking")
                else:
                    # If the response has not changed for 1 seconds, break the loop
                    if time.time() - last_check_time > 2:
                        #print("Response has not changed for 2 seconds, considering it done.")
                        break

            # Exit the loop after 60 seconds to avoid hanging indefinitely
            if time.time() - start_time > 60:
                print("Response taking too long, exiting...")
                break

            time.sleep(0.5)  # Check every 0.5 seconds
        time.sleep(1)
        self.last_response = current_text
        
    
    def return_chatgpt_conversation(self):
        """Returns a list of items, even items are the submitted questions (prompts) and odd items are chatgpt response"""
        return self.driver.find_elements(By.CSS_SELECTOR, 'div.text-base')

    def save_conversation(self, file_name: str, prompt: str, response: str):
        """Saves the full chatgpt conversation of the tab open in chrome into a text file."""
        directory_name = "conversations"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        delimiter = "(;･_･)"
        with open(os.path.join(directory_name, file_name), "a") as file:
            file.write(f"prompt: {prompt}\nresponse: {response}\n\n{delimiter}\n\n")

    def return_last_response(self, prompt: str):
        """Returns the text of the last chatgpt response"""
        response_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.text-base')
        response_elements = [response for response in response_elements if response.text.strip() and response.text.strip() != prompt]
             
        # answer = response_elements[-1].text if response_elements else None
        # return answer
        return self.last_response

    
    def upload_file(self, file_paths: list):
        """Uploads a file to ChatGPT"""
        try:
            
            file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
            for file_path in file_paths:
                # Locate the file input element
                file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
                
                # Use JavaScript to clear the value of the file input
                self.driver.execute_script("arguments[0].value = '';", file_input)
                
                # Send the file path to the file input element
                file_input.send_keys(file_path)
                logging.info(f"File {file_path} uploaded successfully.")
                
        except Exception as e:
            logging.error(f"Error uploading file: {e}")

    def quit(self):
        """Closes the browser and terminates the WebDriver session."""
        logging.info("Closing the browser...")
        self.driver.close()
        self.driver.quit()


