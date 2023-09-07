from django import forms

class ContactForm(forms.Form):#widgets
    name=forms.CharField(label="Name",required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Write your name'}
    ),min_length=3, max_length=100)
    email=forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Write your email'}
    ))
    subject=forms.CharField(label="Asunto",required=True,widget=forms.TextInput(
        attrs={'class':'form-control ','placeholder':'Write the subject of the message'}
    )) 
    message=forms.CharField(label="Message",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':4,'placeholder':'Write the message'}
    ),min_length=10,max_length=1000)
                         