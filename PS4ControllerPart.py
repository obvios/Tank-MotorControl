from pyPS4Controller.controller import Controller

class PS4ControllerPart(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("on_x_press")


class TestController(Controller):
  def __init__(self, **kwargs):
    Controller.__init__(self,**kwargs)

controller = TestController(interface="/dev/input/js0",connecting_using_ds4drv=False)
controller.listen()

