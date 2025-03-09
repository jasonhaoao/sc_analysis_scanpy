def processing_data(adata, min_genes, min_cells, target_sum, n_top_genes, min_mean, max_mean, min_disp):
    print("processing data")
    sc.pp.filter_cells(adata, min_genes = min_genes)
    sc.pp.filter_genes(adata, min_cells = min_cells)
    sc.pp.normalize_total(adata, target_sum = target_sum)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, min_mean = min_mean, max_mean = max_mean, min_disp = min_disp, n_top_genes = n_top_genes)
    return adata