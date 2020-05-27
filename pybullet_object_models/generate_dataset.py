import os
import pickle
import numpy as np

# Generate names of directories of superquadric models
shape_values = [i/10 for i in range(1, 20, 2)]

min_dim, max_dim = 0.02, 0.12
max_grasp_dim = 0.04
dim_values = [i/100 for i in range(int(min_dim*100), int(max_dim*100))]

max_grasp_dim_idx = dim_values.index(max_grasp_dim)

directories = []
for l5 in shape_values:
    for l4 in shape_values:
        for l1 in dim_values:
            for l2 in dim_values[:max_grasp_dim_idx+1]:
                for l3 in dim_values:

                    # setup dir
                    obj_dir = "sq_" + str(l1) + "_" + str(l2) + "_" + str(l3) + "_" + str(l4) + "_" + str(l5)

                    directories.append(obj_dir)

# shuffle list of directories
np.random.shuffle(directories)

# split dataset into k folds
k = 4
folds = np.array_split(directories, k)

# save
for i, fold_k in enumerate(folds):

    try:
        file = open("superquadric_fold_" + str(i) + ".pkl", 'wb')
        pickle.dump(fold_k, file)
        print("superquadric_fold_{}.pkl saved".format(i))

    except Exception:
        print("Error when writing file")


# with open ('dataset.pkl', 'rb') as f:
#     itemlist = pickle.load(f)
