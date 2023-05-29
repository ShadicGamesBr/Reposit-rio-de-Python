import aspose.threed as a3d

scene = a3d.Scene.from_file("Input.glb")
scene.save("Output.3ds")
