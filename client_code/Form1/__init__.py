from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    # Set 'name' to the text in 'name_box'
    name = self.name_box.text
    # Set 'email' to the text in 'email_box'
    email = self.email_box.text
    # Set 'feedback' to the text in 'feedback_box'
    feedback = self.feedback_box.text
    # Set 'recommend' to the selection in 'recommend_box'
    recommend = self.recommend_box.selected_value
    # take user input to server-side
    anvil.server.call('send_feedback', name, email, feedback, recommend)
    # show a pop-up that says "feedback submitted"
    Notification("Feedback submitted!").show()
    # call our 'clear_inputs' method to clear the boxes after submission
    self.clear_inputs()

  # new method to clear each form after each submission
  def clear_inputs(self):
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
    self.recommend_box.selected_value = None