import jetvm



code = '''
import tkinter
testing_button = Button(text='Hello, World!')
testing_button.place(x=30, y=50) 
testing_label = Label(text='Hello World!', font=('Arial', 30, 'bold'))
testing_label.pack()'''
vm = jetvm.JetVM()
vm.compile('test', code)
