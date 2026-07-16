
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import sys
import time


def show_menu():
    print("\n" + "="*50) # for aesthetic 50 time = sign
    print("           SELENIUM MENU          ")
    print("="*50)
    print("1.  Open duckduckgo.com Search By.NAME, By.CLASSNAME")
    print("2.  Open amazon.com Search By.XPATH")
    print("3.  Open selenium.dev Search By.LINK TEXT)")
    print("0.  Exit")
    print("="*50) # for aesthetic 50 time = sign


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-3): ").strip()
        
        if choice == '0':
            print("\nExiting program. Goodbye!")
            sys.exit()
            
        elif choice == '1':
            driver = webdriver.Chrome()

            driver.get("https://duckduckgo.com")
            driver.maximize_window()

            input1 = driver.find_element(By.NAME, "q")
            input1.send_keys("selenium python")
            input1.send_keys(Keys.ENTER)

            time.sleep(5)

            driver.back()

            time.sleep(5)

            driver.forward()

            time.sleep(5)

            driver.quit()
                

        elif choice == '2':
            service = Service(r"C:\WebDriver\chromedriver.exe")

            driver = webdriver.Chrome(service=service)

            driver.get("https://www.amazon.in/")

            driver.maximize_window()
            time.sleep(5)
            driver.refresh()
            time.sleep(5)

            search_box = driver.find_element(By.ID, "twotabsearchtextbox")
            search_box.send_keys("IPhone")

            driver.find_element(By.ID, "nav-search-submit-button").click()

            time.sleep(5)

            iphone_list = driver.find_elements(By.XPATH,"//h2/span")
            print(str(len(iphone_list))+ "products found ")
            for iphone in iphone_list:
                print(iphone.text)


            driver.quit()

        elif choice == '3':
            driver = webdriver.Chrome()

            driver.get("https://www.selenium.dev")

            driver.maximize_window()
            
            

            time.sleep(5)
            
            search_box = driver.find_element(By.LINK_TEXT, "Downloads")
            search_box.click()
            time.sleep(5)
            
            
            driver.quit()

       
        else:
            print("\n[INVALID] Please enter a valid number between 0 and 3.")

if __name__ == '__main__': # for running all codes options in single file
    main()


