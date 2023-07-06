from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import time
class WorkerThread(QThread):
    finished = pyqtSignal()

    def run(self):
        # Simulate some long-running task
        self.sleep(3)
        self.finished.emit()

class BusyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCheckable(True)
        self.toggled.connect(self.onToggled)

        self.movie = QMovie('wait.gif')  # Replace 'busy.gif' with your animated GIF path
        self.movie.setScaledSize(self.size())
        self.movie.frameChanged.connect(self.updateButtonIcon)

    def updateButtonIcon(self, frame):
        pixmap = self.movie.currentPixmap()
        icon = QIcon(pixmap)
        self.setIcon(icon)

    def onToggled(self, checked):
        if checked:
            self.setEnabled(False)
            self.movie.start()
            self.updateButtonIcon(1)

            thread = WorkerThread()
            thread.finished.connect(self.onThreadFinished)
            
            thread.start()
            time.sleep(0.1)
        else:
            self.setEnabled(True)
            self.movie.stop()
            self.setIcon(QIcon())

    def onThreadFinished(self):
        self.setChecked(False)

def start():
    print("enter")

def main()
    app = QApplication(sys.argv)

    widget = QWidget()
    layout = QVBoxLayout(widget)

    busyButton = BusyButton('Busy Button')
    layout.addWidget(busyButton)
    busyButton.clicked.connect(start)

    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    import sys
    main()
