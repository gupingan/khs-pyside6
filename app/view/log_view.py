from app.lib import QtCore, QtGui, QtWidgets
from app.utils.time import get_current_datetime, format_datetime

LEVELS = {
    'NORMAL': '常规',
    'SUCCESS': '成功',
    'FAILURE': '失败',
    'WARNING': '警告',
    'OTHER': '其它',
    'DEBUG': '调试',
    'IMPORTANT': '重要',
}


class LogView(QtWidgets.QTextBrowser):
    receive = QtCore.Signal(str, str)

    def __init__(self, unit=None, parent=None):
        super().__init__(parent=parent)
        self.unit = unit
        self.unit.sendLog.connect(self.append_log_entry)
        self.receive.connect(self.append_log_entry)
        self.setReadOnly(True)
        self.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.document().setDefaultStyleSheet("""
            .NORMAL {color: black;}
            .WARNING {color: orange;}
            .FAILURE {color: red;}
            .SUCCESS {color: green;}
            .DEBUG {color: blue;}
            .IMPORTANT {color: blue;}
        """)
        self.before_max = self.verticalScrollBar().maximum()
        self.after_max = self.verticalScrollBar().maximum()
        self.verticalScrollBar().rangeChanged.connect(self.handle_scrollbar_range_change)
        self.setOpenExternalLinks(True)
        self.pain_logs = []

    def handle_scrollbar_range_change(self, min_val, max_val):
        current = self.verticalScrollBar().value()
        if self.before_max <= current <= self.after_max:
            self.verticalScrollBar().setValue(max_val)
        else:
            self.verticalScrollBar().setValue(current)

    def append_log_entry(self, text: str = '', level: str = 'EMPTY'):
        self.before_max = self.verticalScrollBar().maximum()
        if level == 'EMPTY':
            log_entry = '<br>'
        else:
            current_datetime = get_current_datetime()
            formatted_datetime = format_datetime(current_datetime)
            level_name = LEVELS.get(level, 'OTHER')
            self.pain_logs.append(f'{current_datetime} {level_name}: {text}')
            log_entry = f'<span class="{level}">[{formatted_datetime}] {level_name}: </span>{text}<br>'

        cursor = self.textCursor()
        cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        cursor.insertHtml(log_entry)

        self.after_max = self.verticalScrollBar().maximum()

    def clear(self):
        self.pain_logs.clear()
        super().clear()
