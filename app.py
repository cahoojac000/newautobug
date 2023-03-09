import gradio as gr
from bug import bug

driver = bug()

def login():
   driver.setup()
   return driver.run()

def autofillsubmit(text):
   tokens = str(text).split('\n')
   return driver.autofill(tokens)
   
with gr.Blocks() as interface:
  loginButton = gr.Button(value="Login")
  loginButton.click(login, inputs=None, outputs=None)

  text = gr.Textbox(label="Catalog Number\nCollector\nDate\nScientific Name\nDate Identified\nMale\nIndividual Count\nField Number")
  inputButton = gr.Button(value="Autofill")
  inputButton.click(autofillsubmit, inputs=text, outputs=None)
  
interface.launch()