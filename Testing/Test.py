import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
report = Report()
driver: WebDriver = webdriver.Chrome(executable_path="D:\\IDM Downloads\\Download\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Device',
    release_name='Test V1',
    selenium_driver=driver
)
driver.get('http://127.0.0.1:8000/')
# Test Case 1
try:
    report.write_step(
        'Go to Landing Page',
        status=report.status.Start,
        test_number = 1
    )
    assert (driver.title == 'Home')
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Pass,
        screenshot = True
    )
    time.sleep(3)
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot = True
    )
    
except Exception as e:
    report.write_step(
        'Failed to open landing Page',
        status=report.status.Fail,
        screenshot = True
    )

#Test Case 2
try:
    report.write_step(
        'Go to Login Page',
        status = report.status.Start,
        test_number = 2
    )
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "LOGIN").click()
    time.sleep(3)
    report.write_step(
        'Successfully Load Login Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot = True
    )
    
except Exception as e:
    report.write_step(
        'Failed to Load Login Page',
        status=report.status.Fail,
        screenshot = True
    )

#Test Case 3
try:
    report.write_step(
        'Go to Signup Page',
        status = report.status.Start,
        test_number = 3
    )
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Signup").click()
    time.sleep(3)
    report.write_step(
        'Successfully Load Signup Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot = True
    )
    
except Exception as e:
    report.write_step(
        'Failed to Load Signup Page',
        status=report.status.Fail,
        screenshot = True
    )

# Test Case 4
try:
    report.write_step(
        'Signup for a user',
        status = report.status.Start,
        test_number = 4
    )
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('Bithi')
    driver.find_element(By.NAME, 'email').send_keys('Bithi@gmail.com')
    driver.find_element(By.NAME, 'password').send_keys('uapcse')
    driver.find_element(By.NAME, 'confirm_password').send_keys('uapcse')
    time.sleep(1)
    driver.find_element(By.NAME, "Signup").click()
    time.sleep(3)
    report.write_step(
        'Successfully Signup',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
except Exception as e:
     report.write_step(
        'Failed to Signup',
        status=report.status.Fail,
        screenshot=True
      )
    

# Test Case 5
try:
    report.write_step(
        'Login for a user',
        status = report.status.Start,
        test_number = 5
    )
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('Bithi')
    driver.find_element(By.NAME, 'password').send_keys('uapcse')
    time.sleep(1)
    driver.find_element(By.NAME, "Login").click()
    time.sleep(3)
    report.write_step(
        'Successfully Login',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

except Exception as e:
    report.write_step(
        'Failed to Login',
        status=report.status.Fail,
        screenshot=True
    )

# Test Case 6
try:
    report.write_step(
        'Open a Post Automatically',
        status = report.status.Start,
        test_number = 6
    )
    driver.find_element(By.ID, 'blog_title').click()
    time.sleep(3)
    report.write_step(
        'Successfully Opened a Post Automatically',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot = True
    )
    
except Exception as e:
    report.write_step(
        'Failed to open a Post  Automatically',
        status=report.status.Fail,
        screenshot = True
    )

# Test Case 7
try:
    report.write_step(
        'Open a Post By Title',
        status = report.status.Start,
        test_number = 7
    )
    driver.find_element(By.LINK_TEXT, 'মিরপুরে পথশিশুদের খাবার দিতে আমাদের সাথে আসুন').click()
    time.sleep(3)
    report.write_step(
        'Successfully Opened a Post by Title',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot = True
    )
    
except Exception as e:
    report.write_step(
        'Failed to open a Post  by Title',
        status=report.status.Fail,
        screenshot = True
    )

# Test Case 8
try:
    report.write_step(
        'Donate',
        status = report.status.Start,
        test_number = 8
    )
    time.sleep(1)
    driver.find_element(By.NAME, 'amount').send_keys('1000')
    driver.find_element(By.ID, 'Donate').click()
    time.sleep(3)
    report.write_step(
        'Successfully Donated',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

except Exception as e:
    report.write_step(
        'Failed to Donate',
        status=report.status.Fail,
        screenshot=True
    )

# Test Case 9
try:
    report.write_step(
        'Load Discription',
        status = report.status.Start,
        test_number = 9
    )
    time.sleep(1)
    elements = driver.find_element(By.ID, 'discription')
    time.sleep(3)
    for e in elements:
        print(e.text)
    time.sleep(1)
    report.write_step(
        'Successfully load Discription',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
    
except Exception as e:
    report.write_step(
        'Failed to Load Discription',
        status=report.status.Fail,
        screenshot=True
    )

# Test Case 10
try:
    report.write_step(
        'Logout a user',
        status = report.status.Start,
        test_number = 10
    )
    time.sleep(1)
    driver.find_element(By.ID, 'username').click()
    time.sleep(1)
    driver.find_element(By.ID, "Logout").click()
    time.sleep(3)
    report.write_step(
        'Successfully Logout',
        status=report.status.Pass,
        screenshot=True
    )

except AssertionError:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

except Exception as e:
    report.write_step(
        'Failed to Logout',
        status=report.status.Fail,
        screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()