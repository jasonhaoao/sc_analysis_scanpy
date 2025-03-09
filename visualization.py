import matplotlib.pyplot as plt

def plot_umap(adata, output_path):
    print("plotting UMAP")
    sc.pl.umap(adata, color = ['leiden'], show = False)
    plt.savefig(output_path)