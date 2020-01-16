import os
from setuptools import setup, find_packages

setup_py_dir = os.path.dirname(os.path.realpath(__file__))
need_files = []
datadir = "ycb_objects_models_sim"

hh = setup_py_dir + "/" + datadir

for root, dirs, files in os.walk(hh):
  for fn in files:
    ext = os.path.splitext(fn)[1][1:]
    if ext and ext in 'urdf sdf xml stl ini obj mtl png'.split(
    ):
      fn = root + "/" + fn
      need_files.append(fn[1 + len(hh):])

setup(
  name="ycb-objects-models-sim",
  version="0.1",
  author="Elena Rampone",
  author_email="elena.rampone@iit.it",
  description="URDF-SDF models of textured YCB objects for simulation",
  license="LGPL",
  python_requires='>=3.5',
  keywords="urdf sdf models ycb objects simulation pybullet",
  packages=find_packages(),
  package_data={'ycb_objects_models_sim': need_files},
  url="https://github.com/eleramp/ycb-objects-models-sim",
)
