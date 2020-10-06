"""
Hello World with PySide GUI
---------------------------
Very basic GUI program based upon simple code at 
https://wiki.qt.io/Qt_for_Python
and tutorial code at
https://doc.qt.io/qtforpython/tutorials/basictutorial/widgets.html

Required to work: PySide2 availability
Install with: pip3 install PySide2
"""

import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=40><center><b>Hello World!</b></center></font>")
    label.resize(260,90)
    label.show()
    sys.exit(app.exec_())