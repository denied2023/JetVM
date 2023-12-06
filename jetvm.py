import os
import re


# JetVM by BtPlayzX



class JetVM:
    def __init__(self):
        self.tab = '    '
    def _compile(self, name, code):
        print('Compiling "{}" into JetVM...'.format(name))
        self.alt_python_code = ''

        self.window_geometry_width = 100
        self.window_geometry_height = 100

        code = str(code)
        def append_alt_code(alt_code):
            self.alt_python_code = self.alt_python_code + '\n' + self.tab + alt_code
        for line in code.splitlines():
            if line.startswith('#'):
                pass
            elif 'import tkinter' in line:
                pass
            elif 'from tkinter' in line:
                pass
            elif 'import turtle' in line:
                pass
            elif 'from turtle' in line:
                pass
            elif 'Tk()' in line:
                letters = ''
                for letter in line:
                    if letter == '=':
                        letters += letter
                        break
                    else:
                        letters += letter
                append_alt_code(letters + ' None')
            elif '.mainloop()' in line:
                pass
            elif '.title' in line:
                pass
            elif '.geometry' in line:
                pass
            elif '.iconphoto' in line:
                pass
            elif '.iconbitmap' in line:
                pass
            elif '.resizable' in line:
                pass
            elif 'turtle.' in line:
                append_alt_code(line.replace('turtle.', ''))
            elif 'import threading' in line:
                pass
            elif 'from threading' in line:
                pass
            elif 'from PIL' in line:
                pass
            elif 'import PIL' in line:
                pass
            elif 'tkinter.' in line: line.replace('tkinter.', '')
            elif 'tk.' in line: line.replace('tk.', '')
            elif 'Label' in line:
                label_index = line.find('Label')
                equal_index = line.find('=')
                append_alt_code(line[:equal_index+1] + ' ' + line[label_index:])
            elif 'Button' in line:
                button_index = line.find('Button')
                equal_index = line.find('=')
                append_alt_code(line[:equal_index+1] + ' ' + line[button_index:])
            elif 'class Label' in line:
                print(f'JetVM: Compiling stopped! Please change this line of code: {line}')
                quit()
            elif 'class Button' in line:
                print(f'JetVM: Compiling stopped! Please change this line of code: {line}')
                quit()
            elif 'def Label' in line:
                print(f'JetVM: Compiling stopped! Please change this line of code: {line}')
                quit()
            elif 'def Button' in line:
                print(f'JetVM: Compiling stopped! Please change this line of code: {line}')
                quit()

            else:
                append_alt_code(line)
            
            label_var = ''

            for char in line:
                if char == '=':
                    break
                else:
                    label_var = label_var + char
            label_var = label_var.replace(' ', '')

            if 'open(' in line:
                line.replace('open(', 'open_file(')
                line.replace("',", "'")
                line.replace('r', '')
                line.replace('r+', '')




        
            




        # Save the code

        self.html = f'''
<DOCTYPE html>
<head>
    <title>Klockcraft</title>
    <meta charset="utf-8">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.12.0/brython.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.12.0/brython_stdlib.js"></script>
    <script type = text/javascript>
        if(document.location.href.startsWith("file:")) {{
            alert("Do not run this Klockcraft game locally, please run on live server or HTTP(s).");
        }}
    </script>

</head>

<body>

    <script type="text/python">
    from browser import *
    from random import randint

    def open_file(file_name):
        if file_name.status == 200 or file_name.status == 0:
            print(file_name.text)
        else:
            alert("Failed to load file "+file_name.text)
        website_url = window.location.href
        if website_url.endswith('/'):
            pass
        else:
            website_url += '/'
        req = ajax.ajax()
        req.bind('complete', open_file)
        req.open('GET', website_url+file_name, True)
        req.send()

    class Label:
        def __init__(self, _=None, text='', font=None, fg=None, bg=None, background=None, foreground=None, image=None):
            self.text = text
            self.font = font
            self.fg = fg
            self.bg = bg
            self.image = image
            self.background = background
            self.foreground = foreground
            self.element = document.createElement('label')
            self.element.textContent = self.text
            self.element.style.userSelect = 'none'
            if self.font:
                self.element.style.fontFamily = self.font[0]
                self.element.style.fontSize = self.font[1]
                if self.font[2] == 'bold':
                    self.element.style.fontWeight = 'bold'
                elif self.font[2] == 'italic':
                    self.element.style.fontStyle = 'italic'
                else:
                    self.element.style.fontWeight = 'normal'
                    self.element.style.fontStyle = 'normal'
            if self.fg:
                self.element.style.color = self.fg
            if self.bg:
                self.element.style.backgroundColor = self.bg
            if self.background:
                self.element.style.backgroundColor = self.background
            if self.foreground:
                self.element.style.color = self.foreground
            if self.image:
                self.element = document.createElement('img')
                self.element.src = self.image
            

            
        

        def config(self, text=None, font=None, fg=None, bg=None, background=None, foreground=None):
            if text is not None:
                self.text = text
                self.element.textContent = self.text
            if font is not None:
                self.font = font
                self.element.style.fontFamily = self.font[0]
                self.element.style.fontSize = self.font[1]
                if self.font[2] == 'bold':
                    self.element.style.fontWeight = 'bold'
                elif self.font[2] == 'italic':
                    self.element.style.fontStyle = 'italic'
                else:
                    self.element.style.fontWeight = 'normal'
                    self.element.style.fontStyle = 'normal'
            if fg is not None:
                self.fg = fg
                self.element.style.color = self.fg
            if bg is not None:
                self.bg = bg
                self.element.style.backgroundColor = self.bg
            if background is not None:
                self.background = background
                self.element.style.backgroundColor = self.background
            if foreground is not None:
                self.foreground = foreground
                self.element.style.color = self.foreground
            if self.image:
                self.element = document.createElement('img')
                self.element.src = self.image
            
            
            
        def place(self, x, y):
            self.element.style.left = str(x)+'px'
            self.element.style.top = str(y)+'px'
            document <= self.element

        
        def destroy(self):
            self.element.remove()
        
        def place_forget(self):
            self.element.style.position = 'static'
            self.element.style.left = '0px'
            self.element.style.top = '0px'

        def pack(self):
            self.element.style.left = str(0)+'px'
            self.element.style.top = str(0)+'px'
            document <= self.element
        
        def place_forget(self):
            self.element.style.position = 'static'
            self.element.style.left = '0px'
            self.element.style.top = '0px'
        
    class Button:
        def __init__(self, _=None, text='', command=None, font=None, fg=None, bg=None, background=None, foreground=None, image=None):
            self.text = ''
            self.button = html.BUTTON(text)
            self.button.textContent = text
            self.button.style.borderRadius = '0'
            self.button.style.borderColor = 'white'
            self.image = image
            if command is not None:
                self.button.bind('click', command)
            if font is not None:
                self.button.style.fontFamily = font[0]
                self.button.style.fontSize = font[1]
                if font[2] == 'bold':
                    self.button.style.fontWeight = 'bold'
                elif font[2] == 'italic':
                    self.button.style.fontStyle = 'italic'
                else:
                    self.button.style.fontWeight = 'normal'
                    self.button.style.fontStyle = 'normal'
            if fg is not None:
                self.button.style.color = fg
            if bg is not None:
                self.button.style.backgroundColor = bg
            if background is not None:
                self.button.style.backgroundColor = background
            if foreground is not None:
                self.button.style.color = foreground
            if self.image:
                self.element = document.createElement('img')
                self.element.src = self.image
            

        def config(self, text='', command=None, font=None, fg=None, bg=None, background=None, foreground=None, image=None):
            self.button.text = text
            self.button.textContent = text
            if command is not None:
                self.button.bind('click', command)
            if font is not None:
                self.button.style.fontFamily = font[0]
                self.button.style.fontSize = font[1]
                if font[2] == 'bold':
                    self.button.style.fontWeight = 'bold'
                elif font[2] == 'italic':
                    self.button.style.fontStyle = 'italic'
                else:
                    self.button.style.fontWeight = 'normal'
                    self.button.style.fontStyle = 'normal'
            if fg is not None:
                self.button.style.color = fg
            if bg is not None:
                self.button.style.backgroundColor = bg
            if background is not None:
                self.button.style.backgroundColor = background
            if foreground is not None:
                self.button.style.color = foreground
            if image is not None:
                self.element = document.createElement('img')
                self.element.src = self.image
        def place(self, x, y):
            self.button.style.position = 'absolute'
            self.button.style.left = str(x)+'px'
            self.button.style.top = str(y)+'px'
            document <= self.button


        def destroy(self):
            self.button.remove()

        def place_forget(self):
            self.button.style.position = 'static'
            self.button.style.left = '0px'
            self.button.style.top = '0px'
            
        def pack(self):
            self.element.style.left = str(0)+'px'
            self.element.style.top = str(0)+'px'
            document <= self.button
    class threading:
        class Thread:
            daemon = False
            def __init__(self, target):
                self.target = target
            def start(self):
                timer.set_interval(self.target, 1)
            
    def PhotoImage(file): return file
    {self.alt_python_code}
    </script>

</body>
    '''

        return [name, self.alt_python_code, self.html]
    
    def compile(self, name, code):
        compiled = self._compile(name, code)

        name = compiled[0]
        html = compiled[2]

        save_folder = 'JetVM-COMPILED-'+name
        if os.path.exists(save_folder):
            print(f'JetVM: Compiling stopped! Please delete the folder "{save_folder}"')
            quit()
        os.mkdir(save_folder)
        with open(f'{save_folder}/index.html', 'w+') as writer:
            for w in self.html:
                writer.write(w)

        print(f'Done compiling! Saved in "{save_folder}"')
    
    def super_compile(self, name, code, assets):
        #finish super coming here!
        compiled = self._compile(name, code)

        global alt_python_code
        name = compiled[0]
        alt_python_code = compiled[1]

        global html
        self.html = '''
<DOCTYPE html>
<DOCTYPE html>
<head>
    <title>Klockcraft</title>
    <meta charset="utf-8">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.12.0/brython.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.12.0/brython_stdlib.js"></script>
</head>

<body>

    <script type="text/python">
    from browser import *
    class Label:
        def __init__(self, _=None, text=''):
            self.text = ''
        def config(self, text):
            pass
    class Button:
        def __init__(self, _=None, text=''):
            self.text = ''
        def config(self, text):
            pass
    class threading:
        class Thread:
            daemon = False
            def __init__(self, target):
                self.target = target
            def start(self):
                timer.set_interval(self.target, 0)
            
            def start(self):
                pass
    {alt_python_code}
    </script>

</body>'''

        save_folder = 'JetVM-SUPER_COMPILED-'+name
        if os.path.exists(save_folder):
            print(f'JetVM: Super Compiling stopped! Please delete the folder "{save_folder}"')
            quit()
        os.mkdir(save_folder)
        open(f'{save_folder}/index.html', 'w').write(html)

        for asset in assets:
            open(f'{save_folder}/{asset}', 'w').write(assets[asset])

        print(f'Done compiling! Saved in "{save_folder}"')

        


        