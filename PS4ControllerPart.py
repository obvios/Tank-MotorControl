from pyPS4Controller.controller import Controller

class PS4ControllerPart(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.x_pressed = False
        self.square_pressed = False
        self.left_arrow_pressed = False
        self.right_arrow_pressed = False

    def on_x_press(self):
        print("on_x_press")
        self.x_pressed = True

    def on_x_release(self):
        print("on_x_release")
        self.x_pressed = False

    def on_square_press(self):
        print("on_square_press")
        self.square_pressed = True
        
    def on_square_release(self):
        print("on_square_release")
        self.square_pressed = False

    def on_left_arrow_press(self):
        print("on_left_arrow_press")
        self.left_arrow_pressed = True

    def on_right_arrow_press(self):
        print("on_right_arrow_press")
        self.right_arrow_pressed = True

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")
        self.left_arrow_pressed = False
        self.right_arrow_pressed = False

    def update(self):
        print("starting to listen to ps4 controller events")
        self.listen() 
        
    def run_threaded(self):
        """:return: x_pressed, square_pressed, left_arrow_pressed, right_arrow_pressed"""
        print("PS4ControllerPart.run_threaded")
        return self.x_pressed, self.square_pressed, self.left_arrow_pressed, self.right_arrow_pressed


# ONLY FOR TESTING
if __name__ == "__main__":
    controller = PS4ControllerPart(interface="/dev/input/js0",connecting_using_ds4drv=False)
    controller.update()

