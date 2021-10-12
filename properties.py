import bpy
import random
from . main_bpy import Main_OT_Generator
from bpy.props import (EnumProperty, FloatProperty, IntProperty,
                       PointerProperty, BoolProperty, StringProperty)
from bpy.types import Operator, Panel, PropertyGroup, TexMapping

global updation
updation = Main_OT_Generator.updatingsettings
loadfileupdate = Main_OT_Generator.loadingfile

class addon_Properties(PropertyGroup):

    def Load_File_Check(self):
        all = [item.name for item in bpy.data.objects]
        if len(all)==1555:
            return(False)
        else:
            return(True)

    def hidelegs(self):
        all = [item.name for item in bpy.data.objects]
        for name in all:
            if name.startswith('CONF') or name.startswith('TableLegs'):
                bpy.data.objects[name].hide_viewport = True
                list_of_children = bpy.data.objects[name].children
                for obj in list_of_children:
                    obj.hide_viewport = True
                    obj.hide_render = True
                self.recursive_child(bpy.data.objects[name].children)

    def showleg(self):
        legtype= self.Leg_Type
        all = [item.name for item in bpy.data.objects]
        if legtype == "Delta":
            for name in all:
                if name.startswith("CONF Delta Symmetrisch"):
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        self.recursive_show(obj.children)
        elif legtype == "Hotel":
            for name in all:
                if name.startswith("CONF Hotel Symmetrisch"):
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        self.recursive_show(obj.children)
        elif legtype == "Mike":
            for name in all:
                if name.startswith("CONF Mike Symmetrisch"):
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        self.recursive_show(obj.children)
        elif legtype == "Leg003":
            for name in all:
                if name.startswith("TableLegs.003"):
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        self.recursive_show(obj.children)
        elif legtype == "Leg004":
            for name in all:
                if name.startswith("TableLegs.004"):
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        self.recursive_show(obj.children)

    def recursive_show(self,list):
        children_list = []    
        for obj in list:
            if obj.children:
                children_list.append(obj.children)
            obj.hide_viewport = False
            obj.hide_render = False
        if children_list:
            for child in children_list:
                self.recursive_show (child)

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
    
    mode_options = [
        ("Delta", "Delta Version", '', 'Leg Type Delta', 0),
        ("Hotel", "Hotel Version", '', 'Leg Type Hotel', 1),
        ("Mike", "Mike Version", '', 'Leg Type Mike', 2),
        ("Leg003", "Table Leg 003", '', 'Leg Type 003', 3),
        ("Leg004", "Table Leg 004", '', 'Leg Type 004', 4)
    ]
    renderers = [
        ("CYCLES", "Cycles", '', "Cycles", 0),
        ("BLENDER_EEVEE", "Eevee",'',"Eevee",1)
    ]
    Load_File : StringProperty(subtype="FILE_PATH", update=loadfileupdate)

    Load_Directory : StringProperty(subtype="DIR_PATH", default="", update=updation)
    Leg_Type : EnumProperty(items=mode_options,
        name="Leg Type",
        description="Please Select the Desired Table Leg",
        default="Delta",
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

    
