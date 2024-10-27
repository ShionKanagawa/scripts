import os
import shutil
import xml.etree.ElementTree as ET

# Parse the appfilter.xml file
def parse_appfilter(appfilter_path):
    tree = ET.parse(appfilter_path)
    root = tree.getroot()
    items = []
    for item in root.findall('item'):
        component = item.get('component')
        drawable = item.get('drawable')

        # Extract the package name
        if component:
            package_name = component.split('/')[0].replace('ComponentInfo{', '').strip()
            items.append((package_name, drawable))
    return items

# Locate and copy icon files
def copy_icons(items, drawable_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for package_name, drawable_name in items:
        icon_file = f"{drawable_name}.png"
        icon_path = os.path.join(drawable_folder, icon_file)

        if os.path.exists(icon_path):
            # Copy and rename the file
            new_icon_path = os.path.join(output_folder, f"{package_name}.png")
            shutil.copy(icon_path, new_icon_path)
            print(f"Copied: {icon_file} -> {package_name}.png")
        else:
            print(f"Icon not found: {icon_file}")

# Main function
def convert_icons(appfilter_path, drawable_folder, output_folder):
    items = parse_appfilter(appfilter_path)
    copy_icons(items, drawable_folder, output_folder)

# Example call
appfilter_path = './appfilter.xml'  # Replace with the actual path to appfilter.xml
drawable_folder = './drawable-nodpi'  # Replace with the path to the drawable_nodpi folder
output_folder = './output'  # Replace with the path to the target output folder

convert_icons(appfilter_path, drawable_folder, output_folder)
