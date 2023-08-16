import serial
import win32api
import win32con

port = 'COM3'

baud_rate = 9600

ser = serial.Serial(port, baud_rate, timeout=0)

def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while(True):
    
    for line in ser.read():

        if line == 1:
            mouse_click(x, y)
        
ser.close()
