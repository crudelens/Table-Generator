import bpy
import os

from . main_bpy import Main_OT_Generator

class Checker_OT_Generator(bpy.types.Operator):
    bl_idname = "checkerop.create"
    bl_label = "Check Last Render"

    def execute(self, context):
        bpy.context.window_manager.popup_menu(Checker_OT_Generator.oops, title="Last Rendered File", icon='RECOVER_LAST')
        return {'FINISHED'}

    def oops(self,context):
        scene = context.scene.your_properties
        filepath=bpy.data.scenes["Scene.001"].render.filepath
        cameras=Main_OT_Generator.camselect(self)
        result="NO RENDERS FOUND"
        all = [item.name for item in bpy.data.objects]
        if filepath != "":
            for name in all:
                if name.startswith("Texturemat_TABLETOPMAT_e"):
                    for i in cameras:
                        if f"{name}.{scene.Leg_Type}.{i.name}.jpg" in os.listdir(filepath):
                            result=f"{name}.{scene.Leg_Type}.{i.name}"
            self.layout.label(text=f"{result}")
        else:
            self.layout.label(text="FILEPATH IS EMPTY")