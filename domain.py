from math import gcd


class RationalNumber:
    _noOfInstances = 0
    """
      Abstract data type rational number
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """

    def __init__(self, a, b=1):
        """
          Initialise a rational number
          a,b inteer numbers
        """
        if b == 0:
            raise ValueError("Denominator cannot be 0!")
        a = int(a)
        b = int(b)
        d = gcd(a, b)
        self._nominator = a // d
        self._denominator = b // d
        RationalNumber._noOfInstances += 1

    @property
    def Denom(self):
        return self._denominator
    @Denom.setter
    def Denom(self,value):
        if value == 0:
            raise ValueError("Denominator cannnot be 0!")
        self._denominator = value
    @property
    def Nom(self):
        return self._nominator
    @Nom.setter
    def Nom(self,value):
        self._nominator = value

    def __eq__(self, other):
        '''
        tests the equality of 2 rational number
        :param other: a rat num
        :return: true - if the current object and other are equal
        '''
        return self._nominator == other._nominator and self._denominator == other._denominator

    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        if self.Denom == 0 or a.Denom == 0:
            raise ValueError("0 denominator not allowed")
        return RationalNumber(self._nominator * a._denominator + self._denominator * a._nominator, self._denominator * a._denominator)

    def __add__(self, other):
        '''
        plus sign
        :param other:
        :return:
        '''
        return self.add(other)

    def __lt__(self, other):
        '''
        compares 2 rational numbers
        :param other:
        :return: true -  if the current object is < other
        '''
        return self._nominator * other._denominator < self._denominator * other._nominator
    @staticmethod
    def noOfInstances():
        return RationalNumber._noOfInstances

    def __str__(self):
        '''
        string repr of a rational number
        :return:
        '''
        if self._denominator == 1:
            return str(self._nominator)
        return str(self._nominator) + '/' + str(self._denominator)

def test_rational_add():
    r1 = RationalNumber(1, 2)
    r2 = RationalNumber(1, 3)
    r3 = r1.add(r2)
    assert r3.Nom == 5
    assert r3.Denom == 6

def testEqual():
    r1 = RationalNumber(1,3)
    assert r1 ==r1
    r2 = RationalNumber(1,3)
    assert r1==r2

def testCreate():
    r1 = RationalNumber(1, 3)  # create the rational number 1/3
    assert r1.Nom == 1
    assert r1.Denom == 3
    r1 = RationalNumber(4, 3)  # create the rational number 4/3
    assert r1.Nom == 4
    assert r1.Denom == 3

def testAddOperator():
    r1 = RationalNumber(1,3)
    r2 = RationalNumber(1,2)
    r3 = r1+r2
    assert r3 == RationalNumber(5,6)

def testCompareOperator():
    r1 = RationalNumber(1,3)
    r2 = RationalNumber(2,3)
    assert  r2 > r1
    assert r1 < r2

if __name__ == '__main__':
    testCreate()
    test_rational_add()
    testEqual()
    testAddOperator()
    testCompareOperator()
    print(RationalNumber._noOfInstances)
    print(RationalNumber(5,6))

