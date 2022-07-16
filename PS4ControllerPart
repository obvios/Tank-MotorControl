from pyPS4Controller.controller import Controller

class TestController(Controller):
  def __ini__(self, **kwargs):
    Controller.__init__(self,**kwargs)

controller = TestController(interface="/dev/input/js0",connecting_using_ds4drv=False)
controller.listen()

