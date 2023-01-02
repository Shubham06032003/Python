import matplotlib as plt
import numpy as np
from sklearn import datasets,linear_model
    
Diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
print(Diabetes.keys())