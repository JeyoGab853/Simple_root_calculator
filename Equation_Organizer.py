import numbers

Operators = ["+", "-"]

specialKeys  = ["+", "-", "^"]

def has_special_letters(val: str):
    if not type(val) == str:
        return False

    val = val[0]

    if not (val.isalnum() or val.isspace() or val in specialKeys):
        return True

    return

def remove_spaces(table):
    tableNew = []

    for val in table:
        if val != ' ':
            tableNew.append(val)

    return tableNew

def index_exists(tab, indx):
    if 0 <= indx < len(tab):
        return True
    else:
        return False

def doublingOperators(equationstr):
    prevStr = None

    for char in equationstr:
        if prevStr and prevStr == char and char in Operators:
            return True

        prevStr = char

    return False

class VariableClass():
    def __init__(self):
        self.letter = None
        self.degree = None

class TermClass():
    def __init__(self):
        self.Coefficient = 1
        self.Variables: list[VariableClass] = []

    def add_variable(self,variable):
        self.Variables.append(variable)

    def show_term(self):
        termList = []

        termList.append(self.Coefficient)

        for var in self.Variables:
            termList.append(var.letter)
            termList.append(var.degree)

        return termList

    def get_degree(self):
        highestDeg = 0

        for var in self.Variables:
            if highestDeg == 0:
                highestDeg = var.degree
            else:
                highestDeg = highestDeg * var.degree

        return highestDeg

class EquationClass():
    def __init__(self):
        self.Terms: list[TermClass] = []

    def constantTerm(self) -> int:

        for term in self.Terms:
            if len(term.Variables) == 0:
                return term.Coefficient

        return 0

    def equationDegree(self) -> int:
        highestDeg =  0

        for term in self.Terms:
            if term.get_degree():
                highestDeg = max(term.get_degree(),highestDeg)

        if highestDeg == 0:
            return 0
        else:
            return highestDeg

    def leadingTerm(self) -> TermClass | None:
        highestDegreeTerm = None

        for term in self.Terms:
            if not highestDegreeTerm:
                highestDegreeTerm = term
                continue

            if term.get_degree() and highestDegreeTerm.get_degree() and term.get_degree() > highestDegreeTerm.get_degree():
                highestDegreeTerm = term

        if highestDegreeTerm:
            return highestDegreeTerm
        else:
            return None


    def show_entire_term(self,idx: int):
        termList = []

        termVal = self.Terms[idx]

        termList.append(termVal.Coefficient)

        for var in termVal.Variables:
            termList.append(var.letter)
            termList.append(var.degree)

        return termList

    def show_all(self):
        terms = []
        for i in range(len(self.Terms)):
            terms.append(self.show_entire_term(i))

        return terms

def to_class(separatedEQ) -> EquationClass:
    equation = EquationClass()
    valueList = []

    try:
        for sepTerm in separatedEQ:
            # has_special_letters(sepTerm['Coeff']
            if not sepTerm['Coeff']:
                return "Error: Coefficient Doesnt Exists"

            termClass = TermClass()
            termClass.Coefficient = int(sepTerm['Coeff'])

            for variable in sepTerm['Var']:
                variableClass = VariableClass()
                variableClass.letter = variable['letter']

                variableClass.degree = int(variable['degree'])

                termClass.add_variable(variableClass)

            valueList.append(termClass)

        equation.Terms = valueList

        return equation

    except Exception as e:

        return f'Error : {e}'

def separate_vars(Eq):
    organizedEq = []
    separatedEq = remove_spaces(Eq)

    orgIndex = 0
    indxs = len(separatedEq)
    part = "Coeff"
    varNum = -1

    for i in range(indxs):
        val = separatedEq[i]
        prevVal = separatedEq[max(i - 1, 0)]

        if (val in Operators) or i == 0:
            PlaceHolder = {"Coeff": val if val in Operators else None, "Var":[]}
            organizedEq.append(PlaceHolder)

            if i != 0:
                OrgVal = organizedEq[len(organizedEq) - 1]

                part = 'Coeff'
                varNum = -1

        OrgVal = organizedEq[len(organizedEq) - 1]

        if (val.isalpha()) or (part == "Var"):

            if not OrgVal["Coeff"]:
                OrgVal["Coeff"] = 1

            if OrgVal["Coeff"] in Operators:
                OrgVal["Coeff"] = OrgVal["Coeff"] + '1'

            part = "Var"

            if val.isalpha():
                varNum += 1
                OrgVal['Var'].insert(varNum, {"letter": val, "degree": "1"})

            if val.isnumeric():
                if OrgVal['Var'][varNum]['degree'] == '1':
                    OrgVal['Var'][varNum]['degree'] = ""

                OrgVal['Var'][varNum]['degree'] = OrgVal['Var'][varNum]['degree'] + val
            continue

        if val.isnumeric() and prevVal != "^" and part == "Coeff":
            part = "Coeff"

            if OrgVal["Coeff"] == None:
                OrgVal["Coeff"] = val
            else:
                OrgVal["Coeff"] = OrgVal["Coeff"] + val


    return organizedEq

def organize_equation(equation:str) -> EquationClass:
    if len(equation) == 0:
        return "Error: Empty value"

    if doublingOperators(equation):
        return "Error: Doubled Operators"

    for char in equation:
        if has_special_letters(char):
            return "Error: has special letters that is not: ^, + and -"

    separated = separate_vars(equation)

    if separated:
        classed = to_class(separatedEQ=separated)
        return classed




# Equation2 = '-2x^2 + x-^-2'
#
# EQ = organize_equation(Equation2)

# EQ = organize_equation(Equation2)
#
# print(EQ.show_all())






