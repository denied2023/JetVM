import jetvm



code = '''
import tkinter
def on_click(_):
    testing_label.config(text='Hello World!')
testing_button = Button(text='Click Me!', font=('Arial', 30, 'bold'), fg='blue', command=on_click)
testing_button.place(x=30, y=50)
testing_label = Label(text='Hello World!', font=('Arial', 30, 'italic'), fg='red')
testing_label.pack()'''
vm = jetvm.JetVM()
vm.compile('test', code)
