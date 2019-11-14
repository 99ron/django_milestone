from django import forms
from gallery.models import Reviews, Attachment
from multiupload.fields import MultiMediaField


class reviewForm(forms.ModelForm):
    
    files = MultiMediaField(min_num=1, max_num=3, max_file_size=1024*1024*10, media_type="image")
    
    class Meta:
        model = Reviews
        fields = ['rating', 'title', 'comment']
        exclude = ['username'] 
    
    def save(self, commit=True):
        instance = super(reviewForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, review_table=instance)
        return instance

        
        