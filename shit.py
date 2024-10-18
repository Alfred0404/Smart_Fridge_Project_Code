from sympy.matrices import Matrix
from sympy import *
from numpy import sin, cos


def translation(x, y, z):
    T = [[ 1 , 0 , 0 , x ],
         [ 0 , 1 , 0 , y ],
         [ 0 , 0 , 1 , z ],
         [ 0 , 0 , 0 , 1 ]]
    
    return T


def x_rotation(angle):
    T = Matrix([[ 1 ,     0      ,      0      , 0 ],
                [ 0 , cos(angle) , -sin(angle) , 0 ],
                [ 0 , sin(angle) ,  cos(angle) , 0 ],
                [ 0 ,     0      ,      0      , 1 ]])
    
    return T


def z_rotation(angle):
    T = Matrix([[ cos(angle) , -sin(angle) , 0 , 0 ],
                [ sin(angle) ,  cos(angle) , 0 , 0 ],
                [     0      ,      0      , 0 , 1 ],
                [     0      ,      0      , 1 , 0 ],])
    
    return T


q1, q2, q3, q4 = symbols("q1 q2 q3 q4")
l1, l2, l3, l4 = symbols("l1 l2 l3 l4")


T1 = translation(0, 0, 11)*z_rotation(pi + q1)
