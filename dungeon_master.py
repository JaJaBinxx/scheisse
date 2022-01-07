from dm.refine_materials import RefineMaterialsOperator, RefineMaterialsPanel
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


def unregister():
    unregister_class(RefineMaterialsPanel)
    unregister_class(RefineMaterialsOperator)
