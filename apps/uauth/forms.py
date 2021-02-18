from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class UserLoginForm(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(
        attrs={"class":"form-control",
        "placeholder":"Your user name"}),
        validators=[validators.MaxLengthValidator(10,"Siz 10ta dan oshiq xarif kiritdingiz")]
        )

	password = forms.CharField(label="",widget=forms.PasswordInput(
            attrs={"class":"form-control", 
            "placeholder":"Confirm password"}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise ValidationError('This user does not exist')
			if not user.check_password(password):
				raise ValidationError('Incorrect password')
			if not user.is_active:
				raise ValidationError('This user is not active')

		return super(UserLoginForm,self).clean(*args, **kwargs)



class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={"class":"form-control",
            "placeholder":"Your user name"}),validators=[validators.MaxLengthValidator(10,"Siz 10ta dan oshiq xarif kiritdingiz")])
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={"class":"form-control",
            "placeholder":"Your email"}))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={"class":"form-control",
            "placeholder":"password"}),validators=[validators.MinLengthValidator(6,"Sizning parolingiz yaroqsiz")])
    password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={"class":"form-control",
            "placeholder":"confirm password"}),validators=[validators.MinLengthValidator(6,"Sizning parolingiz yaroqsiz")])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords not match.")
        return data
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username



 	

 		

 		
 		

 		
 		















 	