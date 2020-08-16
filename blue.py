from subprocess import run
from time import sleep
import rumps

class BlueApp(rumps.App):
    def __init__(self):
        super(BlueApp, self).__init__('BluePy', icon="bt.png")
        self.menu = ["Restart"]

    @rumps.clicked("Restart")
    def restart(self, _):
        process = run("/usr/local/bin/blueutil -p 0", shell=True)
        sleep(2)
        run("/usr/local/bin/blueutil -p 1", shell=True)

BlueApp().run()
