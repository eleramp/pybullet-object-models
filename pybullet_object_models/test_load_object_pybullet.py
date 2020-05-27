import os
import time
import pybullet_object_models
from pybullet_object_models import ycb_objects
from pybullet_object_models import graspa_layouts
from pybullet_object_models import superquadric_objects

import pybullet as p
import pybullet_data

# Open GUI and set pybullet_data in the path
p.connect(p.GUI)
p.resetDebugVisualizerCamera(3, 90, -30, [0.0, -0.0, -0.0])
p.setTimeStep(1. / 240)

# Load plane contained in pybullet_data
planeId = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"))

# Set gravity for simulation
p.setGravity(0, 0, -9.8)

flags = p.URDF_USE_INERTIA_FROM_FILE

obj_id = p.loadURDF(os.path.join(superquadric_objects.getDataPath(), 'sq_0.1_0.02_0.1_0.9_0.9', "model.urdf"), [1., 0.0, 0.8], flags=flags)

while 1:
    p.stepSimulation()
    time.sleep(1./240)
