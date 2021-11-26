import matplotlib.pyplot as plt

def init_plot():
    fig, axs = plt.subplots(2, 3) # 2 rows, 3 cols
    fig.delaxes(axs[1,2])

    axs[0, 0].set(xlabel = 'graph size')
    axs[0, 1].set(xlabel = 'graph diameter')
    axs[0, 2].set(xlabel = 'path distance')
    axs[1, 0].set(xlabel = 'milestone distance')
    axs[1, 1].set(xlabel = 'milestone count')

    return fig, axs

def process_results(size, diameter, path_distance, milestone_distance, milestone_count, steps, steps_dfs):

    fig, axs = init_plot()

    axs[0, 0].scatter(size, steps, color='blue', label='pbg')
    axs[0, 0].scatter(size, steps_dfs, color='red', label='dfs')

    axs[0, 1].scatter(diameter, steps, color='blue', label='pbg')
    axs[0, 1].scatter(diameter, steps_dfs, color='red', label='dfs')

    axs[0, 2].scatter(path_distance, steps, color='blue', label='pbg')
    axs[0, 2].scatter(path_distance, steps_dfs, color='red', label='dfs')

    axs[1, 0].scatter(milestone_distance, steps, color='blue', label='pbg')
    axs[1, 0].scatter(milestone_distance, steps_dfs, color='red', label='dfs')

    axs[1, 1].scatter(milestone_count, steps, color='blue', label='pbg')
    axs[1, 1].scatter(milestone_count, steps_dfs, color='red', label='dfs')

    for ax in axs.flat:
        ax.set(ylabel='setps')
        ax.legend(loc='best')

    plt.show()
