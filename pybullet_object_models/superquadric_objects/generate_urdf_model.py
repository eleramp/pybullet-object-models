import os

def get_urdf_str(mesh_dir, scale_values):
    urdf_str = ("""
<robot name="model.urdf">
  <link name="base_link">
    <contact>
      <friction_anchor/>
      <lateral_friction value="0.8"/>
      <spinning_friction value="0.001"/>
      <rolling_friction value="0.001"/>
      <contact_cfm value="0.1"/>
      <contact_erp value="1.0"/>
    </contact>
    <inertial>
      <origin xyz="0 0 0" />
      <mass value="0.1" />
      <inertia ixx="1e-3" ixy="0" ixz="0" iyy="1e-3" iyz="0" izz="1e-3"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0"/>
      <geometry>
        <mesh filename="%s/model.obj" scale="%s %s %s"/>
      </geometry>
      <material name="white">
        <color rgba="1. 1. 1. 1."/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0"/>
      <geometry>
        <mesh filename="%s/model.obj" scale="%s %s %s"/>
      </geometry>
    </collision>
  </link>
</robot>
""") % (mesh_dir, scale_values[0], scale_values[1], scale_values[2], mesh_dir, scale_values[0], scale_values[1], scale_values[2])
    return urdf_str


# Write all urdf strings
shape_values = [i/10. for i in range(1, 20, 2)]

min_dim, max_dim = 0.02, 0.12
max_grasp_dim = 0.04

dim_values = [i/100. for i in range(int(min_dim*100), int(max_dim*100))]

max_grasp_dim_idx = dim_values.index(max_grasp_dim)

count = 0
for l5 in shape_values:
    for l4 in shape_values:
        for l1 in dim_values:
            for l2 in dim_values[:max_grasp_dim_idx+1]:
                for l3 in dim_values:
                    count += 1
                    # setup dirs
                    obj_dir = "sq_" + str(l1) + "_" + str(l2) + "_" + str(l3) + "_" + str(l4) + "_" + str(l5)
                    mesh_dir = "sq_" + str(max_dim) + "_" + str(max_dim) + "_" + str(max_dim) + "_" + str(l4) + "_" + str(l5)

                    # define the scale values to change the mesh dimension
                    scale_values = [round(l1/max_dim,2), round(l2/max_dim,2), round(l3/max_dim, 2)]

                    # create urdf
                    urdf_str = get_urdf_str(mesh_dir, scale_values)

                    # save
                    try:
                        os.makedirs(obj_dir, exist_ok=True)
                        f = open(os.path.join(obj_dir,"model.urdf"), 'w')
                        f.write(urdf_str)
                        print("urdf model saved in {}".format(os.path.join(obj_dir,"model.urdf")))

                    except Exception:
                        print("Error: cannot save urdf file at {}".format(os.path.join(obj_dir,"model.urdf")))

print("count {}".format(count))
