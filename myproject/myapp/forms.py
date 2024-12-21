from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# Header Start
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
        
        
class HeaderSliderForm(forms.ModelForm):
    class Meta:
        model = models.HeaderSlider
        fields = ['img','name','text']
# Header End
# Main One Start
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
# Main One End

# Main Two start
class MainTwoLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainTwoLeft
        fields = ['name','text','but_name','but_adress']

class MainTwoRightForm(forms.ModelForm):
    class Meta:
        model = models.MainTwoRight
        fields = ['name','text']
        
# Main Two End

# Main Thee Start

class MainTheeTopForm(forms.ModelForm):
    class Meta:
        model = models.MainTheeTop
        fields = ['name']
        
class MainTheeContentForm(forms.ModelForm):
    class Meta:
        model = models.MainTheeContent
        fields = ['img','name','pay']



# Main Thee End

# Main Four Start
class MainFourTopForm(forms.ModelForm):
    class Meta:
        model = models.MainFourTop
        fields = ['name']

class MainFourLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainFourLeft
        fields = ['name','number','nametwo','numbertwo']

class MainFourRightForm(forms.ModelForm):
    class Meta:
        model = models.MainFourRight
        fields = ['img']
# Main Four End

# Footer Start

class FooterForm(forms.ModelForm):
    class Meta:
        model = models.Footer
        fields = ['name','adress']

# Footer End


# Login

User = get_user_model()

class CustomUserCreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Пароли не совпадают.")
            if len(password1) < 6:
                raise forms.ValidationError("Пароль должен быть длиной не менее 6 символов.")
            # Добавьте свои проверки, если нужно
            return password2
        