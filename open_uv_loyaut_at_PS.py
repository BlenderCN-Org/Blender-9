import bpy

tempFolder = bpy.app.tempdir
uvLay =tempFolder+"uv_temp.png"


def openInPs():
	bpy.ops.uv.export_layout(filepath=uvLay, size=(1024, 1024), opacity=0)
	bpy.ops.image.external_edit(filepath=uvLay)
	finishOp = True


openInPs()

