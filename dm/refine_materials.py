import bpy
from bpy.types import Operator, Panel


class RefineMaterialsOperator(Operator):
    bl_idname = "wm.no_no_refine"
    bl_label = "Refine moteriels"

    def execute(self, context):
        mat_list = [mat.name for mat in bpy.data.materials]

        for o in context.selected_objects:
            if o.type == 'MESH' and o.data and o.data.materials:
                refined_materials = []
                for m in o.data.materials:
                    refined_name = m.name
                    pos = refined_name.find('.')
                    if pos > -1:
                        refined_name = refined_name[:pos]
                    if refined_name in mat_list:
                        refined_materials.append(refined_name)
                    else:
                        refined_materials.append(m.name)

                o.data.materials.clear()
                for ref_mat in refined_materials:
                    o.data.materials.append(bpy.data.materials.get(ref_mat))

        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class RefineMaterialsPanel(Panel):
    bl_idname = 'panel.refine_materials_panel'
    bl_label = 'Refine materials'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator(RefineMaterialsOperator.bl_idname)
