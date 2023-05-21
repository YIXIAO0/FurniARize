import furniARize
import os
import shutil
import time
import subprocess
# Path to furniARize.py python script (this file)
python_script = "C:\\Users\\16084\\Documents\\ECE209AS\\shap-e\\furniARize.py"

# Path to the Unity Assets folder for the new user
new_unity_assets_folder = os.path.join("C:\\Users\\16084\\Documents\\ECE209AS\\shap-e\\FurniARize\\Assets\\Models", furniARize.username)
os.makedirs(new_unity_assets_folder, exist_ok = True)

# Copy the four .obj files to the new Assets folder 
for i in range(4):
    # Path to the .obj file that the python script produces
    obj_file = os.path.join("C:\\Users\\16084\\Documents\\ECE209AS\\shap-e", furniARize.username, f"example_mesh_{i}.ply")
    # Make sure the script has finished and the .obj file exists before trying to move it
    # Wait until the Python script completes and the .obj file is created
    while not os.path.exists(obj_file):
        time.sleep(1)
    # Move the .obj file to the Unity project's Assets folder
    shutil.copy(obj_file, new_unity_assets_folder)
