from tkinter import *
import os
import subprocess

iterations_between_saving = "50"


cmd_eval = ["evaluate.py ", "--checkpoint ", "CHANGE THIS", "--in-path ","CHANGE THIS","--out-path " "out.jpg"]
cmd_train = ["style.py ", "--checkpoint-dir ", "CHANGE THIS", "--style ", "CHANGE THIS", "--checkpoint-iterations ", iterations_between_saving]


root = Tk()
tkvar = StringVar(root)

def train():
    print("Training")
    path= os.path.join("models", tkvar.get()).replace("\\","/")
    cmd_train[2] = path + " "
    cmd_train[4] = os.path.join(path,"in.jpg ").replace("\\","/")
    command = "".join(cmd_train)
    print(command)
    subprocess.Popen(command, shell=True)
    
def evaluate():
    print("Evaluate")
    path= os.path.join("models", tkvar.get()).replace("\\","/")
    cmd_eval[2] = path + " "
    cmd_eval[4] = "in.jpg "
    command = "".join(cmd_eval)
    print(command)
    subprocess.Popen(command, shell=True)
    
def createModel():
    print("Create Model")
    
def findModels():
    models = ['Create new','Train model from checkpoint']
    for root, dirs, files in os.walk("models", topdown = False):
        for name in dirs:
             models.append(name)
    return models

info = Label(root, text="Train last model, evaluate a finished model or create new model")
info.grid(column=0, row=0)

choices = findModels()
tkvar.set(choices[0])

combo = OptionMenu(root, tkvar, *choices)
combo.grid(column=0, row=1)

button_train = Button(root,text="Train model", command=train)
button_train.grid(column=1, row=2)
button_train.grid_remove()

button_evaluate = Button(root, text="Evaluate model", command=evaluate)
button_evaluate.grid(column=1, row =1)
button_evaluate.grid_remove()

button_newModel = Button(root, text="OK", command=createModel)
button_newModel.grid(column=1,row=1)


def changeMode(mode):
    print(mode)

def change_dropdown(*args):
    option = tkvar.get()
    print(option)
    if(option==choices[0]):
        button_newModel.grid()
        button_train.grid_remove()
        button_evaluate.grid_remove()
    elif(option==choices[1]):
        button_evaluate.grid_remove()
        button_newModel.grid_remove()
        button_train.grid()
        
    else:
        button_train.grid()
        button_newModel.grid_remove()
        button_evaluate.grid()
        
tkvar.trace('w', change_dropdown)



root.title("Training helper")
root.mainloop()
