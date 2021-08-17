from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
HTTPS = "https://"

# hard coded data to test
siteDomain = "indeed.com"
jobSearch = "Any Job Title"
locationSearch = "City, State example: Austin, TX"

listOfJobs = []

def if_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True


def if_exists_by_class_name(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True


def if_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def removeSpaces(strArray):

    newjobCounter = 0
    jobCounter = 0

    for i, word in enumerate(strArray):

        jobCounter += 1

        if strArray[i].__contains__("\n"):
            strArray[i] = strArray[i].replace("\n", " ")
        if strArray[i].__contains__("new"):
            newjobCounter += 1

        print(strArray[i] + "\n")

    if newjobCounter == 0:
        print("Unfortunately, there are no new jobs for this search")
    else:
        print("With " + str(newjobCounter) + " out of " + str(jobCounter) + " new jobs!")

    return strArray

try:

    # Goes to Site
    driver.get(HTTPS + siteDomain)

    # obtains access to elements from website
    searchJob = driver.find_element_by_name("q")
    searchLocation = driver.find_element_by_name("l")

    # clear text field
    searchJob.send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)
    searchLocation.send_keys(Keys.CONTROL, "a", Keys.BACK_SPACE)

    # inputs values into website elements
    searchJob.send_keys(jobSearch)
    searchLocation.send_keys(locationSearch)

    # presses button to search
    searchLocation.send_keys(Keys.RETURN)

    # get jobs from first page
    jobCards = driver.find_elements_by_class_name("jobCard_mainContent")
    for job in jobCards:
        listOfJobs.append(job.text)

    # add all links to a list
    linklist = []
    page_counter = 1

    # gets links for pages 2 through 5, ref link for page 1 is never actually clicked
    for link in driver.find_elements_by_xpath('//*[@id="resultsCol"]/nav/div/ul/li//a'):
        if page_counter >= 5:
            break

        linklist.append(link.get_attribute('href'))
        page_counter += 1

    for link in linklist:
        driver.get(link)

        time.sleep(2)

        # checks for popup, if there is popup, exit out and sleep
        if if_exists_by_id("popover-x"):
            driver.find_element_by_id("popover-x").click()

        # obtains data in class name value
        jobCards = driver.find_elements_by_class_name("jobCard_mainContent")

        # prints number of jobs returned
        print(str(len(jobCards)) + " jobs in: " + locationSearch)

        # inserts each job into list of jobs array
        # commented out to make debugging easier
        for jobCard in jobCards:

            # Maybe TODO: seperate each card into title, company name, company location

            # company location xpath: //*[@id="sj_7a8808e8a395e9b8"]/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/pre/div
            # Not sure how to get around hardcoded id

            listOfJobs.append(jobCard.text)

    print("Indeed page links: " + str(linklist))
    print(removeSpaces(listOfJobs))



except ValueError:
    print(ValueError)

finally:
    driver.quit()
