from django import forms
from gallery.models import Reviews, Attachment
from multiupload.fields import MultiMediaField


SORT_BY = (
    ('Newest', 'Newest'),
    ('Oldest', 'Oldest'),
    ('HighRated', 'Highest Rated'),
    ('LowRated', 'Lowest Rated'),
    )

# This form uses the django-multiupload app.
class reviewForm(forms.ModelForm):
    
    files = MultiMediaField(min_num=1, max_num=3, max_file_size=1024*1024*10, media_type="image")
    
    class Meta:
        model = Reviews
        fields = ['rating', 'title', 'comment']
        exclude = ['username', 'review_left', 'order_number', 'user_int'] 
    
    # When the user submits the form and it validates, it collects each uploaded/selected image files 
    # and references them to the current instance being submitted. 
    def save(self, commit=True):
        instance = super(reviewForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, review_table=instance)
        return instance

# Used to order the reviews.
class sortOrder(forms.Form):
    order = forms.ChoiceField(choices=SORT_BY,
    widget=forms.Select(attrs={'class': 'form-control'}))