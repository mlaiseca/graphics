import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1,1,1),
    (1,1,-1),
    (1,-1,1),
    (1,-1,-1),
    (-1,1,1),
    (-1,1,-1),
    (-1,-1,1),
    (-1,-1,-1),
    )

edges = (
    (0,1),
    (0,2),
    (0,4),
    (5,4),
    (5,1),
    (5,7),
    (6,7),
    (6,4),
    (6,2),
    (3,7),
    (3,1),
    (3,2),
    )

surfaces = (
    (0,1,5,4),
    (0,1,3,2),
    (2,3,7,6),
    (4,5,7,6),
    (1,3,7,5),
    (0,2,6,4)
    )

colors = (
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1)
    )


def Cube():
    glBegin(GL_QUADS)
    #set as one constant color per surface, if we set x in inner for loops we get a gradient
    x = 0 
    for surface in surfaces:
        x+=1 
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])

    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    glRotatef(0,0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
        

    
    
