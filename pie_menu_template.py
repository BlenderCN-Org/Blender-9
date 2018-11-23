# Template file added to by JTa, based on Templates&gt;Python&gt;UI Pie Menu
#   the additions show how to keybind the new menu from an addon/script
#   added code to keybind shift-q to bring up select mode

import bpy
from bpy.types import Menu

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)

class VIEW3D_PIE_select_mode(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator_enum("mesh.select_mode", "type")

addon_keymaps = []


def register():
    bpy.utils.register_class(VIEW3D_PIE_select_mode)

    # area below was based on code from the scripts\addons\ui_pie_menus_official.py file
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
    
    kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', shift=True)
    kmi.properties.name = 'VIEW3D_PIE_select_mode'        

    addon_keymaps.append(km)
    

def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_select_mode)

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)

        wm.keyconfigs.addon.keymaps.remove(km)

    # clear the list
    del addon_keymaps[:]
    

if __name__ == "__main__":
    register()
