from django import forms

from .models import Document

#表格的資料內容並回傳到資料庫
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
