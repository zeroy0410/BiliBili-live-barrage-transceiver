# BiliBili live barrage transceiver

![screenshot](https://github.com/zeroy0410/BiliBili-live-barrage-transceiver/blob/main/src/screenshot.png)

### Install
A simple python program for sending and receiving barrage in bilibili live room.

This project needs you to install requests first.
```
pip install requests
```

It's needed to full your basic information which can be seen in Browser Dev Tool in `config.json`.

It's recommended to install Tmux for the best experience.

### Usage
Create a new terminal.

Run tmux.

Use `Ctrl+b` and `%` to split the windows and `Ctrl+b` and `Direction key` to change the focus between two sessions.

Run `python receive.py` in the left session,and `python send.py` in the right session.

Now you can receive and send barrages.

Enjoy it!

