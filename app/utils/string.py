import re
import string
import uuid


def get_short_id():
    """
    获取短 ID
    :return: str 8位 短ID
    """
    _array = string.digits + string.ascii_letters
    _id = str(uuid.uuid4()).replace('-', '')
    buffer = []
    for i in range(0, 8):
        start = i * 4
        end = (i + 1) * 4
        val = int(_id[start: end], 16)
        buffer.append(_array[val % 62])

    return ''.join(buffer)


def validate_user_id(user_id: str):
    """
    校验小红书 User ID
    :param user_id: UserID
    :return:
    """
    pattern = r'^[0-9a-f]{24}$'
    return bool(re.match(pattern, user_id))


def validate_note_id(note_id: str):
    """
    校验小红书 Note ID
    :param note_id: NoteID
    :return:
    """
    pattern = r'^[0-9a-f]{24}$'
    return bool(re.match(pattern, note_id))


def validate_web_session(session: str):
    """
    校验小红书 CK 中的 web_session
    :param session: web_session 值
    :return:
    """
    pattern = r'^[0-9a-f]{38}$'
    return bool(re.match(pattern, session))


def validate_chinese_name(name):
    """
    常规的判断中文名
    :param name: 名字
    :return: 返回bool类型
    """
    pattern = "^[\u4e00-\u9fa5]{2,5}$"  # 匹配2到4个汉字
    return re.match(pattern, name) is not None


def create_link(url: str, text: str, max_length: int = 0):
    """
    根据给定的 URL 和文本，创建一个 HTML 链接。可以指定最大长度来截断文本。
    """
    if max_length == 0:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{truncate(text, max_length)}</a>'


def extract_link_text(link_text: str):
    """
    从 HTML 链接中提取显示的文本。
    """
    pattern = r'<a.*?>(.*?)</a>'
    match = re.search(pattern, link_text)
    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        return None


def truncate(s, max_length, ellipsis='...'):
    """
    截断字符串，使其不超过指定的最大长度。可以指定省略号的样式。
    """
    if len(s) > max_length:
        return s[:max_length - len(ellipsis)] + ellipsis
    return s


def replace_dbl_backslash(s):
    """
    将字符串中的双反斜杠替换为单反斜杠。
    """
    return s.replace(r'\\', '\\')


def decode_unicode_esc(s):
    """
    对字符串中的 Unicode 转义序列进行解码。
    """
    return s.encode().decode('unicode_escape')


def keep_literal(s):
    """
    将字符串转换为其原始表示形式（带有引号）。
    """
    return f'{s!r}'


def restore_str(s):
    """
    对字符串进行处理，包括替换双反斜杠和解码 Unicode 转义序列。
    """
    s = replace_dbl_backslash(s)
    s = decode_unicode_esc(s)
    return s
