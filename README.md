# Nav Panel

Inspired on vim's netrw, shows a quick panel to open files within the current directory.

![Preview](http://sahib.io/nav_panel.gif)

It's usefull when you want to quickly open files within the current buffer's directory, also you can navigate on directories without opening the side bar.

## Key mappings

### Windows and Linux
```
[
    {"keys": ["ctrl+alt+p"], "command": "open_nav_panel"},
]
```

### macOS
If you often use the `show_scope_name` command (`super+alt+p`) you should use another key mappig.
```
[
    {"keys": ["super+alt+p"], "command": "open_nav_panel"},
]
```

## Default settings
```
{
    "show_hidden_files": false
}
```
