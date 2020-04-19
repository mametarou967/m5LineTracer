from m5stack import *
from m5ui import *
from uiflow import *
import machine
import hat

setScreenColor(0x111111)
hat_BeetleC0 = hat.get(hat.BEETLEC)
label0 = M5TextBox(48, 1, "Line Tracer on BeetleC", lcd.FONT_Default,0xff0378, rotate=90)
lcd.clear()
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
    M5TextBox(0, self.row * 12, str(self.row) + "_" + string)
    self.row = self.row + 1

class Sensor:
  
  def __init__(self,pinin):
    self.pinin = pinin
  
  def IsOnline(self):
    if(self.pinin.value() == 1):
      return True
    else:
      return False
      
class BeetlecController:

  def __init__(self,hatBeetle):
    self.hatBeetle = hatBeetle
    
  def moveRight(self):
    self.hatBeetle.SetPulse(0, -30)
    self.hatBeetle.SetPulse(1, 120)
    wait_ms(50)
    self.stop()
    wait_ms(100)
  
  def moveLeft(self):
    self.hatBeetle.SetPulse(0, 120)
    self.hatBeetle.SetPulse(1, -30)
    wait_ms(50)
    self.stop()
    wait_ms(100)
    
  def stop(self):
    self.hatBeetle.SetPulse(0, 0)
    self.hatBeetle.SetPulse(1, 0)

class BeetlecAutomaton:
  
  def __init__(self,beetlecController,Sensor):
    self.beetlecController = beetlecController
    self.sensor = Sensor
    self.stateWait = 0
    self.stateOnlineRightMove = 1
    self.stateOnlineLeftMove = 2
    self.stateHamidashiRight = 3
    self.stateHamidashiLeft = 4
    self.state = self.stateWait

  def raiseEvent(self):
    # èÛë‘ëJà⁄
    if self.state == self.stateWait:
      if self.sensor.IsOnline():
        self.state = self.stateOnlineRightMove
    elif self.state == self.stateOnlineRightMove:
      if self.sensor.IsOnline():
        self.state = self.stateOnlineLeftMove
      else:
        self.state = self.stateHamidashiRight
    elif self.state == self.stateOnlineLeftMove:
      if self.sensor.IsOnline():
        self.state = self.stateOnlineRightMove
      else:
        self.state = self.stateHamidashiLeft
    elif self.state == self.stateHamidashiRight:
      if self.sensor.IsOnline():
        self.state = self.stateOnlineLeftMove
    elif self.state == self.stateHamidashiLeft:
      if self.sensor.IsOnline():
        self.state = self.stateOnlineRightMove
    
    self.action()
  
  def action(self):
    if self.state == self.stateOnlineRightMove:
      self.beetlecController.moveRight()
    elif self.state == self.stateOnlineLeftMove:
      self.beetlecController.moveLeft()
    elif self.state == self.stateHamidashiRight:
      self.beetlecController.moveLeft()
    elif self.state == self.stateHamidashiLeft:
      self.beetlecController.moveRight()
    
display = Display()
sensor = Sensor(pinin)
beetlecController = BeetlecController(hat_BeetleC0)
beetlecAutomaton = BeetlecAutomaton(beetlecController,sensor)

while True:
  display.printDisp(str(sensor.IsOnline()))
  beetlecAutomaton.raiseEvent()
  wait_ms(1000)