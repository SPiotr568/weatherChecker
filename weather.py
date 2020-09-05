import pyautogui

def checkPosition():
    screenWidth, screenHeight = pyautogui.size()
    currenMouseX, currentMouseY = pyautogui.position()
    print(f"Screen width: {screenWidth}\nScreen height: {screenHeight}\nx: {currenMouseX}\ny: {currentMouseY}")

def checkWeather():
    location = input('Enter location to check weather: ')
    openFile('chrome')
    pyautogui.hotkey('command','t')
    pyautogui.moveTo(154,61)
    pyautogui.click()
    pyautogui.write('pogoda ' + location.capitalize())
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.screenshot('pogoda.png')
    pyautogui.hotkey('command','w')
    openFile('pogoda.png')
    pyautogui.sleep(0.1)
    pyautogui.hotkey('ctrl','command','f')

def openFile(nameOfFile):
    pyautogui.hotkey('command','space')
    pyautogui.sleep(0.1)
    pyautogui.write(nameOfFile)
    pyautogui.press('enter')

checkPosition()
checkWeather()