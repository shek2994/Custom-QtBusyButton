from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea, QLabel, QVBoxLayout, QHBoxLayout
import time
class WorkerThread(QThread):
    finished = pyqtSignal()

    def run(self):
        # Simulate some long-running task
        self.sleep(3)
        self.finished.emit()
json_stylesheet = """
 QPushButton {
    color: white;
    min-width: 80px;
    max-width: 80px;
    min-height: 50px;
    max-height: 50px;
    border: 2px solid #555;
    border-radius: 30px;
    border-style: outset;
    background: qradialgradient(
        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #888
        );
    padding: 5px;
    background:navy;

    }
    QPushButton:hover{
    color:white;
    background: qradialgradient(
        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #bbb
        );
    }
    """
class BusyButton(QPushButton):
    def __init__(self, *args, use_local_worker=True,  **kwargs):
        super().__init__(*args, **kwargs)
        self.use_local_worker = use_local_worker
        print(args, kwargs, use_local_worker)
        self.setCheckable(True)
        self.toggled.connect(self.onToggled)

        self.movie = QMovie('wait.gif')  # Replace 'busy.gif' with your animated GIF path
        self.movie.setScaledSize(self.size())
        self.movie.frameChanged.connect(self.updateButtonIcon)
        self.setStyleSheet(json_stylesheet)

    def updateButtonIcon(self, frame):
        pixmap = self.movie.currentPixmap()
        icon = QIcon(pixmap)
        self.setIcon(icon)

    def onToggled(self, checked):
        print("BusyButton-OnToggle" ,checked)
        if checked:
            self.setEnabled(False)
            self.movie.start()
            self.updateButtonIcon(1)

            if self.use_local_worker:
                thread = WorkerThread()
                thread.finished.connect(self.onThreadFinished)                
                thread.start()
                time.sleep(0.1)
        else:
            print("2.EE")
            self.setEnabled(True)
            self.movie.stop()
            self.setIcon(QIcon())

    def onThreadFinished(self):
        print("1.BB, BusyButton-onThreadFinished")
        self.setChecked(False)
        print("3.AA")

def start():
    print("enter")

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from enum import Enum

class ButtonState(Enum):
    START = 0
    PAUSE = 1
    RESUME = 2

class ControlButton(QPushButton):
    def __init__(self, *args, cb=None,**kwargs):
        super().__init__(*args, **kwargs)
        self.state = ButtonState.START
        self.error_occurred = False
        self.setText("START")
        self.clicked.connect(cb)
        # self.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.state == ButtonState.START:
            # Simulate error in starting the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error in starting the process
                print("Error occurred. Process could not be started.")
                return

            # Start the process
            print("Process started.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")
        elif self.state == ButtonState.PAUSE:
            # Pause the process
            print("Process paused.")
            # Simulating an error in the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error, retain PAUSE state
                print("Error occurred. Process remains paused.")
            else:
                self.state = ButtonState.RESUME
                self.setText("RESUME")
        elif self.state == ButtonState.RESUME:
            # Resume the process
            print("Process resumed.")
            # Simulating an error in the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error, retain RESUME state
                print("Error occurred. Process remains resumed.")
            else:
                self.state = ButtonState.PAUSE
                self.setText("PAUSE")

    def onSuccess(self):
        if self.state == ButtonState.START:
            # Start the process
            print("Process started.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")
        elif self.state == ButtonState.PAUSE:
            # Pause the process
            print("Process paused.")
            self.state = ButtonState.RESUME
            self.setText("RESUME")
        elif self.state == ButtonState.RESUME:
            # Resume the process
            print("Process resumed.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")

class ControlBusyButton(BusyButton):
    def __init__(self, *args, cb=None,**kwargs):
        super().__init__(*args, **kwargs)
        self.state = ButtonState.START
        self.error_occurred = False
        # self.setText("TEST")
        self.clicked.connect(cb)
        # self.clicked.connect(self.onClicked)

    def onClicked(self):
        print("ControlBusyButton-onClicked")
        if self.state == ButtonState.START:
            # Simulate error in starting the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error in starting the process
                print("Error occurred. Process could not be started.")
                return

            # Start the process
            print("Process started.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")
        elif self.state == ButtonState.PAUSE:
            # Pause the process
            print("Process paused.")
            # Simulating an error in the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error, retain PAUSE state
                print("Error occurred. Process remains paused.")
            else:
                self.state = ButtonState.RESUME
                self.setText("RESUME")
        elif self.state == ButtonState.RESUME:
            # Resume the process
            print("Process resumed.")
            # Simulating an error in the process
            # error_occurred = True
            if self.error_occurred:
                # Handle error, retain RESUME state
                print("Error occurred. Process remains resumed.")
            else:
                self.state = ButtonState.PAUSE
                self.setText("PAUSE")
    def onSuccess(self):
        print("ControlBusyButton-onSuccess emitted")
        if self.state == ButtonState.START:
            # Start the process
            print("Process started.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")
        elif self.state == ButtonState.PAUSE:
            # Pause the process
            print("Process paused.")
            self.state = ButtonState.RESUME
            self.setText("RESUME")
        elif self.state == ButtonState.RESUME:
            # Resume the process
            print("Process resumed.")
            self.state = ButtonState.PAUSE
            self.setText("PAUSE")
    def onStop(self):
        self.state = ButtonState.START
        self.setText("START")


from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
class ConfirmationDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        #Block/hide the Title widget in popup windows
        self.setWindowTitle("Confirmation")
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        
        # Create the message label
        label = QLabel(message)
        label.setStyleSheet("background-color: rgb(170, 170, 255);")

        # Create the button box with OK and CANCEL buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_box.setStyleSheet(json_stylesheet)

        # Create the main layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button_box)
        
        self.setLayout(layout)

    def paintEvent(self, event):
        # Create a QPainter
        painter = QPainter(self)
        # Set the desired background color
        painter.fillRect(self.rect(), QColor(170, 170, 255)) 

    def confirm(self):
        result = self.exec_()
        return result == QDialog.Accepted


class TextAppender():
    def __init__(self):
        self.textBuffer = ''
        self.VBarObj = None
        self.ScrollObj = None
        pass
    def appendText(self, text):
        newText = self.textBuffer + "\n" + text
        if(len(newText) > 8000):
            newTextList = newText.split('\n')
            while(len(newText) >= 8000):
                newTextList.pop(0)
                newText = '\n'.join(newTextList)
        self.textBuffer = newText
    def text(self):
        return self.textBuffer
    def moveScrollBarToBottom(self, min, max):
        self.ScrollObj.verticalScrollBar().setValue(max)
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    widget = QWidget()
    layout = QVBoxLayout(widget)

    busyButton = BusyButton('Busy Button')
    layout.addWidget(busyButton)
    busyButton.clicked.connect(start)

    widget.show()

    sys.exit(app.exec_())
