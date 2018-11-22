import bpy

uvLay ="D:\\uv_layout.png"
print(uvLay)
bpy.ops.uv.export_layout(filepath=uvLay, size=(1024, 1024), opacity=0)
bpy.ops.image.external_edit(filepath=uvLay)
