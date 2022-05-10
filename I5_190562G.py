import numpy as np
import math as m
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(223)


# ax3=fig.add_subplot(222)


# This function created as to solve any linear equation
def Solve(row1, row2, cof):
    L = np.array([row1, row2])
    X = np.array(cof)
    [x, y] = np.linalg.solve(L, X)
    return (x, y)


# Final angle function
def SClin(a, b, c1, c2):
    Z = m.acos((m.pow(c1, 2) + m.pow(c2, 2) - m.pow(a, 2) - m.pow(b, 2)) / (2 * a * b))
    for Y in [-Z, Z, 2 * m.pi - Z]:
        row1 = [a * m.cos(Y) + b, -a * m.sin(Y)]
        row2 = [a * m.sin(Y), a * m.cos(Y) + b]
        cof = [c1, c2]
        sol1, sol2 = Solve(row1, row2, cof)
        Co, Si = sol1, sol2
        if Si < 0:
            beta = m.pi * 2 - m.acos(Co)
        else:
            beta = m.acos(Co)
        alpha = Y + beta
        if 0 <= beta <= m.pi and 0 <= alpha <= 2 * m.pi:
            albe = [alpha, beta]
            return albe


# given Parameters
[AB, BC, CD, AD] = [15, 35, 30, 25]
ob = 0.18849

A = 0
X = []
Y = []


def animate(i):
    global A, X, Y
    if A < 2 * m.pi:
        A = A + m.pi / 20
    else:
        A = m.pi / 20
    # Analysing mechanism
    [B, D] = SClin(-BC, CD, AB * m.cos(A) - AD, AB * m.sin(A))

    # plotting Mechanism
    x_A = 0
    x_B = AB * m.cos(A)
    x_C = AD + CD * m.cos(D)
    x_D = AD

    y_A = 0
    y_B = AB * m.sin(A)
    y_C = CD * m.sin(D)
    y_D = 0

    # plotting

    ax1.cla()
    x_M = [x_A, x_B, x_C, x_D, x_A]  # plotting AB,BC,CD,AD
    y_M = [y_A, y_B, y_C, y_D, y_A]

    ax1.annotate('A', (x_A, y_A))
    ax1.annotate('B', (x_B, y_B))
    ax1.annotate('C', (x_C, y_C))
    ax1.annotate('D', (x_D, y_D))

    ax1.plot(x_M, y_M, color='#c71032')
    ax1.axis('equal')
    ax1.set_title('Position of Linkages')
    ax1.set_ylim([-40, 50])
    ax1.set_xlim([-20, 50])

    Dv = D
    Bv = B
    if (A - D > m.pi / 2 and B < A - m.pi) or (B > A and D > A):
        Dv = m.pi + D
    if D < A < m.pi + D:
        Bv = m.pi + B

    bc, oc = Solve([m.cos(Bv), m.cos(Dv)], [m.sin(Bv), m.sin(Dv)], [ob * m.cos(A), ob * m.sin(A)])
    print(bc, oc)
    print(m.degrees(A), int(m.degrees(Bv)), int(m.degrees(Dv)))

    # velocity plotting

    x_o = 0
    x_b = -ob * m.sin(A)
    x_c = -oc * m.sin(D)

    y_o = 0
    y_b = ob * m.cos(A)
    y_c = oc * m.sin(A)

    ax2.cla()
    x_V = [x_o, x_b, x_c, x_o]  # plotting ob,bc,cd
    y_V = [y_o, y_b, y_c, y_o]

    ax2.annotate('o', (x_o, y_o))
    ax2.annotate('b', (x_b, y_b))
    ax2.annotate('c', (x_c, y_c))

    ax2.plot(x_V, y_V, color='#1d1f1e')
    ax2.set_ylim([-0.5, 0.5])
    ax2.set_xlim([-0.5, 0.6])
    ax2.set_title('Velocities  At Instant')
    ax2.axis('equal')

    # plotting realtime data of Velocity of point D
    if A < (m.pi * 2 - 0.001):
        if y_c < 0:
            oc = -oc
        if float(m.degrees(A)) not in X:
            X += [float(m.degrees(A))]
            Y += [oc]
    ax3.cla()
    ax3.plot(X, Y)
    ax3.set_title('Velocity of point C')


ax = plt.gca()
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
