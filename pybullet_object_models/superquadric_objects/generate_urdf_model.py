import os

def get_urdf_str():
    urdf_str = ("""
<robot name="model.urdf">
  <link name="base_link">
    <inertial>
      <origin xyz="0 0 0" />
      <mass value="0.1" />
      <inertia ixx="1e-3" ixy="0" ixz="0" iyy="1e-3" iyz="0" izz="1e-3"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0"/>
      <geometry>
        <mesh filename="model.obj" scale="1 1 1"/>
      </geometry>
    </visual>
    <collision>
      <origin xyz="0 0 0"/>
      <geometry>
        <mesh filename="model.obj" scale="1 1 1"/>
      </geometry>
    </collision>
  </link>
</robot>
""")
    return urdf_str


# Write all urdf strings
shape_values = [i/10 for i in range(1, 20, 2)]

for l5 in shape_values:
    for l4 in shape_values:

        l1 = l2 = l3 = 0.5

        obj_dir = "sq_" + str(l1) + "_" + str(l2) + "_" + str(l3) + "_" + str(l4) + "_" + str(l5)

        urdf_str = get_urdf_str()
        try:
            f = open(os.path.join(obj_dir,"model.urdf"), 'w')
            f.write(urdf_str)
        except Exception:
            print("Error")
