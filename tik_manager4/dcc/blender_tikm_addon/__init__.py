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


import sys
from pathlib import Path


import bpy
import bmesh
import bpy.types
from bpy.props import (BoolProperty, EnumProperty, FloatProperty, 
                       IntProperty, PointerProperty, StringProperty)
from bpy.types import AddonPreferences, Object, Scene, WindowManager





def define_props():
    bpy.types.WindowManager.tikm_path = StringProperty(name="tikm_path", default="",
                                                description="path for TiK Manager")

    bpy.types.WindowManager.qt_path = StringProperty(name="qt_path", default="")


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
        layout.label(text="QT Framework path")
        layout.prop(self, "qt_path", text="QT Folder")


# Define an operator for the Main UI
class WM_OT_TikMainUI(bpy.types.Operator):
    bl_idname = "wm.tik_main_ui"
    bl_label = "Tik Main UI"

    def execute(self, context):
        tik_ui = main.launch(dcc="Blender")
        self.report({'INFO'}, "Tik Main UI Launched")
        return {'FINISHED'}


# Define an operator for the Save Version action
class WM_OT_TikSaveVersion(bpy.types.Operator):
    bl_idname = "wm.tik_new_version"
    bl_label = "Tik New Version"

    def execute(self, context):
        tik_ui = main.launch(dcc="Blender", dont_show=True)
        tik_ui.on_new_version()
        return {'FINISHED'}

    # Define an operator for the Publish action

class WM_OT_TikPublish(bpy.types.Operator):
    bl_idname = "wm.tik_publish"
    bl_label = "Tik Publish"

    def execute(self, context):
        tik_ui = main.launch(dcc="Blender", dont_show=True)
        tik_ui.on_publish_scene()
        return {'FINISHED'}
    # Define the Tik Manager menu

class VIEW3D_MT_tik_manager(bpy.types.Menu):
    bl_label = "Tik Manager"
    bl_idname = "VIEW3D_MT_tik_manager"

    def draw(self, context):
        layout = self.layout

        tikm_path=context.window_manager.tikm_path
        

        if tikm_path:

            pyside_path = str( Path(__file__).joinpath("site-packages") )
            qt_path = str( Path(tikm_path).joinpath(__file__).joinpath("site-packages") )

            if pyside_path not in sys.path:
                sys.path.insert(0, pyside_path)

            if tik_path not in sys.path:
                sys.path.append(tik_path)

            from tik_manager4.ui.Qt import QtWidgets
            from tik_manager4.ui import main

        # Add the commands to launch the external UI
        layout.operator("wm.tik_main_ui")
        # Add a separator between commands
        layout.separator()
        layout.operator("wm.tik_new_version")
        layout.operator("wm.tik_publish")

def menu_func(self, context):
    self.layout.menu("VIEW3D_MT_tik_manager")

classes = ( 
            TIK_Preferences,
            WM_OT_TikMainUI,
            WM_OT_TikSaveVersion,
            WM_OT_TikPublish,
            VIEW3D_MT_tik_manager,
        )

def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.TOPBAR_HT_upper_bar.prepend(menu_func)

def unregister():

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()