from django import forms
from gallery.models import reviews, attachment
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class reviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ['username', 'rating', 'comment']
        
        
        files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

        def save(self, commit=True):
            instance = super(reviewForm, self).save(commit)
            for each in self.cleaned_data['files']:
                attachment.objects.create(file=each, message=instance)
    
            return instance