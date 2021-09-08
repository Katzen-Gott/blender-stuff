bl_info = {
    "name": "Bevel&Subdiv",
    "category": "Object",
    "blender": (2, 93, 3),
}
import bpy

class BevelSubdiv(bpy.types.Operator):
    """Add Bevel and subdiv modifiers"""
    bl_idname = "object.bevel_subdivide"
    bl_label = "Bevel and subdivide"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.active_object
        
        # set bevel weight to 1 on sharp edges
        obj.data.use_customdata_edge_bevel = True
        for edge in filter(lambda e: e.use_edge_sharp, obj.data.edges):
            edge.bevel_weight=1
        
        # add bevel
        b = obj.modifiers.new('Bevel', 'BEVEL')
        b.segments = 2
        b.width = 0.005
        b.profile = 1
        b.limit_method = 'WEIGHT'
        
        # add a subsurf modifier
        m = obj.modifiers.new('Subsurf', 'SUBSURF')
        m.levels = 2
        # this turns on optimal display
        m.show_only_control_edges = True

        return {'FINISHED'}

def register():
    print('installing Bevel & Subdiv')
    bpy.utils.register_class(BevelSubdiv)
    print('Success!!')

def unregister():
    bpy.utils.unregister_class(BevelSubdiv)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()