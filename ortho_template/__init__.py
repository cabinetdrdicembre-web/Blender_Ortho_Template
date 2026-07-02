bl_info = {
    "name": "Ortho Template",
    "author": "Cabinet Dr Dicembre + ChatGPT",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar",
    "description": "Orthodontic 5 Views Template",
    "category": "3D View",
}

import bpy

from . import panel


def register():

    panel.register()


def unregister():

    panel.unregister()


if __name__ == "__main__":
    register()
