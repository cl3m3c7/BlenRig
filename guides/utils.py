import bpy
from bpy_extras import view3d_utils
from math import radians
from mathutils import Matrix, Vector

# GET ARMATURE
def get_armature_object(context):
    return context.scene.blenrig_guide.arm_obj

# REPROPORTION
def set_reproportion_on(context=None):
    if context:
        context.pose_object.data.reproportion = True
        context.pose_object.show_in_front = True

def set_reproportion_off(context=None):
    if context:
        context.pose_object.data.reproportion = False
        context.pose_object.show_in_front = False

# Display Type
def set_display_type(context, mode):
    context.pose_object.data.display_type = mode

# POSE
def deselect_all_pose_bones(context=None, invert=False):
    if context:
        for b in context.pose_object.pose.bones: #context.selected_pose_bones_from_active_object:
            b.bone.select = invert
    else:
        bpy.ops.pose.select_all(action='DESELECT' if not invert else 'SELECT')

def select_all_pose_bones(context=None):
    deselect_all_pose_bones(context, True)

# EDIT
def deselect_all_edit_bones(context=None, invert=False):
    if context:
        for b in context.active_object.data.edit_bones:
            b.select = b.select_head = b.select_tail = invert
    else:
        bpy.ops.armature.select_all(action='DESELECT' if not invert else 'SELECT')

def select_all_edit_bones(context=None):
    deselect_all_edit_bones(context, True)

# POSE
def deselect_pose_bone(context, bone_name, invert=False):
    if not context:
        return
    bone = context.pose_object.data.bones.get(bone_name, None)
    if bone:
        bone.select = invert

def select_pose_bone(context, bone_name):
    deselect_pose_bone(context, bone_name, True)
    bones = context.pose_object.data.bones
    bone = bones.get(bone_name, None)
    if bone:
        bones.active = bone

# EDIT
def deselect_edit_bone(context, bone_name, invert=False):
    if not context:
        return
    bone = context.active_object.data.edit_bones.get(bone_name, None)
    if bone:
        bone.select = bone.select_head = bone.select_tail = invert

def select_edit_bone(context, bone_name):
    deselect_edit_bone(context, bone_name, True)

# POSE
def select_pose_bones(context, *bone_names):
    if not context:
        return
    bones = context.pose_object.data.bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.select = True
            bones.active = bone

def deselect_pose_bones(context, *bone_names):
    if not context:
        return
    bones = context.pose_object.data.bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.select = False

# EDIT
def select_edit_bones(context, *bone_names):
    if not context:
        return
    bones = context.active_object.data.edit_bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.select = bone.select_head = bone.select_tail = True

def deselect_edit_bones(context, *bone_names):
    if not context:
        return
    bones = context.active_object.data.edit_bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.select = bone.select_head = bone.select_tail = False

# POSE / OBJECT
def hide_bones(context, *bone_names):
    if not context:
        return
    bones = context.pose_object.data.bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.hide = True

def unhide_bones(context, *bone_names):
    if not context:
        return
    bones = context.pose_object.data.bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.hide = False

# EDIT
def hide_edit_bones(context, *bone_names):
    if not context:
        return
    bones = context.active_object.data.edit_bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.hide = True

def unhide_edit_bones(context, *bone_names):
    if not context:
        return
    bones = context.active_object.data.edit_bones
    for name in bone_names:
        bone = bones.get(name, None)
        if bone:
            bone.hide = False

# POSE / OBJECT
def hide_all_bones(context):
    if context:
        for bone in context.pose_object.data.bones:
            bone.hide = True
    else:
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.hide(unselected=False)

def unhide_all_bones(context):
    if context:
        for bone in context.pose_object.data.bones:
            bone.hide = False
    else:
        bpy.ops.pose.reveal()
        bpy.ops.pose.select_all(action='DESELECT')

def hide_selected_pose_bones(context):
    if context:
        for pose_bone in context.selected_pose_bones_from_active_object:
            pose_bone.bone.hide = True
    else:
        bpy.ops.pose.hide(unselected=False)

# EDIT
def hide_all_edit_bones(context):
    for bone in context.active_object.data.edit_bones:
        bone.hide = True

def unhide_all_dit__bones(context):
    for bone in context.active_object.data.edit_bones:
        bone.hide = False

def hide_selected_edit_bones(context):
    for pose_bone in context.selected_editable_bones:
        pose_bone.bone.hide = True

###########

def set_viewpoint(viewpoint='RIGHT'):
    bpy.ops.view3d.view_axis(type=viewpoint)

def set_view_perspective(context, enable: bool):
    if enable and not context.space_data.region_3d.is_perspective:
        bpy.ops.view3d.view_persportho()
    elif not enable and context.space_data.region_3d.is_perspective:
        bpy.ops.view3d.view_persportho()

def frame_selected():
    bpy.ops.view3d.view_selected(use_all_regions=False)

def frame_points(*points):
    return

def load_reproportion_image(img_name: str):
    from . reproportion.guide_reproportion import images_dir
    from os.path import exists, isfile, join
    path = join(images_dir, img_name)
    if not exists(path) or not isfile(path):
        return None
    return bpy.data.images.load(path, check_existing=True)

def load_datatransfer_image(img_name: str):
    from . datatransfer.guide_datatransfer import images_dir
    from os.path import exists, isfile, join
    path = join(images_dir, img_name)
    if not exists(path) or not isfile(path):
        return None
    return bpy.data.images.load(path, check_existing=True)

def hide_image(image):
    if image.name.startswith('.'):
        return
    image.name = '.' + image.name

def get_regiondata_view3d(context):
    if not context:
        context = bpy.context
    return context.region, context.space_data.region_3d

def spacecoordstoscreencoords(context, p):
    return view3d_utils.location_3d_to_region_2d(*get_regiondata_view3d(context), p, default=None)

def inside(p, _p, _s):
    return ((_p[0] + _s[0]) > p[0] > _p[0]) and ((_p[1] + _s[1]) > p[1] > _p[1])

def near(a, b, d):
    return abs(a[0] - b[0]) < d and abs(a[1] - b[1]) < d

def set_mode(mode: str):
    bpy.ops.object.mode_set(mode=mode)

def set_active_object(context, _object):
    _object.select_set(state=True)
    context.view_layer.objects.active = _object

def toggle_pose_x_mirror(context, state):
    if context.mode == 'POSE':
        context.pose_object.data.use_mirror_x = state

def move_global_z():
    bpy.ops.transform.translate('INVOKE_DEFAULT', orient_type ='GLOBAL', constraint_axis=(False, False, True), release_confirm=True)

def snap_selected_to_cursor():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

def cursor_to_selected():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            c = bpy.context.copy()
            c['area'] = area
        else:
            print("No View3D, aborting.")

    bpy.ops.view3d.snap_cursor_to_active(c)

def mirror_pose():
    bpy.ops.pose.copy()
    bpy.ops.pose.paste(flipped=True)

#### Object to Temp Collection

def blenrig_temp_link(object):
    temp_collection = bpy.data.collections.get("BlenRig_temp")
    temp_objects = object
    if bpy.context.scene.collection.children.find("BlenRig_temp") == -1:
        if temp_collection:
                bpy.context.scene.collection.children.link(temp_collection)
        else:
            temp_collection = bpy.data.collections.new("BlenRig_temp")
            bpy.context.scene.collection.children.link(temp_collection)
        for ob in temp_objects:
            try:
                temp_collection.objects.link(ob)
            except:
                pass

def blenrig_temp_unlink():
    temp_collection = bpy.data.collections.get("BlenRig_temp")
    if bpy.context.scene.collection.children.find("BlenRig_temp") != -1:
        for ob in temp_collection.objects:
            temp_collection.objects.unlink(ob)
        bpy.context.scene.collection.children.unlink(temp_collection)

face_rig_objects = []

def collect_facemask():
    face_rig_objects.clear()
    for ob in bpy.data.objects:
        if hasattr(ob, 'parent'):
            if ob.parent == bpy.context.active_object:
                if "FaceRigMesh" in ob.name:
                    face_rig_objects.append(ob)
    return face_rig_objects

mdef_cage_objects = []

def collect_cage():
    mdef_cage_objects.clear()
    for ob in bpy.data.objects:
        if "MdefCage" in ob.name:
            mdef_cage_objects.append(ob)
    return mdef_cage_objects

mdef_weights_model_objects = []

def collect_mdef_weights_model():
    mdef_weights_model_objects.clear()
    for ob in bpy.data.objects:
        if "MDefWeightsModel" in ob.name:
            mdef_weights_model_objects.append(ob)
    return mdef_weights_model_objects

#### Local View

def switch_out_local_view():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            space = area.spaces[0]
            bpy.ops.view3d.localview()
            if space.local_view: #check if using local view
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region} #override context
                        bpy.ops.view3d.localview(override) #switch to global view

#### Deselect all objects
def deselect_all_objects(context):
    if context.mode != 'OBJECT':
        set_mode('OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

### Check if object has modifiers
def check_mod_type(mod_type):
    active = bpy.context.active_object
    if hasattr(active, 'modifiers'):
        for mod in active.modifiers:
            if hasattr(mod, 'type'):
                if mod.type == mod_type:
                    return True

def check_mod_type_name(mod_type, mod_name):
    active = bpy.context.active_object
    if hasattr(active, 'modifiers'):
        for mod in active.modifiers:
            if hasattr(mod, 'type'):
                if mod.type == mod_type:
                    if mod.name == mod_name:
                        return True

#### Shapekey Creation
def add_shapekey(context, shape_name):
    ob=bpy.context.object
    if hasattr(ob, 'data') and hasattr(ob.data, 'shape_keys'):
        if hasattr(ob.data.shape_keys, 'key_blocks'):
            shapekeys = ob.data.shape_keys.key_blocks
            if shapekeys.find('Basis') == -1:
                Basis = ob.shape_key_add(from_mix=False)
                Basis.name = 'Basis'
            if shape_name in shapekeys:
                index = ob.data.shape_keys.key_blocks.find(shape_name)
                ob.active_shape_key_index = index
                ob.data.shape_keys.key_blocks[index].value = 1.0
                ob.use_shape_key_edit_mode = True
                #Rename Shapekeys Datablock
                ob.data.shape_keys.name = 'ShapeKeys'
            else:
                new_shape = ob.shape_key_add(from_mix=False)
                new_shape.name = shape_name
                if shape_name in shapekeys:
                    index = ob.data.shape_keys.key_blocks.find(shape_name)
                    ob.active_shape_key_index = index
                    ob.data.shape_keys.key_blocks[index].value = 1.0
                    ob.use_shape_key_edit_mode = True
                    #Rename Shapekeys Datablock
                    ob.data.shape_keys.name = 'ShapeKeys'
        #If no Shapekeys present
        else:
            Basis = ob.shape_key_add(from_mix=False)
            Basis.name = 'Basis'
            shapekeys = ob.data.shape_keys.key_blocks
            new_shape = ob.shape_key_add(from_mix=False)
            new_shape.name = shape_name
            #Rename Shapekeys Datablock
            ob.data.shape_keys.name = 'ShapeKeys'
            if shape_name in shapekeys:
                index = ob.data.shape_keys.key_blocks.find(shape_name)
                ob.active_shape_key_index = index
                ob.data.shape_keys.key_blocks[index].value = 1.0
                ob.use_shape_key_edit_mode = True

### Add Drivers
driver_data_path = []
driver_array_index = []

def add_drivers(object_item,d_data_path, d_array_index, array_check, d_extrapolation, d_hide, d_lock, d_mute, d_expression, d_type):
    driver_data_path[:] = []
    driver_array_index[:] = []
    if array_check == 'no_array':
        fcurve = object_item.driver_add(d_data_path)
    if array_check == 'array':
        fcurve = object_item.driver_add(d_data_path, d_array_index)
    fcurve.extrapolation = d_extrapolation
    fcurve.hide = d_hide
    fcurve.lock = d_lock
    fcurve.mute = d_mute
    if d_type == 'SCRIPTED':
        fcurve.driver.expression = d_expression
    fcurve.driver.type = d_type
    for m in fcurve.modifiers:
        fcurve.modifiers.remove(m)
    driver_data_path.append(fcurve.data_path)
    driver_array_index.append(fcurve.array_index)
    return (fcurve)

def add_shapekeys_driver(object_item,d_data_path, d_type, d_expression):
    driver_data_path[:] = []
    driver_array_index[:] = []
    fcurve = object_item.driver_add(d_data_path)
    fcurve.extrapolation = 'CONSTANT'
    fcurve.hide = False
    fcurve.lock = False
    fcurve.mute = False
    fcurve.driver.type = d_type
    if d_type == 'SCRIPTED':
        fcurve.driver.expression = d_expression
    for m in fcurve.modifiers:
        fcurve.modifiers.remove(m)
    driver_data_path.append(fcurve.data_path)
    driver_array_index.append(fcurve.array_index)
    return (fcurve)


def add_vars(current_driver, v_name, v_type, t_id, t_bone_target, t_data_path, t_transform_space, t_transform_type, t_rotation_mode):
    var = current_driver.driver.variables.new()
    var.name = v_name
    var.type = v_type
    target = var.targets[0]
    target.id = t_id
    if v_type == 'SINGLE_PROP':
        target.data_path = t_data_path
    if v_type == 'TRANSFORMS':
        target.bone_target = t_bone_target
        target.transform_space = t_transform_space
        target.transform_type = t_transform_type
        target.rotation_mode = t_rotation_mode

def add_vars_shapekeys(current_driver, v_name, ob_shapkeys, shape_name):
    var = current_driver.driver.variables.new()
    var.name = v_name
    var.type = 'SINGLE_PROP'
    target = var.targets[0]
    target.id_type = 'KEY'
    target.id = bpy.data.shape_keys[ob_shapkeys]
    target.data_path = 'key_blocks["' + shape_name + '"].value'


def add_mod_generator(current_driver, m_type, m_blend_in, m_blend_out, m_frame_start, m_frame_end, m_mode, m_mute, m_poly_order, m_use_additive, m_use_influence, m_use_restricted_range, m_co_0, m_co_1):
    mod = current_driver.modifiers.new(m_type)
    mod.blend_in = m_blend_in
    mod.blend_out = m_blend_out
    mod.frame_start = m_frame_start
    mod.frame_end = m_frame_end
    mod.mode = m_mode
    mod.mute = m_mute
    mod.poly_order = m_poly_order
    mod.use_additive = m_use_additive
    mod.use_influence = m_use_influence
    mod.use_restricted_range = m_use_restricted_range
    mod.coefficients[0] = m_co_0
    mod.coefficients[1] = m_co_1

def add_mod_generator_angle(current_driver, angle):
    mod = current_driver.modifiers.new('GENERATOR')
    mod.blend_in = 0.0
    mod.blend_out = 0.0
    mod.frame_start = 0.0
    mod.frame_end = 0.0
    mod.mode = 'POLYNOMIAL'
    mod.mute = False
    mod.poly_order = 1
    mod.use_additive = False
    mod.use_influence = False
    mod.use_restricted_range = False
    mod.coefficients[0] = 0.0
    mod.coefficients[1] = 1.0/radians(angle)

def add_mod_generator_location(current_driver, loc):
    mod = current_driver.modifiers.new('GENERATOR')
    mod.blend_in = 0.0
    mod.blend_out = 0.0
    mod.frame_start = 0.0
    mod.frame_end = 0.0
    mod.mode = 'POLYNOMIAL'
    mod.mute = False
    mod.poly_order = 1
    mod.use_additive = False
    mod.use_influence = False
    mod.use_restricted_range = False
    mod.coefficients[0] = 0.0
    mod.coefficients[1] = 1.0/loc

def add_mod_generator_location_offset(current_driver, x_offset, loc):
    mod = current_driver.modifiers.new('GENERATOR')
    mod.blend_in = 0.0
    mod.blend_out = 0.0
    mod.frame_start = 0.0
    mod.frame_end = 0.0
    mod.mode = 'POLYNOMIAL'
    mod.mute = False
    mod.poly_order = 1
    mod.use_additive = False
    mod.use_influence = False
    mod.use_restricted_range = False
    mod.coefficients[0] = x_offset
    mod.coefficients[1] = 1.0/loc

### Check if Shapekey has a Driver
def check_shapekey_driver(shape_name):
    active = bpy.context.active_object
    if hasattr(active, 'data') and hasattr(active.data, 'shape_keys') and hasattr(active.data.shape_keys, 'key_blocks'):
        if hasattr(active.data.shape_keys.key_blocks, 'data') and hasattr(active.data.shape_keys.key_blocks.data, 'animation_data'):
            if hasattr(active.data.shape_keys.key_blocks.data.animation_data, 'drivers'):
                for driver in active.data.shape_keys.key_blocks.data.animation_data.drivers:
                    if shape_name in driver.data_path:
                        return True

### Get Local Transforms of Bone For Driver Updater (Code by Niabot)
def bone_local_transforms(armature, bname, transform_type):
    bone        = armature.data.bones[bname]
    bone_ml     = bone.matrix_local
    bone_pose   = armature.pose.bones[bname]
    bone_pose_m = bone_pose.matrix

    if bone.parent:

        parent        = bone.parent
        parent_ml     = parent.matrix_local
        parent_pose   = bone_pose.parent
        parent_pose_m = parent_pose.matrix

        object_diff = parent_ml.inverted() @ bone_ml
        pose_diff   = parent_pose_m.inverted() @ bone_pose_m
        local_diff  = object_diff.inverted() @ pose_diff

    else:

        local_diff = bone_ml.inverted() @ bone_pose_m

    if transform_type == 'rot_x':
        transform = local_diff.to_euler('ZYX')[0]
    if transform_type == 'rot_y':
        transform = local_diff.to_euler('XZY')[1]
    if transform_type == 'rot_z':
        transform = local_diff.to_euler('XYZ')[2]
    if transform_type == 'loc_x':
        transform = local_diff.to_translation()[0]
    if transform_type == 'loc_y':
        transform = local_diff.to_translation()[1]
    if transform_type == 'loc_z':
        transform = local_diff.to_translation()[2]
    if transform_type == 'scale_x':
        transform = local_diff.to_scale()[0]
    if transform_type == 'scale_y':
        transform = local_diff.to_scale()[1]
    if transform_type == 'scale_z':
        transform = local_diff.to_scale()[2]
    return transform
