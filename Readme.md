Nautilus Apply Icons Extension
A Nautilus extension that allows you to use a dedicated folder of icons to apply custom emblems to its sibling folders.

Replace the placeholder image above with a screenshot or an animated GIF demonstrating your extension. Tools like Peek or Giphy Capture can create GIFs easily.

Description
This Python-based extension for the GNOME Nautilus file manager provides a quick way to manage custom folder icons for project theming.

The core workflow is simple:

Create a special folder (e.g., .icons-theme).

Fill it with .png icons whose names match the names of other folders at the same directory level.

Right-click the special folder and select "Apply Icons From This Folder".

The extension will automatically apply each icon to its corresponding folder. If a folder doesn't have a matching icon, its custom icon will be removed, reverting it to the default.

Features
Bulk Icon Application: Apply dozens of custom folder icons with a single click.

Automatic Icon Removal: Cleans up custom icons from folders that no longer have a match in your icons folder.

User Notifications: Provides clear desktop notifications when the process is complete.

Detailed Logging: Creates a log file at ~/.nautilus-apply-icon-folder-extension.log for troubleshooting.

Requirements
Before installing, ensure you have the following dependencies:

A Debian-based Linux distribution (e.g., Ubuntu, Pop!_OS, Linux Mint)

Nautilus File Manager

Python 3

The python3-nautilus package

The gir1.2-notify-0.7 package (for desktop notifications)

The gio command-line utility (usually included with glib2.0-bin)

On most Debian-based systems, you can install these with the following command:

sudo apt update
sudo apt install python3-nautilus gir1.2-notify-0.7

Installation
Download the script:
Save the extension script as apply_icons_extension.py.

Create the extensions directory:
The script needs to be placed in the Nautilus Python extensions directory. If it doesn't exist, create it:

mkdir -p ~/.local/share/nautilus-python/extensions/

Copy the script:
Move the apply_icons_extension.py file into that directory:

cp apply_icons_extension.py ~/.local/share/nautilus-python/extensions/

Restart Nautilus:
For the extension to be recognized, you must completely quit and restart Nautilus.

nautilus -q
nautilus

How to Use
Navigate to a directory where you have several project folders (e.g., FolderA, FolderB, FolderC).

Create a new folder and name it with the prefix .icons-. For example, .icons-my-theme.

Inside the .icons-my-theme folder, place your .png icons. The icon names (without the extension) must exactly match the names of the sibling folders. For example, to theme FolderA, you must have an icon named FolderA.png.

Right-click on the .icons-my-theme folder.

Select "Apply Icons From This Folder" from the context menu.

A notification will appear. Press F5 or navigate away and back to see the icon changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.