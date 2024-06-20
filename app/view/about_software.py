from app.lib import QtCore, QtWidgets, QtGui
from app.lib.globals import app_name, version_name, IMAGES_DIR
from app.ui import about_software_ui, disclaim_ui


class AboutSoftware(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = about_software_ui.Ui_AboutSoftware()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.ui.appIcon.setPixmap(QtGui.QPixmap(IMAGES_DIR / 'app-full.png'))
        self.ui.appName.setText(app_name)
        self.ui.appVersionName.setText(version_name)

    def connect_ui_events(self):
        self.ui.disclaim.mousePressEvent = self.handle_disclaim_click

    def handle_disclaim_click(self, event):
        disclaim_dialog = QtWidgets.QDialog(parent=self)
        ui = disclaim_ui.Ui_DisclaimView()
        ui.setupUi(disclaim_dialog)
        disclaim_content = ui.label.text()
        ui.label.setText(disclaim_content.format(appName=app_name))
        disclaim_dialog.exec()
