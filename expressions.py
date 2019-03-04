#!/usr/bin/env python
# coding: utf-8

import re as re
import sys

context = {}

class Node:

    def __init__(self):
        pass

    def evaluate(self):
        return ''

    def beta_red(self):
        pass

class Program:

    def __init__(self, program):
        self.program = program

    def evaluate(self):
        if (self.program != None):
            return self.program.evaluate()

class NodeBeta(Node):

    def __init__(self, left, right, xi):
        self.left = left
        self.right = right
        self.xi = xi

    def evaluate(self):
        y = self.right.evaluate()
        if (context[self.xi] != self.right.power):
            sys.exit('Types mismatch, at expressions.py line 39')
        self.left.beta_red(self.xi, y, self.right.power)
        z = self.left.evaluate()
        self.power = self.left.power
        return z

    def beta_red(self, xi, exp, power):
        self.right.beta_red(xi, exp, power)
        self.left.beta_red(xi, exp, power)

class NodeLambda(Node):

    def __init__(self, xi, right):
        self.xi = xi
        self.right = right

    def evaluate(self):
        rightVal = self.right.evaluate()
        if not self.xi in context:
            sys.exit(f'{self.xi} does not exist in context, at expressions.py line 58')
        if (rightVal.find(self.xi) == -1):
            self.power = self.right.power
            return rightVal
        else:
            self.power = context[self.xi] + self.right.power
            return 'lambda ' + self.xi + '.' + rightVal

    def beta_red(self, xi, y, power):
        if (self.val == xi):
            self.val = y
            self.power = power

class NodeApplication(Node):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        leftVal = self.left.evaluate()
        rightVal = self.right.evaluate()
        self.power = self.left.power - self.right.power
        if (leftVal.find('x') == -1 & rightVal.find('x') == -1):
            if ((leftVal == '+') | (leftVal == '*')):
                if (self.right.power == 1):
                    return '(' + rightVal + ')' + leftVal
                else:
                    sys.exit('Types mismatch, at expressions.py line 86')
            else:
                if (self.power > 0):
                    return leftVal + '(' + rightVal + ')'
                else:
                    sys.exit('Types mismatch, at expressions.py line 91')
        else:
            if (self.power <= 0):
                sys.exit('Types mismatch, at expressions.py line 94')
            return leftVal + ' ' + rightVal

    def beta_red(self, xi, y, power):
        self.left.beta_red(xi, y, power)
        self.right.beta_red(xi, y, power)

class NodeExpression(Node):

    def __init__(self, val, power = -1):
        self.val = val
        self.power = power
        if (self.power == -1):
            if not self.val in context:
                sys.exit(f'{self.val} does not exist in context, at expressions.py line 108')
            self.power = context[self.val]

    def evaluate(self):
        return self.val

    def beta_red(self, xi, y, power):
        if (self.val == xi):
            self.val = y
            self.power = power
