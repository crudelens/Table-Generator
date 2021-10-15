import bpy
import os

from bpy.props import FloatProperty, PointerProperty, StringProperty
from bpy.types import Operator, Panel, PropertyGroup, RenderEngine

class Interface_PT_Panel(bpy.types.Panel):
    bl_label = "Table Generator"
    bl_idname = "SETTINGS_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "TableGen"

    def draw(self, context):
        layout = self.layout
        scene = context.scene.your_properties
        col = layout.column()
        if scene.Load_File_Check():
            col.label(text="Load AI48_001STUDIO File", icon="BLENDER")
            col.prop(scene,"Load_File",icon_only=True)
        else:
            col = layout.column()
            col.label(text="Name Table Legs", icon = "OUTLINER_OB_EMPTY")
            row=layout.row()
            row.prop(scene, "Leg_Type", text="Leg")
            col = layout.column()
            col = layout.column()
            col.label(text="Select Render Engine", icon = "RENDER_RESULT")
            col.prop(scene, "renderengine", icon="RESTRICT_RENDER_OFF")
            col = layout.column()
            col.label(text="File Directory", icon = "FILEBROWSER")
            col.prop(scene,"Load_Directory",icon_only=True)
            col = layout.column()
            col.operator("mainoperator.create", icon = "PLAY")
