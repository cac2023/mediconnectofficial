from ._anvil_designer import PatientSignUpTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class PatientSignUp(PatientSignUpTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def confirm_click(self, **event_args):
    AppState.Pusername=self.username_sign.text
    AppState.Ppassword=self.password_sign.text
    AppState.PCode = self.text_box_1.text
    AppState.PName=self.namebox.text
    anvil.server.call('add_patient', AppState.Pusername, AppState.Ppassword, AppState.PCode, AppState.PName)

    open_form('PatientLogin')
    pass

  def psback_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('PatientLogin')
    pass







