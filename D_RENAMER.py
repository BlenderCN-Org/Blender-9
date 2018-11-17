#----------------------------------------------------------
# File layout.py
#----------------------------------------------------------
import bpy
 
#   Layout panel
class LayoutPanel(bpy.types.Panel):
    bl_label = "Panel with funny layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        layout = self.layout

 
        layout.label("Renamer", icon='TEXT')
        row = layout.row()
        box = row.box()
        box.operator("my.button", text="NONE", emboss=False).loc="4 11"
        box.operator("my.button", text="Arena", emboss=False).loc="4 11"
        box.operator("my.button", text="Canyon", emboss=False).loc="4 12"
        box.operator("my.button", text="Dubai", emboss=False).loc="4 13"
        box.operator("my.button", text="Alitude", emboss=False).loc="4 14"
   
###############################################
       
        box1 = row.box()
        box1.operator("my.button", text="NONE", emboss=False)

       
###############################################
        
        box = row.box()
        box.operator("my.button", text="00", emboss=False)
        box.operator("my.button", text="01", emboss=False)
        box.operator("my.button", text="02", emboss=False)
        box.operator("my.button", text="03", emboss=False)
        box.operator("my.button", text="04", emboss=False)
        box.operator("my.button", text="05", emboss=False)
        box.operator("my.button", text="06", emboss=False)
        box.operator("my.button", text="07", emboss=False)
        box.operator("my.button", text="08", emboss=False)
        box.operator("my.button", text="09", emboss=False)

    def register():
    print("Hello World")
def unregister():
    print("Goodbye World"
    
#    Registration
bpy.utils.register_module(__name__)