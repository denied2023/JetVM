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
            alert("It is recommended to use live server or HTTP(s) to run this program! Project might crash. Press OK to continue.");
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
            if self.text:
                self.element.textContent = self.text
            

            
        

        def config(self, text=None, font=None, fg=None, bg=None, background=None, foreground=None):
            if text is not None:
                self.text = text
                self.element.innerHTML = self.text
            if font is not None:
                self.font = font
                self.element.style.fontFamily = self.font[0]
                self.element.style.fontSize = str(self.font[1]) + 'px'
                if self.font[2] == 'bold':
                    self.element.style.fontWeight = 'bold'
                elif self.font[2] == 'italic':
                    self.element.style.fontStyle = 'italic'
                else:
                    self.element.style.fontWeight = 'normal'
                    self.element.style.fontStyle = 'normal'
            if fg is not None or foreground is not None:
                self.fg = fg if fg is not None else foreground
                self.element.style.color = self.fg
            if bg is not None or background is not None:
                self.bg = bg if bg is not None else background
                self.element.style.backgroundColor = self.bg
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
            document <= self.button
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
    class turtle:
        class Turtle:
            def __init__(self):
                self.element = document.createElement('canvas')
                self.element.style.border = '1px solid black'
                self.element.style.position = 'absolute'
                self.element.style.left = '0px'
                self.element.style.top = '0px'
                self.element.width = 500
                self.element.height = 500
                document <= self.element
                self.ctx = self.element.getContext('2d')
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, 250)
                self.ctx.lineTo(500, 250)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(250, 0)
                self.ctx.lineTo(250, 500)
                self.ctx.stroke()
                self.x = 250
                self.y = 250
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
                self.element.style.border = '1px solid black'
                self.element.style.position = 'absolute'
                self.element.style.left = '0px'
                self.element.style.top = '0px'
                self.element.width = 500
                self.element.height = 500
                document <= self.element
                self.ctx = self.element.getContext('2d')
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, 250)
                self.ctx.lineTo(500, 250)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(250, 0)
                self.ctx.lineTo(250, 500)
                self.ctx.stroke()
                self.x = 250
                self.y = 250
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
            def forward(self, distance):
                self.ctx.strokeStyle = self.color
                self.ctx.lineWidth = self.width
                self.ctx.beginPath()
                self.ctx.moveTo(self.x, self.y)
                self.x += distance * math.cos(self.angle)
                self.y += distance * math.sin(self.angle)
                self.ctx.lineTo(self.x, self.y)
                self.ctx.stroke()
            def backward(self, distance):
                self.ctx.strokeStyle = self.color
                self.ctx.lineWidth = self.width
                self.ctx.beginPath()
                self.ctx.moveTo(self.x, self.y)
                self.x -= distance * math.cos(self.angle)
                self.y -= distance * math.sin(self.angle)
                self.ctx.lineTo(self.x, self.y)
                self.ctx.stroke()
            def right(self, angle):
                self.angle -= math.radians(angle)
            def left(self, angle):
                self.angle += math.radians(angle)
            def penup(self):
                self.pen = False
            def pendown(self):
                self.pen = True
            def speed(self, speed):
                self.speed = speed
            def goto(self, x, y):
                self.x = x
                self.y = y
            def setx(self, x):
                self.x = x
            def sety(self, y):
                self.y = y
            def setheading(self, angle):
                self.angle = math.radians(angle)
            def home(self):
                self.x = 250
                self.y = 250
                self.angle = 0
            def clear(self):
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, 250)
                self.ctx.lineTo(500, 250)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(250, 0)
                self.ctx.lineTo(250, 500)
                self.ctx.stroke()
            def reset(self):
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, 250)
                self.ctx.lineTo(500, 250)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(250, 0)
                self.ctx.lineTo(250, 500)
                self.ctx.stroke()
                self.x = 250
                self.y = 250
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
            def circle(self, radius, extent=None, steps=None):
                if extent is None:
                    extent = 360
                if steps is None:
                    steps = 360
                self.ctx.strokeStyle = self.color
                self.ctx.lineWidth = self.width
                self.ctx.beginPath()
                self.ctx.moveTo(self.x, self.y)
                for i in range(steps):
                    if i > extent:
                        break
                    self.x += radius * math.cos(self.angle)
                    self.y += radius * math.sin(self.angle)
                    self.ctx.lineTo(self.x, self.y)
                    self.ctx.stroke()
            def dot(self, size=None, color=None):
                if size is None:
                    size = self.width
                if color is None:
                    color = self.color
                self.ctx.fillStyle = color
                self.ctx.beginPath()
                self.ctx.arc(self.x, self.y, size, 0, 2 * math.pi)
                self.ctx.fill()
            def stamp(self):
                self.ctx.strokeStyle = self.color
                self.ctx.lineWidth = self.width
                self.ctx.beginPath()
                self.ctx.moveTo(self.x, self.y)
                self.ctx.lineTo(self.x, self.y)
                self.ctx.stroke()
            def write(self, text, font=None, align=None, move=None):
                if font is None:
                    font = ('Arial', 12, 'normal')
                if align is None:
                    align = 'left'
                if move is None:
                    move = True
                self.ctx.font = str(font[1]) + 'px ' + font[0]
                self.ctx.textAlign = align
                self.ctx.fillText(text, self.x, self.y)
                if move:
                    self.x += self.ctx.measureText(text).width
            def begin_fill(self):
                self.ctx.fillStyle = self.color
                self.ctx.beginPath()
                self.ctx.moveTo(self.x, self.y)
            def end_fill(self):
                self.ctx.fill()
            def color(self, color):
                self.color = color
            def width(self, width):
                self.width = width
            def hideturtle(self):
                self.element.style.display = 'none'
            def showturtle(self):
                self.element.style.display = 'block'
            def isvisible(self):
                return self.element.style.display == 'block'
            def isdown(self):
                return self.pen
            def distance(self, x, y):
                return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            def heading(self):
                return math.degrees(self.angle)
            def xcor(self):
                return self.x
            def ycor(self):
                return self.y
            def get_poly(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_poly(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def get_screen_poly(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_screen_poly(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def get_shapepoly(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_shapepoly(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def get_shapepoly(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_shapepoly(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def get_shape(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_shape(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def get_shapepoly(self):
                return self.ctx.getImageData(0, 0, self.element.width, self.element.height)
            def set_shapepoly(self, poly):
                self.ctx.putImageData(poly, 0, 0)
            def pencolor(self, color):
                self.color = color
            def fillcolor(self, color):
                self.color = color
            def bgcolor(self, color):
                self.ctx.fillStyle = color
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
            def getcanvas(self):
                return self.element
            def getpen(self):
                return self.pen
            def getscreen(self):
                return self.element
            def getturtle(self):
                return self.element
        class Screen:
            def __init__(self):
                self.element = document.createElement('canvas')
                self.element.style.border = '1px solid black'
                self.element.style.position = 'absolute'
                self.element.style.left = '0px'
                self.element.style.top = '0px'
                self.element.width = 500
                self.element.height = 500
                document <= self.element
                self.ctx = self.element.getContext('2d')
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, 250)
                self.ctx.lineTo(500, 250)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(250, 0)
                self.ctx.lineTo(250, 500)
                self.ctx.stroke()
                self.x = 250
                self.y = 250
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
            def setup(self, width, height, startx=None, starty=None):
                self.element.width = width
                self.element.height = height
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, self.element.height / 2)
                self.ctx.lineTo(self.element.width, self.element.height / 2)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(self.element.width / 2, 0)
                self.ctx.lineTo(self.element.width / 2, self.element.height)
                self.ctx.stroke()
                self.x = self.element.width / 2
                self.y = self.element.height / 2
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
                if startx is not None:
                    self.x = startx
                if starty is not None:
                    self.y = starty
            def title(self, title):
                document.title = title
            def bgcolor(self, color):
                self.ctx.fillStyle = color
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
            def clear(self):
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, self.element.height / 2)
                self.ctx.lineTo(self.element.width, self.element.height / 2)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(self.element.width / 2, 0)
                self.ctx.lineTo(self.element.width / 2, self.element.height)
                self.ctx.stroke()
                self.x = self.element.width / 2
                self.y = self.element.height / 2
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
            def reset(self):
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, self.element.height / 2)
                self.ctx.lineTo(self.element.width, self.element.height / 2)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(self.element.width / 2, 0)
                self.ctx.lineTo(self.element.width / 2, self.element.height)
                self.ctx.stroke()
                self.x = self.element.width / 2
                self.y = self.element.height / 2
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
            def bye(self):
                self.element.remove()
            def exitonclick(self):
                self.element.bind('click', lambda _: self.element.remove())
            def onclick(self, fun, btn=1, add=None):
                self.element.bind('click', fun)
            def onkey(self, fun, key):
                self.element.bind('keydown', fun)
            def onkeypress(self, fun, key): 
                self.element.bind('keydown', fun)
            def onkeyrelease(self, fun, key):
                self.element.bind('keyup', fun)
            def listen(self):
                pass
            def ontimer(self, fun, t=0):
                timer.set_timeout(fun, t)
            def ontimer(self, fun, t=0):
                timer.set_timeout(fun, t)
            def tracer(self, n=None, delay=None):
                pass
            def update(self):
                pass
            def window_height(self):
                return self.element.height
            def window_width(self):
                return self.element.width
            def window_x(self):
                return self.element.offsetLeft
            def window_y(self):
                return self.element.offsetTop
            def screensize(self, width, height, startx=None, starty=None):
                self.element.width = width
                self.element.height = height
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, self.element.height / 2)
                self.ctx.lineTo(self.element.width, self.element.height / 2)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(self.element.width / 2, 0)
                self.ctx.lineTo(self.element.width / 2, self.element.height)
                self.ctx.stroke()
                self.x = self.element.width / 2
                self.y = self.element.height / 2
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1
                if startx is not None:
                    self.x = startx
                if starty is not None:
                    self.y = starty
            def setworldcoordinates(self, llx, lly, urx, ury):
                self.element.width = urx - llx
                self.element.height = ury - lly
                self.ctx.fillStyle = 'white'
                self.ctx.fillRect(0, 0, self.element.width, self.element.height)
                self.ctx.strokeStyle = 'black'
                self.ctx.lineWidth = 1
                self.ctx.beginPath()
                self.ctx.moveTo(0, self.element.height / 2)
                self.ctx.lineTo(self.element.width, self.element.height / 2)
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.moveTo(self.element.width / 2, 0)
                self.ctx.lineTo(self.element.width / 2, self.element.height)
                self.ctx.stroke()
                self.x = self.element.width / 2
                self.y = self.element.height / 2
                self.angle = 0
                self.pen = True
                self.color = 'black'
                self.width = 1
                self.speed = 1

            
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
        print('Super Compiling is under development! Come back later!')

        #finish super compling here!
        compiled = self._compile(name, code)

        global alt_python_code
        name = compiled[0]
        alt_python_code = compiled[1]

        global html
        html = f'''
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
    from random import randint


    assets = {assets}

    def open_file(file_name):
        return assets[file_name]

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
            if self.text:
                self.element.textContent = self.text
            

            
        

        def config(self, text=None, font=None, fg=None, bg=None, background=None, foreground=None):
            if text is not None:
                self.text = text
                self.element.innerHTML = self.text
            if font is not None:
                self.font = font
                self.element.style.fontFamily = self.font[0]
                self.element.style.fontSize = str(self.font[1]) + 'px'
                if self.font[2] == 'bold':
                    self.element.style.fontWeight = 'bold'
                elif self.font[2] == 'italic':
                    self.element.style.fontStyle = 'italic'
                else:
                    self.element.style.fontWeight = 'normal'
                    self.element.style.fontStyle = 'normal'
            if fg is not None or foreground is not None:
                self.fg = fg if fg is not None else foreground
                self.element.style.color = self.fg
            if bg is not None or background is not None:
                self.bg = bg if bg is not None else background
                self.element.style.backgroundColor = self.bg
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
            document <= self.button
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
    {alt_python_code}
    </script>

</body>
    '''

        save_folder = 'JetVM-SUPER_COMPILED-'+name
        if os.path.exists(save_folder):
            print(f'JetVM: Super Compiling stopped! Please delete the folder "{save_folder}"')
            quit()
        os.mkdir(save_folder)
        open(f'{save_folder}/index.html', 'w').write(html)

        for asset in assets:
            open(f'{save_folder}/{asset}', 'w').write(assets[asset])

        print(f'Done compiling! Saved in "{save_folder}"')

        


        