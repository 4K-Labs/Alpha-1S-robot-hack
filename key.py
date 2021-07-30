import keyboard
import lib
address = "88:1B:99:09:E8:96"
lib.connect(address)
keys = { 'w':lib.moveForward, 's':lib.moveBackwardFast , 'a':lib.moveLeft , 'd':lib.moveRightFast , 'v':lib.turnLeft2 , 'm':lib.turnRight2 , 'h':lib.defaultPose}
while True:
    key = keyboard.read_key()
    if keys.get(key):
        keys.get(key)()
        
