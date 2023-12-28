import matplotlib.pyplot as plt
from matplotlib import pyplot
import base64
from io import BytesIO
from matplotlib.ticker import MultipleLocator

def get_graph(df):
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png =buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph

# charts for 2 conditions
def get_chart(df, x_axis, y_axis, label, lab_batch, ylabel):
    pyplot.switch_backend('AGG')
    fig, axes = pyplot.subplots(figsize=(50, 20), dpi=65)
    fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

    # create a dictionary to map each batch to a color
    color_dict = {}
    for i, batch in enumerate(df[lab_batch].unique()):
        color_dict[batch] = plt.cm.get_cmap('tab20')(i / len(df[lab_batch].unique()))

    # plot each batch with a unique color
    if len(df[lab_batch].unique()) <= 2:
        for batch, color in color_dict.items():
            df_batch = df[df[lab_batch] == batch]
            axes.bar(df_batch[x_axis], df_batch[y_axis], label=f'Batch {batch}', color=color, alpha=0.8)
    else:
        for batch, color in color_dict.items():
            df_batch = df[df[lab_batch] == batch]
            axes.plot(df_batch[x_axis], df_batch[y_axis], label=f'Batch {batch}', marker='o', color=color,
                      markersize=20, linewidth=5)

    axes.grid()
    axes.set_xlabel('Electrolyte ID', fontsize=60)
    axes.set_ylabel(ylabel, fontsize=65)
    pyplot.setp(axes.get_xticklabels(), rotation=45, ha='right', size=35)
    pyplot.setp(axes.get_yticklabels(), size=55)
    # set the x-axis tick positions and labels
    x_ticks = range(0, len(df[x_axis]), 2)
    axes.set_xticks(x_ticks)
    x_tick_labels = [df[x_axis][i] for i in x_ticks]
    axes.set_xticklabels(x_tick_labels)
    pyplot.setp(axes.get_yticklabels(), size=55)
    # add legend outside the chart
    axes.legend(fontsize=50, loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)
    # add title
    axes.set_title(f'{label} ', fontsize=70)

    pyplot.tight_layout()
    chart = get_graph(df)
    return chart


def chart1(df):
    return get_chart(df, 'electrolyte_id', 'conductivity'*1000, 'Conductivity', 'lab_batch', 'Conductivity [mS/cm]')

def chart2(df):
    return get_chart(df, 'electrolyte_id', 'voltage', 'Voltage', 'lab_batch', 'Voltage')

def chart3(df):
    return get_chart(df, 'electrolyte_id', 'lce', 'LCE', 'lab_batch', 'LCE')
