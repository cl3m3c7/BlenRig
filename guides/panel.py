from bpy.types import Panel
from .reproportion.guide_reproportion import GUIDE_STEPS_REPROPORTION
from .datatransfer.guide_datatransfer import GUIDE_STEPS_DATATRANSFER
from .mdef.guide_mdef import GUIDE_STEPS_MDEF
from .lattices.guide_lattices import GUIDE_STEPS_LATTICES
from .actions.guide_actions import GUIDE_STEPS_ACTIONS
from .weights.guide_weights import GUIDE_STEPS_WEIGHTS
from .shapekeys.guide_shapekeys import GUIDE_STEPS_SHAPEKEYS

class BlenRigGuidePanel_menu:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = "BLENRIG_PT_blenrig_6_general"
    bl_category = "Blenrig"

    @classmethod
    def poll(cls, context):
        BlenRigPanelOptions = context.window_manager.BlenRigPanelSettings
        if not BlenRigPanelOptions.displayContext == 'GUIDES':
            return False

        obj = context.object
        valid_types = {'POSE','ARMATURE', 'MESH', 'LATTICE', 'CURVE', 'SURFACE'}

        return obj or obj.type in valid_types

class BlenRigGuidePanel(BlenRigGuidePanel_menu,Panel):
    bl_label = "BlenRig Guide"
    bl_idname = "BLENRIG_PT_guide_panel"
    bl_space_type = 'VIEW_3D'
    bl_options = {"HIDE_HEADER",}
    bl_order = 2

    def draw(self, context):
        guide = context.scene.blenrig_guide
        layout = self.layout
        col = layout.column()
        col.label(text="Rigging Assistants")
        button = col.row()
        button_2 = col.row()
        button.scale_y = 1.5
        button_2.scale_y = 1.5
        button.operator("view3d.blenrig_guide_reproportion", text = '1 - Show Reproportion Guide')
        button.operator("view3d.blenrig_guide_datatransfer", text = '2 - Show Weights Transfer Guide')
        button.operator("view3d.blenrig_guide_mdef", text = '3 - Show Mesh Deform Guide')
        button_2.operator("view3d.blenrig_guide_lattices", text = '4 - Show Lattices Guide')
        button_2.operator("view3d.blenrig_guide_actions", text = '5 - Show Actions Guide')
        button_2.operator("view3d.blenrig_guide_weights", text = '6 - Show Weight Painting Guide')
        button_2.operator("view3d.blenrig_guide_rig_settings", text = '7 - Show Advanced Settings Guide')
        button_2.operator("view3d.blenrig_guide_shapekeys", text = '8 - Show Shapekeys Guide')
        layout.separator()

        steps = layout.column(align=True)
        desplegable = steps.box()
        desplegable.prop(guide, 'show_steps', icon='TRIA_DOWN' if guide.show_steps else 'TRIA_RIGHT', emboss=False)

        if not guide.show_steps:
            return

        step_list = steps.box().column(align=True)

        for i, step in enumerate(GUIDE_STEPS_REPROPORTION):
            step_list.operator("view3d.blenrig_guide_reproportion", text=str(i + 1) + "- " + str(step['titulo'][guide.language])).step=i

class BlenRigGuidePanel_options(BlenRigGuidePanel_menu,Panel):
    bl_label = "Options"
    bl_idname = "BLENRIG_PT_guide_panel_sub"
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1

    def draw(self, context):
        guide = context.scene.blenrig_guide
        layout = self.layout
        from . guide_ops import VIEW3D_OT_blenrig_guide_reproportion as OPERATOR
        layout.enabled = False if OPERATOR.instance else True
        layout.prop(guide, 'language')
        layout.prop(guide, 'dpi')
        layout.prop(guide, 'image_scale')
