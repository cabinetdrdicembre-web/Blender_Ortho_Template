import bpy


class ORTHO_PT_MainPanel(bpy.types.Panel):
    bl_label = "Ortho Template"
    bl_idname = "ORTHO_PT_mainpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ortho'

    def draw(self, context):

        layout = self.layout

        layout.label(text="Orthodontic Template")

        layout.separator()

        layout.operator(
            "ortho.import_stl",
            icon='IMPORT'
        )

        layout.separator()

        layout.operator(
            "ortho.create_cameras",
            icon='CAMERA_DATA'
        )

        layout.operator(
            "ortho.render_views",
            icon='RENDER_STILL'
        )
