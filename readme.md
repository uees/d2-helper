### Diablo II Resurrected 快捷施法辅助

功能：

    + 创建守护进程，注册全局热键  alt+/ 启用和关闭功能 （todo: 播放声音提示）
    + 按 x 强制移动
    + 按 1 ~ 0 快捷施法到鼠标区域



### 使用

1. 编辑配置 `settings.py` 技能信息做如下定义：

```python
SKILLS: list = [
    {"key_code": '1', "bind": LEFT, "name": "skill 1"},
    {"key_code": '2', "bind": LEFT, "name": "skill 2"},
    {"key_code": '3', "bind": LEFT, "name": "skill 3"},
    {"key_code": '4', "bind": RIGHT, "name": "skill 4"},
    {"key_code": '5', "bind": RIGHT, "name": "skill 5"},
    {"key_code": '6', "bind": RIGHT, "name": "skill 6"},
    {"key_code": '7', "bind": RIGHT, "name": "skill 7"},
    {"key_code": '8', "bind": RIGHT, "name": "skill 8"},
    {"key_code": '9', "bind": RIGHT, "name": "skill 9"},
    {"key_code": '0', "bind": RIGHT, "name": "skill 0"},
]
```

我在客户端中设置改键  F1~F4 吃药， 1~0 技能，如果你没改，就把上面的 `key_code` 改为 f1~f8 :

```python
SKILLS: list = [
    {"key_code": 'F1', "bind": LEFT, "name": "skill 1"},
    {"key_code": 'F2', "bind": LEFT, "name": "skill 2"},
    {"key_code": 'F3', "bind": LEFT, "name": "skill 3"},
    {"key_code": 'F4', "bind": RIGHT, "name": "skill 4"},
    {"key_code": 'F5', "bind": RIGHT, "name": "skill 5"},
    {"key_code": 'F6', "bind": RIGHT, "name": "skill 6"},
    {"key_code": 'F7', "bind": RIGHT, "name": "skill 7"},
    {"key_code": 'F8', "bind": RIGHT, "name": "skill 8"},
]
```

再一个就是确认下你的各个按键的技能是绑定在左键还是右键，按自己的绑定情况修改, 绑定在左键的：`"bind": LEFT`, 右键的： `"bind": RIGHT` .

2. 到 https://www.python.org/ 下载 python 安装

3. 命令提示符(或PowerShell)进入 `d2-helper` 目录，安装依赖  `pip install -r requirements.txt`

4. 运行脚本 `python main.py`，命令提示符窗口不要关。

5. 按 `alt`+`/` 组合键启动辅助功能，再次按 `alt`+`/` 组合键可关闭辅助功能。

6. 现在可以到 Diablo II Resurrected 中试试是否自动施法了。