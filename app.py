from os import getpid, kill
from PyQt5.QtWidgets import QApplication, QMenu, QAction, QSystemTrayIcon
from PyQt5.QtGui import QIcon

from shortcuts import listener
from threading import Thread
from ui import ShortcutWidget

class App:
    def __init__(self):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)
        
        self.ui = ShortcutWidget()
        self.listener_thread = Thread(target=listener, daemon=True, args=(self.shortcut_app, self.ui))
        self.init_tray()
        self.run()

    def run(self):
        while True:
            print("Running")
            self.invoke_ui()
    
    def init_tray(self):
        self.tray_menu = QMenu()

        self.action_exit = QAction("Exit")
        self.action_exit.triggered.connect(App.exit)
        self.tray_menu.addAction(self.action_exit)

        
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("logo_small.jpg"))
        self.tray.setVisible(True)
        self.tray.setToolTip("PyShortcuts")
        self.tray.setContextMenu(self.tray_menu)
        self.tray.activated.connect(lambda reason: self.shortcut_app())

    def invoke_ui(self):
        self.listener_thread.start()
        print("Hello")
        self.ui.show()
        self.ui.hide()
        while True:
            print("executed!!")
            self.app.exec_()

    def shortcut_app(self):
        print("Window Open")
        self.ui.show()

    def exit(self):
        print("Go fuck yourself!!")
        kill(getpid(), 3)
        exit(0)

if __name__ == "__main__":
    App()
