from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput())
    confirmacao_senha = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            raise forms.ValidationError("As senhas não coincidem.")