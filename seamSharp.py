bl_info = {
    "name": "SeamSharp",
    "category": "Object",
    "blender": (2, 93, 3),
}
import bpy

class SeamSharp(bpy.types.Operator):
    """Mark seam all edges that are marked sharp"""
    bl_idname = "object.seam_sharp"
    bl_label = "Seam sharp"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.active_object
        
        for edge in filter(lambda e: e.use_edge_sharp, obj.data.edges):
            edge.use_seam=True

        return {'FINISHED'}

def register():
    print('installing SeamSharp')
    bpy.utils.register_class(SeamSharp)
    print('Success!!')

def unregister():
    bpy.utils.unregister_class(SeamSharp)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()