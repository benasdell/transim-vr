#import statements
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.task import Task
from panda3d.core import Vec4, Vec3
from panda3d.core import ClockObject

#program start
class vrTest(ShowBase):
    def __init__(self):
        ShowBase.__init__(self) #class initialization

        #setting window size
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.disableMouse() #disables mouse camera movement

        #load environment model
        self.environment = loader.loadModel("models/zebrafishEnviron17_100contrast.egg")
        self.environment.reparentTo(render) #attaches environment to render environment

        self.camera.setPos(0, 0, 5) #sets model at eye-level
        self.camLens.setFov(40) #camera FOV setting, needs testing

        #TV object for displaying images in foreground
        self.tex1 = loader.loadTexture("models/VRE_autoPA_bigFish.avi")
        self.TV1 = loader.loadModel("models/zebrafishEnviron4TV3.egg")
        self.TV1.reparentTo(render)
        self.TV1.setTexture(self.tex1, 1)
        self.TV1.setH(180)
        self.TV1.setPos(0, 20.3, 0)

        # hide mouse cursor
        props = WindowProperties()
        props.setCursorHidden(True)
        self.win.requestProperties(props)

        #keymap for keyboard inputs
        self.keyMap = {
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False,
            "shoot" : False
        }

        #event listeners for keyboard inputs
        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])

        #adds camera inputs to task manager
        self.updateTask = taskMgr.add(self.update, "update")

    #updates control state based on event listeners
    def updateKeyMap(self, controlName, controlState):
        self.keyMap[controlName] = controlState
        print (controlName, "set to", controlState) #console output of key presses for debugging

    #camera movement method, would be replaced with LabView integration
    def update(self, task):
        # Get the amount of time since the last update
        dt = globalClock.getDt()
        velocity = 10 #coefficient for camera movement speed
        # applies camera inputs to camera position
        if self.keyMap["up"]:
            self.camera.setPos(self.camera.getPos() + Vec3(0, velocity * dt, 0))
        if self.keyMap["down"]:
            self.camera.setPos(self.camera.getPos() + Vec3(0, -1 * velocity * dt, 0))
        if self.keyMap["left"]:
            self.camera.setPos(self.camera.getPos() + Vec3(-1 * velocity * dt, 0, 0))
        if self.keyMap["right"]:
            self.camera.setPos(self.camera.getPos() + Vec3(velocity * dt, 0, 0))

        return task.cont
app = vrTest() #creates instance of program class
app.run() #runs program class