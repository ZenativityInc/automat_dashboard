from django import forms

class BatchSearchForm(forms.Form):
    batch_ids = forms.CharField(label='Input batch ID(s)',
                                widget=forms.TextInput(attrs={'data-toggle': 'tooltip', 'data-placement': 'top',
                                                              'title': 'Enter comma-separated batch IDs or ranges (e.g. 1, 3-5, 7)'}))

    def clean_batch_ids(self):
        data = self.cleaned_data['batch_ids'].strip()
        batches = []

        for item in data.split(','):
            item = item.strip()
            if '-' in item:
                start, end = item.split('-')
                batches += list(range(int(start), int(end)+1))
            else:
                batches.append(int(item))

        return batches
