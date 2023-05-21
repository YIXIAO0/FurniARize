import FbxCommon  # Make sure you have installed the Autodesk FBX SDK

def save_to_fbx(coords, rgb=None, faces=None, output_path='output.fbx'):
    manager, scene = FbxCommon.InitializeSdkObjects()

    # Create the mesh
    mesh_name = "Mesh"
    mesh = FbxMesh.Create(scene, mesh_name)

    # Set the vertex coordinates
    control_points = mesh.GetControlPoints()
    for i, coord in enumerate(coords):
        control_points.Add(FbxVector4(coord[0], coord[1], coord[2]))

    # Set the vertex colors if RGB values are provided
    if rgb is not None:
        vertex_colors = mesh.GetElementVertexColor()
        vertex_colors.SetMappingMode(FbxGeometryElement.eByControlPoint)
        vertex_colors.SetReferenceMode(FbxGeometryElement.eDirect)

        color_array = vertex_colors.GetDirectArray()
        for i, color in enumerate(rgb):
            color_array.Add(FbxColor(color[0], color[1], color[2], 1.0))

    # Set the faces if provided
    if faces is not None:
        for face in faces:
            mesh.BeginPolygon()
            for vertex_index in face:
                mesh.AddPolygon(vertex_index)
            mesh.EndPolygon()

    # Create the node and add the mesh to it
    node = FbxNode.Create(scene, mesh_name)
    node.SetNodeAttribute(mesh)
    scene.GetRootNode().AddChild(node)

    # Save the scene to an FBX file
    exporter = FbxExporter.Create(manager, "")
    exporter.Initialize(output_path, -1)
    exporter.Export(scene)
    exporter.Destroy()

    # Cleanup
    manager.Destroy()

# Example usage
coords = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
rgb = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
faces = [[0, 1, 2]]
save_to_fbx(coords, rgb, faces, 'output.fbx')
# Make sure to replace 'output.fbx' with the desired output path for your FBX file. Also, ensure that you have the Autodesk FBX SDK installed and properly configured with the necessary dependencies before running this code.

