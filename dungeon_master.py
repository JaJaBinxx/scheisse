import bpy
from dm.refine_materials import RefineMaterialsOperator, RefineMaterialsPanel
from dm.select_instances import OBJECT_OT_select_linked_nikita, VIEW3D_MT_select_linked_hehe, add_menu_single
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "DUNGEON MASTER",
    "description": "",
    "author": "me",
    "version": (2, 28),
    "blender": (2, 91, 0),
    "location": "Scene panel",
    "category": "Render",
    "support": "COMMUNITY"
}


def register():
    register_class(RefineMaterialsOperator)
    register_class(RefineMaterialsPanel)
    register_class(OBJECT_OT_select_linked_nikita)
    register_class(VIEW3D_MT_select_linked_hehe)
    bpy.types.VIEW3D_MT_select_object.append(add_menu_single)


def unregister():
    unregister_class(RefineMaterialsPanel)
    unregister_class(RefineMaterialsOperator)
    unregister_class(VIEW3D_MT_select_linked_hehe)
    unregister_class(OBJECT_OT_select_linked_nikita)
    bpy.types.VIEW3D_MT_select_object.remove(add_menu_single)
