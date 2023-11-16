"""
Forms for Helios
"""

from django import forms
from django.conf import settings

from .fields import SplitDateTimeField
from .models import Election
from .widgets import SplitSelectDateTimeWidget


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40, label="Nome abreviado", help_text='Sem espaços, será parte da URL da sua eleição, por ex. meu-clube-2023')
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':60}), label="Nome", help_text='Nome apresentável para a sua eleição, p.ex.: Eleição Chefe de Departamento 2023.')
  description = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}),label="Descrição", help_text='Máximo de 4000 caracteres.', required=False)
  election_type = forms.ChoiceField(label="Tipo", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False,label='Usar pseudônimo de eleitores', help_text='Se marcada, a identidade dos eleitores será substituída por pseudônimos, p.ex.: V12, no centro de rastreamento de cédulas.')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, label="Tornar ordem das questões aleatória", help_text='Habilite essa opção se você quiser que as questões apareçam em ordem aleatória para cada eleitor')
  private_p = forms.BooleanField(required=False, initial=False, label="Privada?", help_text='Uma eleição privada só é visível para eleitores registrados.')
  help_email = forms.CharField(required=False, initial="", label="Endereço de Email para Ajuda", help_text='Endereço de email que os eleitores devem usar para pedir ajuda.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="Link para download de informações da Eleição:", help_text=" Link de um documento PDF que contém informações extras, p. ex., biografias e declarações dos candidatos")
  
  # times
  voting_starts_at = SplitDateTimeField( label="Votação começa em", help_text = 'Data e horário de início da votação',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField( label="Votação termina em", help_text = 'Data e horário de término da votação',
                                   widget=SplitSelectDateTimeWidget, required=False)

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField( help_text = 'Informe a data e hora para extensão da votação', label = "Estender votação até: ",
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Enviar", initial="all", choices= [('all', 'todos os eleitores'), ('voted', 'eleitores que depositaram uma cédula'), ('not-voted', 'eleitores que ainda não depositaram uma cédula')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Enviar", choices= [('all', 'todos os eleitores'), ('voted', 'apenas eleitores que lançaram uma cédula'), ('none', 'nenhum - você tem certeza disso?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="ID do Eleitor")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

