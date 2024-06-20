from app.lib import QtWidgets, QtCore
from app.lib.globals import COMMON_CHARS

"""
COMMON_CHARS = {
    '换行符': '\\n',
    '缩进': '\\t',
    '4个空格': ' ' * 4,
    '8个空格': ' ' * 8,
}
"""


class CharPicker(QtWidgets.QDialog):
    selectedSignal = QtCore.Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.chars_group = QtWidgets.QButtonGroup()
        main_layout = QtWidgets.QVBoxLayout()
        grid_layout = QtWidgets.QGridLayout()

        row, col = 0, 0
        for char_name, char_value in COMMON_CHARS.items():
            button = QtWidgets.QRadioButton(char_name)
            button.setToolTip(char_value)
            self.chars_group.addButton(button)
            grid_layout.addWidget(button, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        main_layout.addLayout(grid_layout)
        buttons_layout = QtWidgets.QHBoxLayout()
        cancel_button = QtWidgets.QPushButton("取消")
        cancel_button.clicked.connect(self.reject)
        buttons_layout.addStretch()
        buttons_layout.addWidget(cancel_button)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def connect_ui_events(self):
        self.chars_group.buttonClicked.connect(self.accept)

    def accept(self):
        selected_char = self.chars_group.checkedButton().text()
        self.selectedSignal.emit(COMMON_CHARS.get(selected_char, selected_char))
        super().accept()
