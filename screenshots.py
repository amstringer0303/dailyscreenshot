from selenium import webdriver
from PIL import Image
import time
from datetime import datetime
import os

def capture_screenshot():
    try:
        # URL centered around Barrow, AK, and visible during daytime
        url = 'https://worldview.earthdata.nasa.gov/?v=-157.23997415657044,71.08082336006164,-156.44895853157044,71.5274175983429&s=-156.7887,71.2906&t=2024-07-10-T18%3A11%3A29Z'
        
        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        
        # Navigate to NASA Worldview
        driver.get(url)
        time.sleep(10)  # Wait for the page to load

        # Capture screenshot
        screenshot = driver.get_screenshot_as_png()
        
        # Define the paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(base_dir, f'screenshot_{timestamp}.png')

        # Save the screenshot
        with open(filename, 'wb') as f:
            f.write(screenshot)
        
        # Open the screenshot
        image = Image.open(filename)
        
        # Define the cropping box (adjust based on the screenshot size and Barrow's location)
        width, height = image.size
        left = 0
        top = 0
        right = width
        bottom = height
        
        cropped_image = image.crop((left, top, right, bottom))
        cropped_filename = os.path.join(base_dir, f'cropped_screenshot_{timestamp}.png')
        cropped_image.save(cropped_filename)
        
        # Print a message indicating success
        print(f"Screenshot saved as {filename}")
        print(f"Cropped screenshot saved as {cropped_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_screenshot()