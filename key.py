import keyboard
import lib
address = "88:1B:99:06:d1:54"
lib.connect(address)
keys = { 'w':lib.moveForward, 's':lib.moveBackwardFast , 'a':lib.moveLeftFast , 'd':lib.moveRightFast , 'v':lib.turnLeft2 , 'm':lib.turnRight2 , 'h':lib.defaultPose}
while True:
        key = keyboard.read_key()
        print(key)
        try:
            if keys.get(key):
                keys.get(key)()
        except:
            pass
         
        
