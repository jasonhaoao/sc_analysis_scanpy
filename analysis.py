def run_analysis(adata, n_neighbors, n_pcs, resolution):
    print("run analysis")
    sc.tl.pca(adata, svd_solver="arpack")
    sc.pp.neighbors(adata, n_neighbors = n_neighbors, n_pcs = n_pcs)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution = resolution)
    return adata