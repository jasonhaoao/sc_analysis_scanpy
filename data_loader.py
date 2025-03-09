import scanpy as sc

def load_data(file_path):
    print(f"loading data from {file_path}")
    adata = sc.read_h5ad(file_path)
    return adata