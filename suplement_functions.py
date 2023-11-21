import matplotlib.pyplot as plt
import seaborn as sns


def clear_barplot(
    ax,
    percent=0,
    vertical=True,
    plot_title="",
    pad_top=13,
    pad_bottom=2,
    plot_xlabel="",
    plot_ylabel="",
    legend_visibility=False,
):

    ax.set(xlabel=plot_xlabel, ylabel=plot_ylabel)
    ax.set_title(plot_title, color="#3c4b6b", fontsize=14)
    ax.tick_params(
        axis="both",
        which="both",
        length=0,
    )
    
    if not legend_visibility:
        ax.legend([],frameon=legend_visibility)
    
    if vertical:
        ax.set_yticklabels([])
        sns.despine(left=True)
    else:
        ax.set_xticklabels([])
        sns.despine(bottom=True)

    # Plot on top of the bars
    for c in ax.containers:
        ax.bar_label(c, padding=pad_top, color="#3c4b6b", fontsize=10.5)
    if percent != 0:
        ax.bar_label(
            ax.containers[0],
            padding=pad_bottom,
            labels=percent,
            color="#55185D",
            fontsize=9,
        )
