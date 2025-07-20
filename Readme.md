# Apply Icon Folders - Nautilus Python Extension

## Overview

**Apply Icon Folders** is a Nautilus extension written in Python that simplifies the process of bulk updating folder icons using PNG files stored inside a special directory. The extension detects any folder whose name **starts with `.icons`** (for example, `.icons`, `.icons-theme`, or `.icons_backup`) and uses the `.png` icon files inside it to set custom icons for sibling folders on the same directory level.

When you right-click on such a folder (e.g., `.icons-theme`), an "Apply icons" option appears in the context menu. Selecting it will apply the icons from the `.png` files to the corresponding sibling folders whose names exactly match the icon filenames (without the `.png` extension). Folders without a matching icon will have any existing custom icon removed.

## Features

- Works with *any* folder starting with `.icons` (not strictly `.icons`).
- Automatically scans sibling folders of the `.icons*` folder’s parent directory.
- Applies `.png` icons whose filenames match sibling folder names.
- Removes custom icons from folders that don't have a matching icon file.
- Shows a desktop notification prompting to refresh Nautilus for changes to take effect.

## Installation

### Download the Extension

You can download the extension script from here:
[nautilus-applyiconfoldersextension.py](nautilus-applyiconfoldersextension.py)

### Prerequisites

- Nautilus (Files) version 3.x or 4.x
- Python 3
- `nautilus-python` package
- PyGObject
- `gio` command-line utility (usually installed with GLib)

#### Install dependencies on Debian/Ubuntu
```bash
sudo apt install python3-nautilus python3-gi libglib2.0-bin
```
#### Install dependencies on Fedora
```bash
sudo dnf install nautilus-python python3-gobject glib2-devel # Or just glib2 if glib2-devel is not found
```
### Installation Steps

1. Copy the downloaded `nautilus-applyiconfoldersextension.py` script to one of the Nautilus Python extensions directories:

- For user-only installation:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions/
cp ~/Downloads/nautilus-applyiconfoldersextension.py ~/.local/share/nautilus-python/extensions/
```
- For system-wide installation (requires root permissions):
```bash
sudo cp ~/Downloads/nautilus-applyiconfoldersextension.py /usr/share/nautilus-python/extensions/
```
2. Restart Nautilus to load the extension:
```bash
nautilus -q
nautilus &
```
## Usage

1. Create a folder whose name begins with `.icons` inside a directory containing sibling folders you want to update icons for (e.g., `.icons-theme`).

2. Add `.png` icon files inside this `.icons*` folder. Each `.png` file’s name (without the extension) must exactly match the sibling folder name you wish to assign that icon to.

3. Right-click the `.icons*` folder in Nautilus and select **"Apply icons"** from the context menu.

4. A notification will appear asking you to press `F5` or navigate away and back to refresh the folder view to see icon changes.

## How It Works

- The extension scans the parent directory of the `.icons*` folder and lists all sibling folders.
- It collects all `.png` files inside the `.icons*` folder and matches their filenames against sibling folder names.
- For matching names, it sets the folder’s custom icon metadata to the corresponding `.png`.
- For folders without a matching icon, it removes any custom icon metadata.
- Finally, it displays a desktop notification reminding you to refresh the Nautilus view.

## Troubleshooting

- Ensure required dependencies (`python3-nautilus` and GI libraries) are installed.
- Confirm the extension script is placed in the correct Nautilus extensions directory.
- Restart Nautilus after installing or modifying the extension.
- Run Nautilus with debug mode for troubleshooting:

NAUTILUS_PYTHON_DEBUG=misc nautilus

- Icon filenames and folder names are case-sensitive and must match exactly (excluding the `.png` extension).

## License

This extension is provided under the MIT License.

---

*This README was created to document a Nautilus Python extension that applies custom folder icons based on `.png` files inside any folder beginning with `.icons`.*