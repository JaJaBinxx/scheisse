import bpy
from bpy.types import Menu, Operator, Mesh
from collections import defaultdict


class OBJECT_OT_select_linked_nikita(Operator):
    bl_idname = "object.nn_select_linked"
    bl_label = "Select linked mesh blia"

    # bl_description = "Select Linked (multi)"

    def execute(self, context):
        objs = context.selected_objects

        mesh_dict = defaultdict(list)

        for o in objs:
            if isinstance(o.data, Mesh):
                key = o.data.name
                mesh_dict[key].append(o.name)
        for key in mesh_dict.keys():
            values = mesh_dict[key]
            if len(values) > 0:
                bpy.data.objects[values[0]].select_set(False)
        return {'FINISHED'}


class VIEW3D_MT_select_linked_hehe(Menu):
    bl_label = "Select Linked"
    bl_idname = "VIEW3D_MT_select_linked_nikita"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_select_linked_nikita.bl_idname)


def add_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_select_linked_hehe.bl_idname)


def add_menu_single(self, context):
    self.layout.operator(OBJECT_OT_select_linked_nikita.bl_idname)
