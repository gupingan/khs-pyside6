from loguru import logger
from app.lib import QtWidgets, QtCore
from app.lib.core import Config, ConfigCenter, TomlBase
from app.ui import edit_config_ui, obscuror_help_ui
from app.view import edit_comment


class EditConfig(QtWidgets.QDialog):
    saved = QtCore.Signal(Config)

    SPINBOX_MIN = [0, 0, 1, 0.00]
    SPINBOX_MAX = [9, 9, 100, 1.00]

    def __init__(self, parent=None, config: Config = None, edit_type: str = 'new'):
        """
        编辑配置
        :param parent: qt 父类
        :param config: Config 对象
        :param edit_type: 编辑类型：new/template/exist/copy
        """
        super().__init__(parent=parent)
        self.ui = edit_config_ui.Ui_EditConfig()
        self.ui.setupUi(self)
        self.edit_type = edit_type
        self.config = config or Config('非正常情况下的配置模板')
        if self.edit_type == 'new':
            self.config = TomlBase.template.copy()
        elif self.edit_type == 'template':
            self.config = TomlBase.template
        self.build_interface()
        self.connect_ui_events()
        self.view_from_config()

    def build_interface(self):
        self.collection_type_group = QtWidgets.QButtonGroup()
        self.collection_type_group.addButton(self.ui.radioButton_1, 1)
        self.collection_type_group.addButton(self.ui.radioButton_2, 2)

        if self.edit_type == 'new':
            self.setWindowTitle('添加配置')
        elif self.edit_type == 'template':
            self.ui.groupBox_1.setVisible(False)
            self.setWindowTitle('编辑配置模板')
        elif self.edit_type == 'exist':
            self.setWindowTitle('编辑配置')
        elif self.edit_type == 'copy':
            self.setWindowTitle('编辑配置(仅影响当前单元相对应阶段的配置)')
            self.ui.groupBox_1.setVisible(False)

        self.set_spin_boxes_limits()

    def set_spin_boxes_limits(self):
        """
        设置 spinbox 和 double_spinbox 控件的边界范围
        :return:
        """
        if len(self.SPINBOX_MIN) != len(self.SPINBOX_MAX):
            raise ValueError("SPINBOX_MIN and SPINBOX_MAX must have the same length")

        spin_boxes = [self.ui.uncommon_char_count_sb, self.ui.retry_count_sb, self.ui.retry_interval_ds,
                      self.ui.similarity_lower_limit_dsb]

        for spinbox, min_value, max_value in zip(spin_boxes, self.SPINBOX_MIN, self.SPINBOX_MAX):
            spinbox.setMinimum(min_value)
            spinbox.setMaximum(max_value)

    def connect_ui_events(self):
        """
        连接 UI 控件的信号与槽函数
        :return:
        """
        self.ui.smart_title_btn.clicked.connect(self.handle_smart_title_btn_click)
        self.collection_type_group.buttonClicked.connect(self.handle_toggle_collect_radio_click)
        self.ui.edit_comment_btn.clicked.connect(self.handle_edit_comment_click)
        self.ui.check_block_chk.toggled.connect(self.handle_check_block_toggle)
        self.ui.uncommon_char_help_btn.clicked.connect(self.display_obscuror_help_dialog)
        self.ui.save_btn.clicked.connect(self.handle_save_btn_click)
        self.ui.cancel_btn.clicked.connect(self.close)

    @staticmethod
    def set_combobox_item(combobox: QtWidgets.QComboBox, item: str):
        items = [combobox.itemText(i) for i in range(combobox.count())]
        try:
            item_index = items.index(item.strip())
        except (ValueError, IndexError):
            item_index = 0
        combobox.setCurrentIndex(item_index)
        return item_index

    def view_from_config(self):
        """
        将导入的 Config 实例数据加载到当前界面
        :return:
        """
        # 配置信息
        self.ui.config_name_edit.setText(self.config.name if self.edit_type != 'new' else '基于模板构建的全新配置')
        self.ui.config_id_label.setText(self.config.id)
        # 采集方式
        collect_type_id = self.config.collect_type if 1 <= self.config.collect_type <= 2 else 1
        self.collection_type_group.button(collect_type_id).setChecked(True)
        # 在线搜索
        self.ui.search_edit.setText('|'.join(self.config.keywords))
        self.set_combobox_item(self.ui.note_type_cb, self.config.note_type)
        self.set_combobox_item(self.ui.sort_method_cb, self.config.sort_method)
        self.ui.similarity_filter_chk.setChecked(self.config.is_similarity_filter)
        self.ui.similarity_lower_limit_dsb.setValue(self.config.similarity_lower_limit)
        self.ui.similarity_lower_limit_dsb.setToolTip('推荐0.10~0.20')
        self.ui.similarity_keyword_le.setText('|'.join(self.config.similarity_keywords))
        # 评论设置
        self.ui.comment_chk.setChecked(self.config.is_comment)
        self.ui.fav_no_comment_chk.setChecked(self.config.is_fav_no_comment)
        self.ui.comment_fav_chk.setChecked(self.config.is_comment_fav)
        self.set_combobox_item(self.ui.uncommon_char_mode_cb, self.config.uncommon_char_mode)
        self.comments = self.config.comments  # 评论列表
        uncommon_char_count = self.config.uncommon_char_count
        if uncommon_char_count > self.SPINBOX_MAX[0]:
            uncommon_char_count = self.SPINBOX_MAX[0]
        elif uncommon_char_count < self.SPINBOX_MIN[0]:
            uncommon_char_count = self.SPINBOX_MIN[0]
        self.ui.uncommon_char_count_sb.setValue(uncommon_char_count)
        # 屏蔽参数
        self.ui.linked_check_chk.setChecked(self.config.is_linked_check)
        self.ui.skip_over_comment_chk.setChecked(self.config.is_skip_over_comment)
        self.ui.comment_threshold_sb.setValue(self.config.comment_threshold)
        self.ui.overall_block_stop_chk.setChecked(self.config.is_overall_block_stop)
        self.ui.overall_block_threshold_sb.setValue(self.config.overall_block_threshold)
        self.ui.consecutive_block_stop_chk.setChecked(self.config.is_consecutive_block_stop)
        self.ui.consecutive_block_threshold_sb.setValue(self.config.consecutive_block_threshold)
        self.ui.check_block_chk.setChecked(self.config.is_check_block)
        self.handle_check_block_toggle(self.config.is_check_block)
        self.ui.retry_after_block_chk.setChecked(self.config.is_retry_after_block)
        self.ui.random_comment_chk.setChecked(self.config.is_retry_comment_random)
        retry_count = self.config.retry_count
        if retry_count > self.SPINBOX_MAX[1]:
            retry_count = self.SPINBOX_MAX[1]
        elif retry_count < self.SPINBOX_MIN[1]:
            retry_count = self.SPINBOX_MIN[1]
        self.ui.retry_count_sb.setValue(retry_count)
        retry_interval = self.config.retry_interval
        if retry_interval > self.SPINBOX_MAX[2]:
            retry_interval = self.SPINBOX_MAX[2]
        elif retry_interval < self.SPINBOX_MIN[2]:
            retry_interval = self.SPINBOX_MIN[2]
        self.ui.retry_interval_ds.setValue(retry_interval)

        self.handle_toggle_collect_radio_click(self.collection_type_group.button(collect_type_id))

    def handle_smart_title_btn_click(self):
        """
        处理智能标题按钮的点击事件
        功能：根据配置描述结合术语底板设置新的标题
        :return:
        """
        select_collect_id = self.collection_type_group.checkedId()
        if select_collect_id == -1:
            select_collect_id = 1

        if select_collect_id == 1:
            search_string = self.ui.search_edit.text().strip()
            note_type = self.ui.note_type_cb.currentText()
            sort_type = self.ui.sort_method_cb.currentText()

            # 处理关键词
            keywords = search_string.split('|') if search_string else []
            keyword_part = f"相关'{keywords[0]}'" if keywords else ''

            # 处理笔记类型
            note_type_map = {
                '采集全部': '全部',
                '采集图文': '图文',
                '采集视频': '视频',
                '先图文后视频': '图文和视频',
                '先视频后图文': '视频和图文'
            }
            note_type_part = note_type_map.get(note_type, '未知类型')

            # 在线采集
            title_parts = ['按', sort_type, '排序采集', note_type_part, keyword_part, '笔记']
            title = ''.join(title_parts)
        else:
            # 推荐页采集
            collection_type = self.collection_type_group.button(select_collect_id).text()
            title_parts = [collection_type, '笔记']
            title = ''.join(filter(None, title_parts))

        self.ui.config_name_edit.setText(title)

    def handle_toggle_collect_radio_click(self, button):
        select_collect_id = self.collection_type_group.id(button)
        if select_collect_id == 1:
            self.ui.groupBox_3.setVisible(True)
            self.ui.groupBox_4.setVisible(True)
            self.ui.similarity_filter_chk.setChecked(self.config.is_similarity_filter)
            self.ui.similarity_filter_chk.setEnabled(True)
        elif select_collect_id == 2:
            self.ui.groupBox_3.setVisible(False)
            self.ui.groupBox_4.setVisible(True)
            self.ui.similarity_filter_chk.setChecked(True)
            self.ui.similarity_filter_chk.setEnabled(False)
        else:
            self.ui.groupBox_3.setVisible(False)
            self.ui.groupBox_4.setVisible(False)

        self.adjustSize()

    def handle_check_block_toggle(self, state):
        """
        处理是否检查屏蔽勾选框的切换事件
        :param state: 是否选中
        :return:
        """
        self.ui.groupBox_6.setVisible(state)
        self.adjustSize()

    def handle_save_btn_click(self):
        if self.collection_type_group.checkedId() in (1, 2) and self.ui.similarity_filter_chk.isChecked():
            if not self.ui.similarity_keyword_le.text():
                QtWidgets.QMessageBox.critical(
                    self, '不能保存', '在线搜索或者推荐页采集时，启用相似度过筛必须填写关键词')
                return None

        self.ui.save_btn.setEnabled(False)
        try:
            # 配置信息
            if TomlBase.auto_rename and self.edit_type not in ('copy', 'template'):
                self.handle_smart_title_btn_click()
            self.config.name = self.ui.config_name_edit.text()
            # 采集方式
            self.config.collect_type = self.collection_type_group.checkedId()
            # 在线搜索
            self.config.keywords = self.ui.search_edit.text().strip().split('|')
            self.config.note_type = self.ui.note_type_cb.currentText()
            self.config.sort_method = self.ui.sort_method_cb.currentText()
            self.config.is_similarity_filter = self.ui.similarity_filter_chk.isChecked()
            self.config.similarity_lower_limit = self.ui.similarity_lower_limit_dsb.value()
            self.config.similarity_keywords = self.ui.similarity_keyword_le.text().strip().split('|')
            # 评论设置
            self.config.is_comment = self.ui.comment_chk.isChecked()
            self.config.is_fav_no_comment = self.ui.fav_no_comment_chk.isChecked()
            self.config.is_comment_fav = self.ui.comment_fav_chk.isChecked()
            self.config.comments = self.comments
            self.config.uncommon_char_mode = self.ui.uncommon_char_mode_cb.currentText()
            self.config.uncommon_char_count = self.ui.uncommon_char_count_sb.value()
            # 屏蔽参数
            self.config.is_linked_check = self.ui.linked_check_chk.isChecked()
            self.config.is_skip_over_comment = self.ui.skip_over_comment_chk.isChecked()
            self.config.comment_threshold = self.ui.comment_threshold_sb.value()
            self.config.is_consecutive_block_stop = self.ui.consecutive_block_stop_chk.isChecked()
            self.config.consecutive_block_threshold = self.ui.consecutive_block_threshold_sb.value()
            self.config.is_overall_block_stop = self.ui.overall_block_stop_chk.isChecked()
            self.config.overall_block_threshold = self.ui.overall_block_threshold_sb.value()
            self.config.is_check_block = self.ui.check_block_chk.isChecked()
            self.config.is_retry_after_block = self.ui.retry_after_block_chk.isChecked()
            self.config.is_retry_comment_random = self.ui.random_comment_chk.isChecked()
            self.config.retry_count = self.ui.retry_count_sb.value()
            self.config.retry_interval = self.ui.retry_interval_ds.value()

            if self.edit_type == 'new':
                ConfigCenter.append(self.config)

            if self.edit_type == 'new' or self.edit_type == 'exist':
                ConfigCenter.save()
            elif self.edit_type == 'template':
                TomlBase.save()

        except Exception as e:
            logger.exception(e)
            QtWidgets.QMessageBox.critical(self, '操作失败', str(e))

        self.ui.save_btn.setEnabled(True)
        self.saved.emit(self.config)
        self.close()

    def handle_edit_comment_click(self):
        edit_comment_dialog = edit_comment.EditComment(self.comments, parent=self)
        edit_comment_dialog.editedSignal.connect(self.set_current_comments)
        edit_comment_dialog.exec()

    def set_current_comments(self, comments):
        self.comments = comments

    def display_obscuror_help_dialog(self):
        obscuror_help_dialog = QtWidgets.QDialog(parent=self)
        obscuror_help_ui.Ui_obscurorHelpRoot().setupUi(obscuror_help_dialog)
        obscuror_help_dialog.exec()
