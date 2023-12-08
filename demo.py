import jetvm



code = '''
import tkinter
def on_click(_):
    print('Hello World!')
    testing_label.config(text='Ouch! You clicked me!')
testing_button = Button(text='Click Me!', font=('Arial', 30, 'bold'), fg='blue', command=on_click)
testing_button.place(x=30, y=50)
testing_label = Label(text='Hello World!', font=('Arial', 30, 'italic'), fg='red')
testing_label.pack()'''
vm = jetvm.JetVM()
vm.compile('test', code)
