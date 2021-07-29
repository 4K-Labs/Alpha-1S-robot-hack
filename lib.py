import bluetooth
import time
from os import system 


sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
def connect(address):
    global sock
    print('Connecting...')
    port = 6
    sock.connect((address, port))
    print('Connected')

def disconnect():
    global sock
    sock.close()
    
def sendAction(action_name):
    global sock
    action_name = bytes(action_name,'ascii')
    action_name = [(x).to_bytes(1, byteorder='big') for x in action_name]
    msg = create_message(b'\x03',action_name)
    sock.send(msg)
    ### Send check battery
    msg = battery_message()
    sock.send(msg)
    system("clear")
    # display status
    checkStatus()
    
def create_message(command,parameters):
    header = b'\xFB\xBF'
    end = b'\xED'
    parameter = b''.join(parameters)
    length = bytes([len(parameters)+5])
    data = [command, length]
    data.extend(parameters)
    total=0
    for x in data:
        total += ord(x)
        total %= 256  
    check = bytes([total])
    return header+length+command+parameter+check+end

#############################################################
def checkStatus():
    recived = sock.recv(1024) # Buffer size
    print("STATUS:")
    # refer to the data sheet
    if b'\x03\x00' in recived:
        print("Send action: Success")
    if b'\x03\x01' in recived:
        print("Send action: failure-empty file name")
    if b'\x03\x02' in recived:
        print("Battery capacity: low")
    if b'\x03\x03' in recived:
        print("Send action: error")
    if b'\x18' in recived:
        index = recived.index(b'\x18')
        if b'\x01' in recived:
            print(f"Battery capacity: charging, {recived[index + 4]}%")    
        else:
            print(f"Battery capacity: {recived[index + 4]}%")
   


def battery_message():
#check for battery status
    header = b'\xFB\xBF'
    end = b'\xED'
    length = bytes([len(b'\x00')+5])
    data = [b'\x18', length]
    param = b'\x00'
    data.extend([param])
    total = 0
    for x in data:
        total += ord(x)
        total %= 256  
    check = bytes([total])
    
    return header+length+b'\x18'+b'\x00'+check+end
   
############################################################### 



#gamepad movements

def moveBackward():
    sendAction('Move back')
    
def DefaultFoot():
    sendAction('action//gamepad//Default foot1.hts')

def FallBackwardRise():
    sendAction('action//gamepad//Fall backward rise1.hts')

def FallForwardRise():
    sendAction('action//gamepad//Fall forward rise1.hts')
    
def moveForward():
    sendAction('action//gamepad//Forward2')
    
def leftSlideTackle():
    sendAction('action//gamepad//Left slide tackle1.hts')
    
def moveLeftward():
    sendAction('action//gamepad//leftward1.hts')

def rightSlideTackle():
    sendAction('action//gamepad//right slide tackle1.hts')
     
def moveRightward():
    sendAction('action//gamepad//rightward1.hts')
    
def shootLeft():
    sendAction('action//gamepad//Shoot left1.hts')
    
def shootRight():
    sendAction('action//gamepad//Shoot right1.hts')

def turnLeft():
    sendAction('action//gamepad//turnLeft1.hts')

def turnRight():
    sendAction('action//gamepad//turnright1.hts')  
    
   
   
    
#actions

def aSecretLife():
    sendAction('a secret life') 
    
def defaultPose():
    sendAction('Default') 
    
def getUp():
    sendAction('get up')
    
def leftPunch():
    sendAction('Left punch')

def moveBackward():
    sendAction('Move Back')

def moveLeftward():
    sendAction('Move Leftward')    
    
def moveRightward():
    sendAction('move rightward')
    
def presentation():
    sendAction('presentation extended edition')    
    
def presentation2():
    sendAction('presentation')

def pushUp():
    sendAction('push-up')

def rightPunch():
    sendAction('Right punch')

def dance():
    sendAction('rotan-give them')

def sport():
    sendAction('sirius')
    
def dance2():
    sendAction('sweet and sour')
    
def soldier():
    sendAction('trojan horse')
    
def turnLeft2():
    sendAction('turn left')
    
def turnRight2():
    sendAction('turn right')
    
def dance3():
    sendAction('we are taking off')
 
 
    
#walk movements
  
def moveBackwardFast():
    sendAction('action/walk/back_fast.hts')  
    
def moveBackward():
    sendAction('action/walk/back_mid.hts')
    
def moveBackwardSlow():
    sendAction('action/walk/back_slow.hts')
    
def courseFailer():
    sendAction('action/walk/course_failer.hts')
    
def courseSuccess():
    sendAction('action/walk/course_success.hts')  
    
def moveForwardFast():
    sendAction('action/walk/forward_fast.hts')   
    
def moveForward():
    sendAction('action/walk/forward_mid.hts') 
    
def moveForwardSlow():
    sendAction('action/walk/forward_slow.hts')
    
def moveLeftFast():
    sendAction('action/walk/left_fast.hts')
    
def moveLeft():
    sendAction('action/walk/left_mid.hts')
    
def moveLeftSlow():
    sendAction('action/walk/left_slow.hts')
    
def moveRightFast():
    sendAction('action/walk/Right_fast.hts')
    
def moveRight():
    sendAction('action/walk/Right_mid.hts')
    
def moveRightSlow():
    sendAction('action/walk/Right_slow.hts')
    
def turnLeft3():
    sendAction('action/walk/turn_left.hts')
    
def turnRight3():
    sendAction('action/walk/turn_right.hts')