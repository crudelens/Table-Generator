# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Table Generator",
    "author" : "Ayush Yadav",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

#imports
import bpy,bmesh
from bpy.props import(
    PointerProperty
)

from . main_bpy import Main_OT_Generator
from . Interface_Panel import Interface_PT_Panel
from . properties import addon_Properties

classes = (Interface_PT_Panel, Main_OT_Generator, addon_Properties)
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.your_properties = PointerProperty(type=addon_Properties) #Propertygroupaccess

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.your_properties #Propertygroupdelete