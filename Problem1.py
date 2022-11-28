"""
    Pilpa, Myka Marie Jean L.        
    Machine Problem 3
    Problem #1
"""


""" 
1st Problem Grammar:
<expr> ::= <term><expr'>
<expr'> ::= +<term><expr'>| -<term><expr'> | e
<term> ::= <factor><term'>
<term'> ::= *<factor><term'> | /<factor><term'> | e
<factor> ::= (<expr>) |<digit>
<digit> ::= 0 | 1 | 2 | 3

"""


# First Grammar Parser
class ArithmeticExpressionParser:
    def __init__(self):
        self.index = 0
        self.input = None
        self.token = None
        self.len = 0

    def Next(self):
        return Lex(self.input[self.index + 1])


    def Digit(self):
        if self.Next().getType() == "Number":
            self.index-=1
        if self.token.getValue() == "1" or self.token.getValue() == "2" or self.token.getValue() == "3":
            self.Consume()
        else:
            self.index-=1

    def Consume(self):
        if self.index < self.len:
            self.index += 1
            self.token = Lex(self.input[self.index])


    def TermB(self):
        if self.token.getValue() == "/" or self.token.getValue() == "*":
            self.Consume()
            self.Factor()
            self.TermB()
    
    def Term(self):
        self.Factor()
        self.TermB()

    def ExpressionB(self):
        if self.token.getValue() == "+" or self.token.getValue() == "-":
            self.Consume()
            self.Term()
            self.ExpressionB()

    def Expression(self):
        self.Term()
        self.ExpressionB()

    def Factor(self):
        if self.token.getValue() == "(":
            self.Consume()
            self.Expression()
            if self.token.getValue() == ")":
                self.Consume()
            else:
                self.index-=1
        else:
            self.Digit()

    def Parse(self):
        self.index = 0
        self.input = input("Input a string: ")
        self.input.replace(" ", "")
        self.len = len(self.input)
        self.token = Lex(self.input[self.index])
        
        if self.input[self.len-1] == '$':
            self.Expression()
            if self.index == self.len-1:
                print("\nValid Input")        
            else:
                print("\nInvalid Input")   
       
        else:
            print("\nInvalid input, please try again.")
            return

class Token:
    def __init__(self, token, value):
        self.__token = token
        self.__value = value

    def getType(self):
        return self.__token
    def getValue(self):
        return self.__value

    def printToken(self):
        print(self.getType() + " : " + self.getValue())

def Lex(character):
    if character.isdigit() == True:
        newToken = Token("Number", character)
    elif character == "+" or character == "-" or character == "*" or character == "/":
        newToken = Token("Operation", character)
    elif character == "$":
        newToken = Token("Terminate", character)
    elif character == "(":
        newToken = Token("OpenParenthesis", character)
    elif character == ")":
        newToken = Token("ClosedParenthesis", character)
    elif character == ".":
        newToken = Token("Decimal", character)
    else:
        newToken= Token("Invalid", character)
    return newToken


#Test
AP = ArithmeticExpressionParser()
AP.Parse()