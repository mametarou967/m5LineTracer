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

while True:
  lineTraceValue = pinin.value()
  label1 = M5TextBox(0, deltaY * 12, "hello" + str(deltaY) + "_" + str(lineTraceValue))
  deltaY = deltaY + 1
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
  label1 = M5TextBox(0, deltaY * 12, "hello" + str(deltaY) + "_" + str(lineTraceValue))
  deltaY = deltaY + 1
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
  if deltaY >= 13:
    lcd.clear()
    deltaY = 0