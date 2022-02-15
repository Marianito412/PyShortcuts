from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QDesktopWidget, QMessageBox
from PyQt5 import QtCore
# Only needed for access to command line arguments
import sys
        
class Popup(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.NoDropShadowWindowHint)
        #self.setIcon(QMessageBox.Information)
        self.setText("Hello worldadsfasdfasdfasdfasdfasdf")
        self.resize(400, 120)
        print("Done")

class ShortcutWidget(QWidget):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icon-base
    def __init__(self, parent=None):
        # You need one (and only one) QApplication instance per application.
        # Pass in sys.argv to allow command line arguments for your app.
        # If you know you won't use command line arguments QApplication([]) works too.
        QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup | QtCore.Qt.NoDropShadowWindowHint)
        
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("QWidget {{border: #191414 ;border-radius: 10px ;background: #191414; color: #191414;}}")
        self.move(center_app())
        self.setWindowOpacity(0.9)

        self.event = None
        self.create_widgets()

    def set_event(self, event_to_exec):
        self.event = event_to_exec
        print("event changed")

    def focusInEvent(self, a0):
        print("Focused")
        return super().focusInEvent(a0)

    def focusOutEvent(self, a0):
        self.textbox.clear()
        self.hide()
        print("hidden")
        return super().focusOutEvent(a0)

    def create_widgets(self):
        self.textbox = QLineEdit(self)
        self.textbox.returnPressed.connect(self.textbox_return_pressed_handler)
        self.textbox.textChanged.connect(self.text_changed)
        self.textbox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textbox.setStyleSheet(f'''
                        QLineEdit
                        {{
                            border: 0;
                            background: #191414;
                            color: #B3B3B3;
                            font-size: 25px;
                            border-radius: 2px;
                            selection-background-color: #6f6f76;
                            padding-left: 6px;
                            padding-right: 6px;
                        }}''')
        #self.textbox.move(51, 30 + 9)
        self.textbox.setPlaceholderText("Input")
        self.textbox.resize(481, 41)
        self.textbox.installEventFilter(self)

    def text_changed(self):
        pass

    def textbox_return_pressed_handler(self):
        print(self.textbox.text())
        self.hide()
        self.event(self.textbox.text())


def center_app():
    sizeObject = QDesktopWidget().screenGeometry(-1)
    height = sizeObject.height()
    coord = QDesktopWidget().availableGeometry().center()
    to_sub = QtCore.QPoint(270, height / 3)
    center = coord.__sub__(to_sub)
    return center

if __name__ == "__main__":

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    # Create a Qt widget, which will be our window.
    window = Popup()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()

