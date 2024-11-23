from django import forms
from . import models

class HeaderTopForm(forms.ModelForm):
    class Meta:
        model = models.HeaderTop
        fields = ['text','icon','adress']
        
class HeaderCenterForm(forms.ModelForm):
    class Meta:
        model = models.HeaderCenter
        fields = ['name','adress']
        
class HeaderEndForm(forms.ModelForm):
    class Meta:
        model = models.HeaderEnd
        fields = ['text_top','text_big','text_end','but_name']
        
class MainOneTopForm(forms.ModelForm):
    class Meta:
        model = models.MainOneTop
        fields = ['name']

class MainOneLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainOneLeft
        fields = ['name','text','but_name','but_adress']

class MainOneRightForm(forms.ModelForm):
    class Meta:
        model = models.MainOneRight
        fields = ['pay','img','number','name','text']
