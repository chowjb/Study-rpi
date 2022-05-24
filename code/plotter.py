import utilities.constants as constants
#import importlib
#importlib.reload(grbl)

class Plotter:
    def __init__(self, transport, capture_gcode=False):
        self.transport = transport
        if capture_gcode:
            self.transport.capture_gcode('C:\\temp\\plotting.gcode')
    
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def reset(self, speed=4000, acceleration = 4000):
        # NEMA17 200 steps/rev, 2 microsteps, spool dia = 17.0 mm
        diameter = 17.0
        steps_per_rev = 200
        microsteps = 2
        steps_per_mm = (steps_per_rev * microsteps) / (diameter * constants.PI)
        #print(f'Steps per mm: {steps_per_mm}')
        
        self.transport.reset()
        self.transport.set_speed_accel('X', speed, acceleration)
        self.transport.set_speed_accel('Y', speed, acceleration)
        self.transport.send_gcode(f'$100={steps_per_mm}')
        self.transport.send_gcode(f'$101={steps_per_mm}')
        self.transport.send_gcode('$23=1')  # reverse direction for X for home
        self.transport.send_gcode('$3=3')   # reverse direction of stepper for Y
        self.transport.send_gcode('$27=10') # short pull-off of home
        self.transport.home()
        self.transport.send_gcode('G91 Y-300')  # move to start of plot position
        self.transport.send_gcode('G10 L20 P1 X0 Y0 Z0') # set origin to 0,0,0
        # save this as the permanent home position (it in machine coordinates)
        self.transport.send_gcode('G28.1')
        # set for absolute position
        self.transport.send_gcode('$130=450') # set X max travel
        self.transport.send_gcode('$131=375') # set Y max travel
        self.transport.send_gcode('$25=1000') # set the speed seeking the limit switches
        self.transport.send_gcode('G90')

    def plot_circle(self, x_center, y_center):
        self.transport.debug = False
        self.transport.send_gcode(f'X{x_center} Y{y_center}')

    # def plot_line(self, x, y, speed):
    #     self.grbl.set_speed(speed)
    #     self.grbl.move_to(x, y)
    #     self.grbl.wait_for_idle()
    #     self.grbl.set_speed(constants.DEFAULT_SPEED)
    #     self.grbl.set_feed(constants.DEFAULT_FEED)

    # def plot_arc(self, x, y, z, i, j, k, speed, feed, spindle_speed, spindle_dir):
    #     self.grbl
