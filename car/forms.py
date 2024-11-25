from car.models import CommentModel
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = None
