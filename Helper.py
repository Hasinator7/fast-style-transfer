from tkinter import *
from tkinter import filedialog
import os,sys
import subprocess
from shutil import copyfile

iterations_between_saving = "50"


cmd_eval = ["evaluate.py ", "--checkpoint ", "CHANGE THIS", "--in-path ","CHANGE THIS","--out-path " "out.jpg"]
cmd_train = ["style.py ", "--checkpoint-dir ", "CHANGE THIS", "--style ", "CHANGE THIS", "--checkpoint-iterations ", iterations_between_saving]


root = Tk()
modeOne=[]
modeTwo=[]
modeThree=[]
tkvar = StringVar(root)
stylepath=""

text_Name = Entry(root)
text_Name.grid(column=0, row=2)
modeOne.append(text_Name)

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
    modelName = text_Name.get()
    print(modelName)
    os.mkdir("models/"+modelName)
    copyfile(stylepath, "models/"+modelName+"/in.jpg")
    subprocess.Popen("python Helper.py",shell=True)
    sys.exit()
    
def findModels():
    models = ['Create new','Train model from checkpoint']
    for root, dirs, files in os.walk("models", topdown = False):
        for name in dirs:
             models.append(name)
    return models

    
def chooseStyle():
    global stylepath
    print("Choose Style")
    currdir = os.getcwd()
    filepath = filedialog.askopenfilename(parent = root, initialdir = currdir, filetypes=(("Image files", "*.jpg"), ("All files", "*")))
    if(len(filepath)>0):
        print("You chose " + filepath)
        stylepath = filepath
    
info = Label(root, text="Train last model, evaluate a finished model or create new model")
info.grid(column=0, row=0)

choices = findModels()
tkvar.set(choices[0])

combo = OptionMenu(root, tkvar, *choices)
combo.grid(column=0, row=1)

button_inputImage = Button(root, text="Choose style image", command = chooseStyle)
button_inputImage.grid(column=0, row=4)
modeOne.append(button_inputImage)

button_train = Button(root,text="Train model", command=train)
button_train.grid(column=1, row=2)
button_train.grid_remove()
modeTwo.append(button_train)

button_evaluate = Button(root, text="Evaluate model", command=evaluate)
button_evaluate.grid(column=1, row =1)
button_evaluate.grid_remove()
modeThree.append(button_evaluate)

button_newModel = Button(root, text="OK", command=createModel)
button_newModel.grid(column=1,row=1)
modeOne.append(button_newModel)


def changeMode(mode):
    print(mode)
    if(mode=="New Model"):
        for widget in modeTwo:
            widget.grid_remove()
        for widget in modeThree:
            widget.grid_remove()
        for widget in modeOne:
            widget.grid()
    else:
        for widget in modeOne:
            widget.grid_remove()
        for widget in modeTwo:
            widget.grid()
        for widget in modeThree:
            widget.grid()

def change_dropdown(*args):
    option = tkvar.get()
    print(option)
    if(option==choices[0]):
        changeMode("New Model")
    elif(option==choices[1]):
        changeMode("Train model")
    else:
        changeMode("Evaluate Model")
        
tkvar.trace('w', change_dropdown)



root.title("Training helper")
root.mainloop()
