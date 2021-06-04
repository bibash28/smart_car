import MFRC522
import RPi.GPIO as GPIO

class SimpleMFRC522:

  def __init__(self):
    self.READER = MFRC522.MFRC522()

  def read(self):
    status, TagType = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
    if status != self.READER.MI_OK:
        return None

    status, uid = self.READER.MFRC522_Anticoll()
    if status != self.READER.MI_OK:
        return None


    id = self.uid_to_num(uid)
    return id


  def uid_to_num(self, uid):
      n = 0
      for i in range(0, 5):
          n = n * 256 + uid[i]
      return n
