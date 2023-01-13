import time
import threading


class Cube(threading.Thread):
    
    def __init__(self, side):
        threading.Thread.__init__(self)
        self.side = side


    def cube_volume(self):
        self.cube_volume = self.side * self.side * self.side
        print("Volume of cube is: ", self.cube_volume)
        time.sleep(4)

    def side_sum(self):
        self.side_sum = self.side * 12
        print("Sum of sides is: ", self.side_sum)
        time.sleep(2)
    
    def run(self):
        t1 = threading.Thread(target = self.cube_volume(), args= time.sleep(2))
        t2 = threading.Thread(target = self.side_sum(), args= time.sleep(0.1))
 

r1 = Cube(5)
r1.start()
r1.join()

r2 = Cube(7)
r2.start()
r2.join()



