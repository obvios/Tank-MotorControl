from pyPS4Controller.controller import Controller

class PS4ControllerPart(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("on_x_press")

    def on_x_release(self):
        print("on_x_release")

    def on_square_press(self):
        print("on_square_press")
        
    def on_square_release(self):
        print("on_square_release")

    def on_left_arrow_press(self):
        print("on_left_arrow_press")

    def on_right_arrow_press(self):
        print("on_right_arrow_press")

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")

    def update(self):
        pass 
        
    def run_threaded(self):
        print("PS4ControllerPart.run_threaded")


# ONLY FOR TESTING
if __name__ == "__main__":
    controller = PS4ControllerPart(interface="/dev/input/js0",connecting_using_ds4drv=False)
    controller.listen()

