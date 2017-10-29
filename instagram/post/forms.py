from django import forms

__all__ = (
    'PostForm'
)


class PostForm(forms.Form):
    photo = forms.ImageField()


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea,
    )