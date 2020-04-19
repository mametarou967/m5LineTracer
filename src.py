from m5stack import *
from m5ui import *
from uiflow import *
import machine
import hat

setScreenColor(0x111111)

hat_BeetleC0 = hat.get(hat.BEETLEC)

label0 = M5TextBox(48, 1, "Line Tracer on BeetleC", lcd.FONT_Default,0xff0378, rotate=90)
lcd.clear()
deltaY = 0
pinin = machine.Pin(33, mode=machine.Pin.IN, pull=machine.Pin.PULL_UP)
leftover = False
rigthover = False

class Display:
  
  def __init__(self):
    self.row = 0
    self.rowMax = 13
  
  def printDisp(self,string):
    if self.row >= self.rowMax:
      lcd.clear()
      self.row = 0
    M5TextBox(0, self.row * 12, str(deltaY) + "_" + string)
    self.row = self.row + 1

display = Display()

while True:
  lineTraceValue = pinin.value()
  display.printDisp(str(lineTraceValue))
  if lineTraceValue == 1:
    leftover = False
    rightover = False
  if lineTraceValue == 1 and leftover == False:
    hat_BeetleC0.SetPulse(1, 120)
    wait_ms(50)
    hat_BeetleC0.SetPulse(1, 0)
    wait_ms(100)
  else:
    leftover = True
    wait_ms(150)
  lineTraceValue = pinin.value()
  display.printDisp(str(lineTraceValue))
  if lineTraceValue == 1:
    leftover = False
    rightover = False
  if lineTraceValue == 1 and rightover == False:
    hat_BeetleC0.SetPulse(0, 120)
    wait_ms(50)
    hat_BeetleC0.SetPulse(0, 0)
    wait_ms(100)
  else:
    leftover = True
    wait_ms(150)