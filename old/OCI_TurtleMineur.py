#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle


# In[2]:


discworld = turtle.Screen()
ATuin = turtle.Turtle()
ATuin.speed(0)


# In[3]:


def drawSquare(size):
    for i in range(4):
        ATuin.forward(size)
        ATuin.right(90)


# In[4]:


def drawGrid(nbligne, nbcol, size = 25, space = 5):
    ATuin.speed(0)
    for l in range(nbligne):
        for c in range(nbcol):
            drawSquare(size)
            ATuin.up()
            ATuin.forward(size+space)
            ATuin.down()
        ATuin.up()
        ATuin.backward(nbcol * (size + space))
        ATuin.right(90)
        ATuin.forward(size+space)
        ATuin.down()
        ATuin.left(90)






