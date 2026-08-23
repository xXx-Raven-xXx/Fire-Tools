import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QPalette, QColor, QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QWidget, QGridLayout, QListWidget, QLabel, QComboBox, QSizePolicy

# Platform Variables
version = "26.08"

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Fire Tools: QT Edition v{version}")
        self.setMinimumSize(QSize(1000, 610))

        layout = QGridLayout()
        layout.setContentsMargins(30,30,30,30)
        layout.setHorizontalSpacing(80)

        # Left Column
        label1 = QLabel("Debloat")
        label1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(label1, 0,0)

        debloat = QPushButton("Debloat")
        layout.addWidget(debloat, 1, 0)

        undo = QPushButton("Undo")
        layout.addWidget(undo, 2, 0)

        edit = QPushButton("Edit")
        layout.addWidget(edit, 3, 0)

        label2 = QLabel("Custom DNS")
        label2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(label2, 4, 0)

        customdns = QComboBox()
        customdns.addItems(["Select or Enter DNS Server", "one.one.one.one", "dns.quad9.net", "dns.adguard.com", "adblock.dns.mullvad.net", "family.cloudflare-dns.com", "family.adguard-dns.com", "Disable"])
        customdns.setEditable(True)
        layout.addWidget(customdns, 5, 0)

        setdns = QPushButton("Set Selected DNS")
        layout.addWidget(setdns, 6, 0)

        # Center Column
        label3 = QLabel("Utilities")
        label3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(label3, 0, 1)

        googleservices = QPushButton("Install Google Services")
        layout.addWidget(googleservices, 1, 1)

        batchinstall = QPushButton("Batch Install")
        layout.addWidget(batchinstall, 2, 1)

        disableota = QPushButton("Disable OTA")
        layout.addWidget(disableota, 3, 1)

        label4 = QLabel("Custom Launcher")
        label4.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(label4, 4, 1)

        customlauncher = QComboBox()
        customlauncher.addItems(["Select Launcher", "Nova Launcher", "Lawnchair", "Hyperion", "Local .apk"])
        customlauncher.setEditable(True)
        layout.addWidget(customlauncher, 5, 1)

        setlauncher = QPushButton("Install Selected Launcher")
        layout.addWidget(setlauncher, 6, 1)


        # Right Column
        label5 = QLabel("Packages")
        label5.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label5.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(label5, 0, 2)

        packageselector = QListWidget()
        packageselector.addItems(["com.amazon.firelauncher", "com.amazon.photos", "com.amazon.sharingservice.android.client.proxy"])
        packageselector.setMaximumWidth(260)
        layout.addWidget(packageselector, 1, 2, 4, 1)

        packageoption = QComboBox()
        packageoption.addItems(["Enable", "Disable", "Extract"])
        packageoption.setCurrentIndex(1)
        layout.addWidget(packageoption, 5, 2)

        selected = QPushButton("Disable Selected")
        layout.addWidget(selected, 6, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

if __name__ == "__main__":
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Dark)
    window = MainWindow()
    sys.exit(app.exec())