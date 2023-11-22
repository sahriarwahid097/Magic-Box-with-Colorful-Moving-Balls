from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points = []
origins=[]
state=False
directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
speed = 0.01
recorded_speed=[]
space_bar_pressed=False

def draw_points(x, y, r, g, b):
    glEnable(GL_POINT_SMOOTH)
    glColor3f(r, g, b)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def mouseListener(button, state, x, y):
    global points
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        r = random.random()
        g = random.random()
        b = random.random()
        points.append([x, y, r, g, b])
        origins.append([x, y, r, g, b])
     


def specialKeyListener(key, x, y):
    global speed
    if key==GLUT_KEY_UP:
        speed *= 2
    elif key== GLUT_KEY_DOWN:
        speed /= 2
    


def keyboardListener(key, x, y):
    global space_bar_pressed
    global speed
    global recorded_speed
    
    if key==b' ' and not space_bar_pressed:
        recorded_speed.append(speed)
        space_bar_pressed=True
        speed=0
    elif key==b' ' and space_bar_pressed:
        space_bar_pressed=False
        speed=recorded_speed[-1]


    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    for point in points:
        draw_points(point[0], point[1], point[2], point[3], point[4])
    glutSwapBuffers()

def updatePoints():
    global points
    global speed
    global directions
    global origins

    for point in range(len(points)):
        if points[point][0]<0 or points[point][0]>500 or points[point][1]<0 or points[point][1]>500:
            points[point][0]=origins[point][0]
            points[point][1]=origins[point][1]
        move_x, move_y = random.choice(directions)
        points[point][0] += move_x * speed
        points[point][1] += move_y * speed
        
        
def animate():
    updatePoints()
    glutPostRedisplay()

glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Magic-Box-with-Colorful-Moving-Balls")
glutDisplayFunc(showScreen)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animate)
glutMainLoop()