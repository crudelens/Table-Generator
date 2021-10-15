import bpy
import random
from . main_bpy import Main_OT_Generator
from bpy.props import (EnumProperty, FloatProperty, IntProperty,
                       PointerProperty, BoolProperty, RemoveProperty, StringProperty)
from bpy.types import Operator, Panel, PropertyGroup, TexMapping
global updation
updation = Main_OT_Generator.updatingsettings
loadfileupdate = Main_OT_Generator.loadingfile
global objret
objret=""
class addon_Properties(PropertyGroup):

    def Load_File_Check(self):
        all = [item.name for item in bpy.data.objects]
        if len(all)>75:
            return(False)
        else:
            return(True)

    def showleg(self):
        legtype=self.Leg_Type
        return legtype

    def recursive_show(self,list):
        children_list = []
        for obj in list:
            if obj.children:
                children_list.append(obj.children)
            obj.hide_viewport = False
            obj.hide_render = False
            if obj.type=="MESH":
                objret=obj.name
                return objret

        if children_list:
            for child in children_list:
                objret=self.recursive_show (child)
            return objret
            

    def recursive_child(self, list): #hide
        children_list = []    
        for obj in list:
            if obj.children:
                children_list.append(obj.children)
            obj.hide_viewport = True
            obj.hide_render = True
        if children_list:
            for child in children_list:
                self.recursive_child (child)

    renderers = [
        ("CYCLES", "Cycles", '', "Cycles", 0),
        ("BLENDER_EEVEE", "Eevee",'',"Eevee",1)
    ]
    Load_File : StringProperty(subtype="FILE_PATH", update=loadfileupdate)

    Load_Directory : StringProperty(subtype="DIR_PATH", default="", update=updation)

    Leg_Type : StringProperty(
        name="Leg name",
        default = "",
        update=updation
        )
    
    renderengine : EnumProperty(items=renderers, 
        name="Engine",
        description="Choose Render Engine",
        default='BLENDER_EEVEE',
        update=updation
        )

    filter_glob = StringProperty(default="*.blend", options={'HIDDEN'})
    
    connector : BoolProperty(
        name="",
        description="",
        default = False
    )
    #numberchecker

    
