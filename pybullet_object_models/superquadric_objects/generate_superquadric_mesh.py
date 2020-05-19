import pygalmesh
import meshio

params = [1,1,1,1,1]

l1 = params[0]
l2 = params[1]
l3 = params[2]
l4 = params[3]
l5 = params[4]

file_name = "sq_" + str(l1) + "_" + str(l2) + "_" + str(l3) + "_" + str(l4) + "_" + str(l5) + ".obj"

class SQ(pygalmesh.DomainBase):
    def __init__(self):
        super().__init__()

    def eval(self, x):
        return (( (x[0] / l1) ** 2) ** (1/l5) + ( (x[1] / l2) ** 2) ** (1/l5) )** (l5/l4) \
                + ( (x[2] / l3) ** 2) ** (1/l4) - 1

    def get_bounding_sphere_squared_radius(self):
        return 10

d = SQ()

mesh = pygalmesh.generate_surface_mesh(
    d,
    angle_bound=10,
    radius_bound=0.05,
    distance_bound=0.05
)

meshio.write(file_name, mesh)
