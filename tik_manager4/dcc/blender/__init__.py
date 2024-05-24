bl_info = {
    "name": "Tik Manager 4 ",
    "author": "Kursad Karatas / Arda Kutlu",
    "version": (0, 1),
    "blender": (4, 2, 0),
    "location": "File menu",
    "description": "Tik Manager App",
    "warning": "",
    "doc_url": "",
    "category": "IO",
}


import bpy
import bmesh
import bpy.types
from bpy.props import (BoolProperty, EnumProperty, FloatProperty, 
                       IntProperty, PointerProperty, StringProperty)
from bpy.types import AddonPreferences, Object, Scene, WindowManager


class TIK_Preferences(AddonPreferences):
    bl_idname = __name__
    bl_label = "TIk Manager Settings"
    bl_description = "Preferences"

    tikm_path : StringProperty(
        name="Work Folder",
        subtype='DIR_PATH',
    )

    qt_path : StringProperty(
        name="Meshlab Folder",
        subtype='DIR_PATH',
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Path to Tik Manager Installation")
        layout.prop(self, "tikm_path", text="Tik Manager installation path")
        layout.label(text="Set the folder where MeshlabServer.exe for mesh processing")
        layout.prop(self, "qt_path", text="QT Folder")



classes = ( TIK_Preferences,
            OBJECT_OT_BasemeshTempleReMeshNative,
            OBJECT_OT_SkelloMesh,
            SCULPT_OT_MaskSplit,
            SCULPT_OT_Vert2Mask,
            SCULPT_OT_Mask2Vert,

        )


def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    #bpy.ops.wm.call_menu(name=FILE_MT_BasemeshT

