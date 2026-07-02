import bpy


class ORTHO_PT_MainPanel(bpy.types.Panel):
    """Panneau principal de l'add-on"""

    bl_label = "Ortho Template"
    bl_idname = "ORTHO_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ortho"

    def draw(self, context):

        layout = self.layout

        layout.label(text="Bienvenue !")
        layout.label(text="Le projet est en cours de développement.")

        layout.separator()

        layout.label(text="Version : 0.1")


classes = (
    ORTHO_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
