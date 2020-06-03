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

# split dataset into k folds and keep 3 folds for training, 1 for validation, 1 for testing
k = 5
folds = np.array_split(directories, k)
train_set = np.append(folds[0], [folds[1], folds[2]])
eval_set = folds[3]
test_set = folds[4]

# Train set
try:
    file = open("train.pkl", 'wb')
    pickle.dump(train_set, file)
    print("train.pkl saved")

except Exception:
    print("Error when writing train.pkl")

# Eval set
try:
    file = open("eval.pkl", 'wb')
    pickle.dump(eval_set, file)
    print("eval.pkl saved")

except Exception:
    print("Error when writing eval.pkl")

# Eval set
try:
    file = open("test.pkl", 'wb')
    pickle.dump(test_set, file)
    print("test.pkl saved")

except Exception:
    print("Error when writing test.pkl")


# with open ('dataset.pkl', 'rb') as f:
#     itemlist = pickle.load(f)
