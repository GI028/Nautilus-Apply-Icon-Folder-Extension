import os
import gi
from gi.repository import Nautilus, GObject, Gio,Notify
import subprocess

# Import the correct GI version
gi_version_major = 3 if 30 <= gi.version_info[1] < 40 else 4
gi.require_versions(
    {
        "Nautilus": "3.0" if gi_version_major == 3 else "4.0",
        "Gdk": "3.0" if gi_version_major == 3 else "4.0",
        "Gtk": "3.0" if gi_version_major == 3 else "4.0",
    }
)

def log_message(msg):
    # with open(LOG_PATH, "a") as log_file:
    #     log_file.write(msg + "\n")
    print(msg)

def show_refresh_notification():
    Notify.init("Nautilus Extension")
    notification = Notify.Notification.new(
        "Icon Updated",
        "Please press F5 or navigate away and back to refresh the folder view and see changes.",
        None
    )
    notification.show()

def is_valid_folder(file):
    return file.is_directory() and file.get_name().startswith(".icons")

def set_custom_icon(folder_path, icon_path):
    try:
        file = Gio.File.new_for_path(folder_path)
        # Must use file:// URL scheme
        icon_uri = "file://" + icon_path
        file.set_attribute_string(
            "metadata::custom-icon", icon_uri, Gio.FileQueryInfoFlags.NONE, None
        )
    except Exception as e:
        log_message(f"Failed to Add custom icon metadata to the {folder_path} path: {e}")
        
    
def remove_custom_icon(folder_path):    
    try:
        subprocess.run(
            ['gio', 'set', '-t', 'unset', folder_path, 'metadata::custom-icon'],
            check=True
        )
    except Exception as e:
        log_message(f"Failed to remove custom icon metadata from path {folder_path}: {e}")
        
def get_folders(file):
    selected_path = file.get_location().get_path()
    if not selected_path:
        log_message("Could not get path of selected folder")
        return

    parent_dir = os.path.dirname(selected_path)
    try:
        entries = os.listdir(parent_dir)
    except Exception as e:
        log_message(f"Error listing parent directory '{parent_dir}': {e}")
        return

    # Filter only directories (folders) in the parent directory
    sibling_folders = [
        entry for entry in entries if os.path.isdir(os.path.join(parent_dir, entry))
    ]
    return sibling_folders


def get_icons(file):
    # Get the path of the selected folder itself
    selected_path = file.get_location().get_path()
    if not selected_path:
        log_message("Could not get path of selected folder")
        return

    try:
        # List all entries inside the selected folder
        entries = os.listdir(selected_path)
    except Exception as e:
        log_message(f"Error reading directory '{selected_path}': {e}")
        return

    # Filter the list to include only files ending with .png (case-insensitive)
    try:
        return {
            os.path.splitext(entry)[0]
            for entry in entries
            if entry.lower().endswith(".png")
            and os.path.isfile(os.path.join(selected_path, entry))
        }
    except Exception as e:
        log_message(f"Error reading directory '{selected_path}': {e}")
        return set()



class ApplyIconFoldersExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()

    def menu_activate_cb(self, menu, file):
        # set_custom_icon(file.get_location().get_path(), ICON_PATH)
        # os.path.join(parent_dir, entry)
        folders=get_folders(file)
        icons=get_icons(file)
        icons_dir = file.get_location().get_path()
        folders_dir = os.path.dirname(icons_dir)
        
        for folder in folders:
            if folder in icons:
                set_custom_icon(os.path.join(folders_dir, folder),os.path.join(icons_dir,folder+".png"))
            else:
                remove_custom_icon(os.path.join(folders_dir, folder))   
        show_refresh_notification()  
        
    def get_custom_item(self,file):
        item = Nautilus.MenuItem(
            name="SimpleMenuExtension::Show_File_Name",
            label="Apply icons",
            tip="Use the icons inside this folder to update folders on the same levels",
        )
        item.connect("activate", self.menu_activate_cb, file)
        return item
    # Item menu on the .icons folder
    def get_file_items(self, *args, **kwargs):
        files = args[0] if gi_version_major == 4 else args[1]

        if len(files) != 1:
            return []

        file = files[0]
        if not is_valid_folder(file):
            return []

        return [self.get_custom_item(file)]
    # Item menu on the .icons directory
    def get_background_items(self, *args, **kwargsr):
        file = args[0] if gi_version_major == 4 else args[1]

        if not is_valid_folder(file):
            return []

        return [self.get_custom_item(file)]
