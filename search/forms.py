from django import forms

SEARCH_TYPE_CHOICE = [(i, str(i)) for i in range(1, 3)]


class SearchForm(forms.Form):
    keyword_q = forms.CharField(required=True)
    type_search = forms.TypedChoiceField(choices=SEARCH_TYPE_CHOICE, coerce=int, required=True)

    def clean_keyword_q(self):
        keyword_q = self.cleaned_data['keyword_q']
        if not all(keyword_q.isalnum() or keyword_q.isspace() for keyword_q in keyword_q):
            raise forms.ValidationError(
                'This field can only contain letters and numbers.')
        return keyword_q
