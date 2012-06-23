import floppyforms as forms

from lists.models import List


class ListForm(forms.ModelForm):


    class Meta:
        model = List
