from bpy.types import Panel, Operator
import bpy
import os


class AssignCamsOperator(Operator):
    bl_idname = "wm.yes_yes_assign_cams"
    bl_label = "Cum"

    def execute(self, context):
        objs = context.selected_objects
        scene = context.scene
        img_dir = bpy.path.abspath(scene.bkg_dir)
        for o in objs:
            if o.type == 'CAMERA':
                name = o.name
                name = name[:-4] + '.' + name[-3:]
                file_path = os.path.join(img_dir, name)
                if os.path.isfile(file_path):
                    img = bpy.data.images.load(file_path)
                    o.data.show_background_images = True
                    o.data.background_images.clear()
                    bg = o.data.background_images.new()
                    bg.image = img
                    bg.display_depth = 'FRONT'
                    bg.frame_method = 'CROP'
                    print('setting bg image for cam', o.name, file_path)

        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class AssignCamsPanel(Panel):
    bl_idname = 'panel.assign_cams_panel'
    bl_label = 'Assign cums'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()
        row.prop(scene, 'bkg_dir')
        row = layout.row()
        row.operator(AssignCamsOperator.bl_idname)
