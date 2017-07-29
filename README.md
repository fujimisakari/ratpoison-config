My Linux Development Environment
--

The Ratpoison is my favorite Tiling Window Manager.
You can work in the same way as the GUN Screen.

http://www.nongnu.org/ratpoison/


## How to setup

1. Download and initialization.

```sh
$ git clone https://github.com/fujimisakari/ratpoison-config .ratpoison-config
$ ./.ratpoison-config/init.py
```

2. Install ratpoison and option package.

```sh
$ sudo apt-get install ratpoison ratmenu conky
```

3. Create this file to '/usr/share/xsessions/ratpoison.desktop'.

```
[Desktop Entry]
Encoding=UTF-8
Name=Ratpoison
Comment=Start Ratpoison as your window manager
Exec=ratpoison
Icon=
Type=Application
```

4. Logout, and Xsession change to ratpoison on login page.
