import bpy
import bmesh
import random
import os

global filepath
filepath=""
global legname
legname = ""
class Main_OT_Generator(bpy.types.Operator):
    bl_idname = "mainoperator.create"
    bl_label = "Execute Render"
   
    def execute(self, context):
        shapename=""
        scene = context.scene.your_properties
        bpy.ops.object.hide_view_clear()
        legname=scene.showleg()
        try:
            cameras=self.camselect()
            chairs=self.chairselector()
            decolist=self.decoselector()
            renderdir=bpy.data.scenes["Scene.001"].render.filepath
            all = [item.name for item in bpy.data.objects]
            for name in all:
                if name.startswith("Texturemat_TABLETOPMAT_e"):
                    bpy.data.objects[name].hide_viewport = True
                    bpy.data.objects[name].hide_render = True
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = True
                        obj.hide_render = True
                        scene.recursive_child(obj.children)
            bpy.context.scene.render.engine = scene.renderengine
            bpy.context.scene.render.use_overwrite = False
            for name in all:
                if name.startswith("Texturemat_TABLETOPMAT_e"):
                    material = bpy.data.materials["Tabletop"]
                    nodes = material.node_tree.nodes
                    principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
                    base_color = principled.inputs['Base Color'] #Or principled.inputs[0]
                    link = base_color.links[0]
                    link_node = link.from_node
                    link_node.image.unpack(method='REMOVE')
                    link_node.image.filepath=self.imageselector()
                    link_node.image.name=os.path.basename(link_node.image.filepath)
                    print(link_node.image.name)
                    bpy.data.objects[name].hide_viewport = False
                    bpy.data.objects[name].hide_render = False
                    list_of_children = bpy.data.objects[name].children
                    for obj in list_of_children:
                        obj.hide_viewport = False
                        obj.hide_render = False
                        shapename=scene.recursive_show(obj.children)
                    selectedchair=random.choice(chairs)
                    selecteddeco=random.choice(decolist)
                    bpy.context.layer_collection.children[selectedchair].exclude = False
                    bpy.context.layer_collection.children[selecteddeco].exclude = False
                    bpy.data.objects[name].hide_viewport = True
                    bpy.data.objects[name].hide_render = True
                    for i in cameras:
                        bpy.context.scene.camera=i
                        bpy.data.scenes["Scene.001"].render.filepath=f"{renderdir}{shapename}.{legname}.{i.name}.{link_node.image.name}"
                        if f"{shapename}.{legname}.{i.name}.{link_node.image.name}.jpg" in os.listdir(renderdir):
                            self.report({'INFO'}, f"{shapename}.{legname}.{i.name}.{link_node.image.name}.jpg already exists")
                            break
                        else:
                            bpy.ops.render.render(animation=False, write_still=True, use_viewport=True, scene="Scene.001")
                            print(f"{name} rendered")
                    for obj in list_of_children:
                        obj.hide_viewport = True
                        obj.hide_render = True
                        scene.recursive_child(obj.children)
                    bpy.context.layer_collection.children[selectedchair].exclude = True
                    bpy.context.layer_collection.children[selecteddeco].exclude = True
            renderdir=bpy.data.scenes["Scene.001"].render.filepath
            return {'FINISHED'}
        except:
            self.report({'WARNING'}, "INVALID FILEPATH")
            return {'CANCELLED'}


    def updatingsettings(self,context):
        scene = context.scene.your_properties
        bpy.context.scene.render.engine = scene.renderengine
        filepath=scene.Load_Directory
        bpy.data.scenes["Scene.001"].render.filepath=filepath
        bpy.ops.object.hide_view_clear()
        legname=scene.showleg()

    def loadingfile(self,context):
        scene = context.scene.your_properties
        filename, extension = os.path.splitext(scene.Load_File)
        if extension== '.blend':
            bpy.ops.wm.open_mainfile(filepath=scene.Load_File)
        else:
            bpy.context.window_manager.popup_menu(Main_OT_Generator.oops, title="Error", icon='ERROR')

    def oops(self,context):
        self.layout.label(text="INVALID FILE TYPE! CHOOSE .blend FILE TO PROCEED.")
        
    def chairselector(self):
        list=[]
        all = [item.name for item in bpy.data.collections]
        for name in all:
            if name.startswith("Chairs"):
                list.append(name)
                bpy.context.layer_collection.children[name].exclude = True
        return list
    
    def decoselector(self):
        list=[]
        all = [item.name for item in bpy.data.collections]
        for name in all:
            if name.startswith("Deco"):
                list.append(name)
                bpy.context.layer_collection.children[name].exclude = True
        return list
    
    def camselect(self):
        cameras_obj = [cam for cam in bpy.data.objects if cam.type == 'CAMERA']
        return cameras_obj
    
    def imageselector(self):
        tabletex=[]
        path=os.path.dirname(os.path.realpath(__file__))
        final_path = str(path) + "\TABLETOP_TEXTURES"
        tabletex=os.listdir(final_path)
        texture=random.choice(tabletex)
        return f"{final_path}\{texture}"



    