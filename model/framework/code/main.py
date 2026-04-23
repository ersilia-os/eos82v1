# imports
import os
import sys
import torch
import numpy as np
from ersilia_pack_utils.core import read_smiles, write_out

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)

from load import load_smi_ted

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read input
_, smiles_list = read_smiles(input_file)

model_smi_ted = load_smi_ted()

# run model
with torch.no_grad():
    df_embeddings_train = model_smi_ted.encode(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(df_embeddings_train)
assert input_len == output_len

outputs = df_embeddings_train.to_numpy() #obtain results as numpy array
num_dims = df_embeddings_train.shape[1]
header = [f"feat_{str(i).zfill(3)}" for i in range(num_dims)]

write_out(outputs, header, output_file, np.float32)
