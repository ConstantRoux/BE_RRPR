import numpy as np
import math


class MGI:

    def __init__(self, L, H):
        self.H = H
        self.L = L
        self.q1, self.q2, self.q3, self.q4 = (0, 0, 0, 0)
        self.q1_bis, self.q2_bis, self.q3, self.q4_bis = (0, 0, 0, 0)

    def getQi(self):
        return (self.q1, self.q2, self.q3, self.q4)

    def getQi_bis(self):
        return (self.q1_bis, self.q2_bis, self.q3, self.q4_bis)

    def getQi(self, X, Y, Z, theta):
        w1 = Y - self.L[4] * np.sin(theta)
        w2 = -self.L[0] + X - self.L[4] * np.cos(theta)
        z = self.L[2] + self.L[3]
        c2 = round((w1 * w1 + w2 * w2 - self.L[1] * self.L[1] - z * z) / (2 * z * self.L[1]), 2)
        self.q2 = (math.atan2(np.sqrt(1 - c2 * c2), c2)) % (2 * np.pi)
        self.q2_bis = (math.atan2(-np.sqrt(1 - c2 * c2), c2)) % (2 * np.pi)
        x1 = Y - self.L[4] * np.sin(theta)
        x2 = self.L[0] - X + self.L[4] * np.cos(theta)
        y1 = -x2
        y2 = x1
        z1 = self.L[1] * np.cos(self.q2) + self.L[2] + self.L[3]
        z1_bis = self.L[1] * np.cos(self.q2_bis) + self.L[2] + self.L[3]
        z2 = -self.L[1] * np.sin(self.q2)
        z2_bis = -self.L[1] * np.sin(self.q2_bis)
        self.q1 = (math.atan2((z1*y2-z2*y1)/(x1*y2-x2*y1),(z2*x1-z1*x2)/(x1*y2-x2*y1)) - self.q2) % (2 * np.pi)
        self.q1_bis = (math.atan2((z1_bis*y2-z2_bis*y1)/(x1*y2-x2*y1),(z2_bis*x1-z1_bis*x2)/(x1*y2-x2*y1)) - self.q2_bis) % (2 * np.pi)
        self.q4 = (theta - self.q1 - self.q2) % (2 * np.pi)
        self.q4_bis = (theta - self.q1_bis - self.q2_bis) % (2 * np.pi)
        self.q3 = Z - self.H[0] - self.H[1]

        print(c2)

        return ((self.q1, self.q2, self.q3, self.q4),
                (self.q1_bis, self.q2_bis, self.q3, self.q4_bis))
