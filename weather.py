import pyautogui
import time

def checkPosition():
    screenWidth, screenHeight = pyautogui.size()
    currenMouseX, currentMouseY = pyautogui.position()
    print(f"Screen width: {screenWidth}\nScreen height: {screenHeight}\nx: {currenMouseX}\ny: {currentMouseY}")

def checkWeather():
    location = input('Enter location to check weather: ').capitalize()
    openFile('chrome')
    pyautogui.hotkey('command','t')
    searchOnGoogle('pogoda ' + location)
    waitForPageLoading()
    fileName = creatFileName(location)
    pyautogui.screenshot(fileName)
    pyautogui.hotkey('command','w')
    openFile(fileName)

def openFile(nameOfFile):
    pyautogui.hotkey('command','space')
    pyautogui.sleep(0.1)
    pyautogui.write(nameOfFile)
    pyautogui.press('enter')

def waitForPageLoading():
    while(pyautogui.pixelMatchesColor(92, 59, (255, 255, 255))):
        pyautogui.sleep(0.01)

def searchOnGoogle(phrase):
    pyautogui.click(154,61)
    pyautogui.write(phrase)
    pyautogui.press('enter')

def creatFileName(location):
    now=time.localtime()
    fileName = 'weather' + location + '_' + str(now.tm_mday) +'.'+ str(now.tm_mon) + '; ' + str(now.tm_hour) + '.' + str(now.tm_min) + '.png' 
    return fileName

checkWeather()