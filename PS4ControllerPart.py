from pyPS4Controller.controller import Controller

class PS4ControllerPart(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.throttlePressed = False
        self.reversePressed = False
        self.steeringLeft = False
        self.steeringRight = False

    def on_x_press(self):
        print("on_x_press")
        self.throttlePressed = True

    def on_x_release(self):
        print("on_x_release")
        self.throttlePressed = False

    def on_square_press(self):
        print("on_square_press")
        self.reversePressed = True
        
    def on_square_release(self):
        print("on_square_release")
        self.reversePressed = False

    def on_left_arrow_press(self):
        print("on_left_arrow_press")
        self.steeringLeft = True

    def on_right_arrow_press(self):
        print("on_right_arrow_press")
        self.steeringRight = True

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")
        self.steeringLeft = False
        self.steeringRight = False

    def update(self):
        print("starting to listen to ps4 controller events")
        self.listen() 
        
    def run_threaded(self):
        """:return: throttlePressed, reversePressed, steeringLeft, steeringRight"""
        print("PS4ControllerPart.run_threaded")
        return self.throttlePressed, self.reversePressed, self.steeringLeft, self.steering.right


# ONLY FOR TESTING
if __name__ == "__main__":
    controller = PS4ControllerPart(interface="/dev/input/js0",connecting_using_ds4drv=False)
    controller.update()

