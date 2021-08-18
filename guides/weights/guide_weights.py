from os.path import dirname, join
from .. weights.guide_weights_actions import *

images_dir = join(dirname(__file__), 'images')

GUIDE_STEPS_WEIGHTS = (
    #Intro
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Weights Guide Intro',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "In this Guide you will be able to adjust the Character's and Mdef Cage Weights if needed. You will also be able to adjust the values of the Volume Preservation Bones and the Realistic Joints values to simulate Sekeltal Structure volume in the Joints. Keep in mind that this will be the initial deformation setup, if you need to fine tune it, you will be able to do it in the Shapekeys Guide",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Intro
    },
    #Ankle Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Ankle',
            'ES': 'Tobillo'
            },
        'texto': {
            'EN': "Check the Ankle deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Realistic Joints and Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Ankle
    },
    #Foot Toe Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Foot Toe',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the 'Foot Toe joints' deformation. Change the active Joint with the 'Set Joint Number' Button. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Realistic Joints and Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Foot_Toe
    },
    #Knee Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Knee',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Knee deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Realistic Joints and Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Knee
    },
    #Thigh Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Thigh',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Thigh deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Thigh
    },
    #Torso Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Torso deformation. Change the active Joint with the 'Set Joint Number' Button. Scroll through the key Poses with the 'Set Joint Transform' slider. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Torso
    },
    #Neck Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Neck',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Neck deformation. Change the active Joint with the 'Set Joint Number' Button. Scroll through the key Poses with the 'Set Joint Transform' slider. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Neck
    },
    #Clavicle Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Clavicle',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Clavicle deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Clavicle
    },
    #Arm Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Arm / Shoulder',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Shoulder deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Shoulder
    },
    #Forearm Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Elbow',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Elbow deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Realistic Joints and Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Elbow
    },
    #Wrist Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Wrist',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Wrist deformation. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Realistic Joints and Volume Preservation values first. Select the Character's Mesh and enhance deformation with the 'Edit Corrective Smooth Vgroup' Button. If you need to adjust the weights press the 'Toggle Weight Painting' button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Cage_Wrist
    },
    #Character Mesh Wrist Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Hands Mdef Group',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the 'no_mdef' Vertex Group to define the area of influence of the Mesh Deform and the Armature Modifier. Hands should have full influence of this group. Transition should happen at the Wrist area.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Wrist
    },
    #Hand Volume Preservation Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Hands General VP & RJ Values',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Define the general values of Realistic Joints and Volume Preservation for the hands. Scroll through the key Poses with the 'Set Joint Transform' slider.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Hand_VP
    },
    #Fingers 1 Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Fings_1
    },
    #Fingers 1 Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Palm',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the Weights of the Palm and the first Joint of the Fingers. Change the active Finger with the 'Set Joint Number' Button. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Volume Preservation values first",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Fings_2
    },
    #Head Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Fingers',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the Weights of the Fingers. Change the active Joint with the 'Set Joint Number' Button. Scroll through the key Poses with the 'Set Joint Transform' slider. Adjust the Volume Preservation values first. Enhance deformation with the 'Select Corrective Smooth Vgroup' Button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Head
    },
    #Head Joints Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Head_Joints
    },
    #Ear Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Ears
    },
    #Eyebrows Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Eyebrows
    },
    #Eye Sockets
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Eye_Socket
    },
    #Eyelids Poses
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Eyelids
    },
    #Cheeks
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Cheeks
    },
    #Nose
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Nose
    },
    #Mouth
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Mouth
    },
    #Inner Mouth
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': WEIGHTS_Char_Inner_Mouth
    },
)




