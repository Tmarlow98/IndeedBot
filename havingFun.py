from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
HTTPS = "https://"

# hard coded data to test 
siteDomain = "indeed.com"
jobSearch = "Entry Level Software Developer"
locationSearch = "Richmond, VA"

listOfJobs = [""]

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

# obtains data in class name value
jobCards = driver.find_elements_by_class_name("jobCard_mainContent")

# prints number of jobs returned
print(str(len(jobCards)) + " jobs in: " + locationSearch)

# inserts jobcards
for jobCard in jobCards:
    listOfJobs.append(jobCard.text)

# 
def removeSpaces(strArray):

    newjobCounter = 0

    for i, word in enumerate(strArray):
        if strArray[i].__contains__("\n"):
            strArray[i] = strArray[i].replace("\n", " ")
        if strArray[i].__contains__("new"):
            newjobCounter += 1

        print(strArray[i] + "\n")

    if newjobCounter == 0:
        print("Unfortunately, there are no new jobs for this search")
    else:
        print("With " + str(newjobCounter) + " out of " + str(len(jobCards)) + " new jobs!")

    return strArray


print(removeSpaces(listOfJobs))
# driver.quit()

# locationSearch = ["Richmond, VA", "Fort Lauderdale, FL", "Remote"]
