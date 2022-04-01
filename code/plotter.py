#import time
#import importlib
#from in_out import grbl as transport
import utilities.constants as constants
#importlib.reload(grbl)

class Plotter:
    def __init__(self, transport):
        self.transport = transport
    
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def reset(self):
        # NEMA17 200 steps/rev, 2 microsteps, spool dia = 17.0 mm
        diameter = 17.0
        steps_per_rev = 200
        microsteps = 2
        steps_per_mm = (steps_per_rev * microsteps) / (diameter * constants.PI)
        #print(f'Steps per mm: {steps_per_mm}')
        
        self.transport.reset()
        self.transport.set_speed_accel('X', 2000, 2000)
        self.transport.set_speed_accel('Y', 2000, 2000)
        self.transport.send_gcode(f'$100={steps_per_mm}')
        self.transport.send_gcode(f'$101={steps_per_mm}')
        self.transport.send_gcode('$23=3')   # reverse direction for X/Y
        self.transport.send_gcode('$27=10')   # short pull-off of home
        self.transport.home()

    # def plot(self, x, y, speed):
    #     self.grbl.set_speed(speed)
    #     self.grbl.move_to(x, y)
    #     self.grbl.wait_for_idle()
    #     self.grbl.set_speed(constants.DEFAULT_SPEED)
    #     self.grbl.set_feed(constants.DEFAULT_FEED)

    # def plot_line(self, x, y, speed):
    #     self.grbl.set_speed(speed)
    #     self.grbl.move_to(x, y)
    #     self.grbl.wait_for_idle()
    #     self.grbl.set_speed(constants.DEFAULT_SPEED)
    #     self.grbl.set_feed(constants.DEFAULT_FEED)

    # def plot_arc(self, x, y, z, i, j, k, speed, feed, spindle_speed, spindle_dir):
    #     self.grbl
