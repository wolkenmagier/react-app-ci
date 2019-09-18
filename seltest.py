# Import unittest module for creating unit tests
import unittest

# Import time module to implement 
import time

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

# For automating data input
from selenium.webdriver.common.keys import Keys

# For providing custom configurations for Chrome to run
from selenium.webdriver.chrome.options import Options


# --------------------------------------
# Provide a class for the unit test case
class PythonOrgSearchChrome(unittest.TestCase):

	# Anything declared in setUp will be executed for all test cases
	def setUp(self):
		# Select which device you want to emulate by uncommenting it
		# More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
		mobile_emulation = { 
			"deviceName": "Nexus 5"
			
			# Or specify a specific build using the following two arguments
			#"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
		    #"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
		}
		
		# Define a variable to hold all the configurations we want
		chrome_options = webdriver.ChromeOptions()
		
		# Add the mobile emulation to the chrome options variable
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		chrome_options.add_argument('--headless')

		# Create driver, pass it the path to the chromedriver file and the special configurations you want to run
		self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)

	# An individual test case. Must start with 'test_' (as per unittest module)
	def test_search_in_python_chrome(self):	
		# Assigning a local variable for the global driver
		driver = self.driver

		# Go to google.com
		driver.get('http://localhost:8080')
		time.sleep(1)
		assert "React App" not in driver.title
		

		# Take a screenshot of the results
	# Anything declared in tearDown will be executed for all test cases
	def tearDown(self):
		# Close the browser. 
		# Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
		self.driver.close()

# Boilerplate code to start the unit tests
if __name__ == "__main__":
	unittest.main()
