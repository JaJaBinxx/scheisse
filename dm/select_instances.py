import bpy
from bpy.types import Menu, Operator


class OBJECT_OT_select_linked_nikita(Operator):
    bl_idname = "object.nn_select_linked"
    bl_label = "Select linked mesh blia"

    # bl_description = "Select Linked (multi)"

    def execute(self, context):
        objs = context.selected_objects

        for ob in objs:
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.select_linked(extend=True, type='OBDATA')

        for ob in objs:
            bpy.context.view_layer.objects.active = ob
            bpy.context.active_object.select_set(False)
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
