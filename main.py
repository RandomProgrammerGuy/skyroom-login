from selenium import webdriver

print('lessons list: \nphys = physics\nchem = chemistry\nmath = math\nlit = literature\neng = english\ndini = '
      'dini\nneg = negaresh\n arab = arabic\n geog = geography\ngeom = geometry')
print('________________________________________________________________________')
lesson = input('Choose a Lesson: ')

username = "2284051545"
password = "2284051545"

driver = webdriver.Chrome("/Users/parsafarjam/dev/WebDrivers/chromedriver")

if lesson == 'phys':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-fizik")
elif lesson == 'chem':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-shimi")
elif lesson == 'math':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-riazi")
elif lesson == 'lit':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-farsi")
elif lesson == 'eng':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-zaban")
elif lesson == 'dini':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-dini")
elif lesson == 'neg':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-negaresh")
elif lesson == 'arab':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-arabi")
elif lesson == 'geog':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-joghrafi")
elif lesson == 'geom':
    driver.get("https://www.skyroom.online/ch/dastgheib2/10riazi1-joghrafi")
else:
    print("Err 001: invalid lesson entered")

user_textbox = driver.find_element_by_id('username')
user_textbox.send_keys(username)

pass_textbox = driver.find_element_by_id('password')
user_textbox.send_keys(password)

login_butt = driver.find_element_by_id('btn_login')
login_butt.submit()
