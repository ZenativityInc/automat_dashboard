import re
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from .models import LiquidMasterTable
from .utils import *
from .forms import BatchSearchForm

def BatchID(request):
    df = None
    form_reset = request.POST.get('form_reset') == 'True'
    chart1 = None
    chart2 = None
    chart3 = None
    search_form = BatchSearchForm(request.POST or None)
    if request.method == 'POST':
        if form_reset:
            search_form = BatchSearchForm()
            chart1 = None
            chart2 = None
            chart3 = None
        else:
            if search_form.is_valid():
                batch_ids = search_form.cleaned_data['batch_ids']
                graph_qs = LiquidMasterTable.objects.filter(lab_batch__in=batch_ids)

                if len(graph_qs) > 0:
                    df = pd.DataFrame.from_records(graph_qs.values())
                    df['conductivity'] = round(df['conductivity'] * 1000, 4)
                    chart1 = get_chart(df, 'electrolyte_id', 'conductivity', 'Conductivity', 'lab_batch','Conductivity [mS/cm]')
                    chart2 = get_chart(df, 'electrolyte_id', 'voltage', 'Voltage', 'lab_batch', 'Voltage')
                    chart3 = get_chart(df, 'electrolyte_id', 'lce', 'LCE', 'lab_batch', 'LCE')
                else:
                    messages.warning(request, "Apparently no data available...")
    context = {
        'search_form': search_form,
        'df': df,
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3,

    }
    return render(request, 'graphs.html',  context)
