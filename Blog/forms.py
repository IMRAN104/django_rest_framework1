from django import forms


class BlogPostForm(forms.Form):
    """BlogPostForm definition."""

    # TODO: Define form fields here
    title = forms.CharField(max_length=50, required=True)
    slug = forms.SlugField(allow_unicode=True, required=True)
    content = forms.CharField(max_length=2000, required=False)
