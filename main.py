import argparse
from .data_loader import load_data
from .preprocessing import preprocess_data
from .analysis import run_analysis
from .visualization import plot_umap

def main():
    parser = argparse.ArgumentParser(description="Run single-cell analysis pipeline.") # 这里创建一个 argparse.ArgumentParser 对象，用于解析命令行参数，description参数描述了程序的功能
    parser.add_argument("--input", type=str, required=True, help="Path to input h5ad file.") # 这里添加的是命令行参数、输入值的类型、是否必填/默认值是多少、帮助信息等属性
    parser.add_argument("--output", type=str, required=True, help="Path to output UMAP plot.")
    parser.add_argument("--min_genes", type=int, default=2000, help="Minimum number of genes per cell, defult = 2000.")
    parser.add_argument("--min_cells", type=int, default=3, help="Minimum number of cells per gene, defult = 3.")
    parser.add_argument("--target_sum", type=float, default=1e4, help="Target sum for normalization, defult = 1e4.")
    parser.add_argument("--n_top_genes", type=int, default=2000, help="Number of top genes for highly variable genes, default=2000.")
    parser.add_argument("--min_mean", type=float, default=0.0125, help="Minimum for mean highly variable genes, default=0.0125.")
    parser.add_argument("--max_mean", type=float, default=3, help="Maximum mean for highly variable genes, default=3.")
    parser.add_argument("--min_disp", type=float, default=0.5, help="Minimum dispersion for highly variable genes, default=0.5.")
    parser.add_argument("--n_neighbors", type=int, default=10, help="Number of neighbors for PCA, default=10.")
    parser.add_argument("--n_pcs", type=int, default=40, help="Number of PCs for PCA, default=40.")
    parser.add_argument("--resolution", type=float, default=0.8, help="Resolution for Leiden clustering, default=0.8.")
    args = parser.parse_args() # 解析命令行参数，将上面的东西打包起来，返回一个命名空间对象 args，其中包含所有解析后的参数值

    # Load data
    adata = load_data(args.input)

    # Preprocess data
    adata = preprocess_data(
        adata,
        min_genes=args.min_genes,
        min_cells=args.min_cells,
        target_sum=args.target_sum,
        n_top_genes=args.n_top_genes,
        min_mean=args.min_mean,
        max_mean=args.max_mean,
        min_disp=args.min_disp
    )

    # Run analysis
    adata = run_analysis(
        adata,
        n_neighbors=args.n_neighbors,
        n_pcs=args.n_pcs,
        resolution=args.resolution
    )

    # Plot UMAP
    plot_umap(adata, args.output)

if __name__ == "__main__":
    main()
# 当脚本被直接运行时，调用 main 函数