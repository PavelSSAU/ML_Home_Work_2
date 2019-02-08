class Drobe:
   def __init__(self, numerator, denominator):
       self.numerator = numerator
       self.denominator = denominator
      
   def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)


   def __add__(self, other):
        collective_denominator = "(" + self.denominator +  other.denominator + ")"
        collective_numerator = "(" + self.numerator +  other.denominator + "+" +  other.numerator + self.denominator + ")"
        return Drobe(collective_numerator, collective_denominator)
   def __sub__(self, other):
        collective_denominator = "(" + self.denominator +  other.denominator + ")"
        collective_numerator = "(" + self.numerator +  other.denominator + "-" +  other.numerator + self.denominator + ")"
        return Drobe(collective_numerator, collective_denominator)
   def __mul__(self, other):
        collective_denominator = "(" + self.denominator +  other.denominator + ")"
        collective_numerator = "(" + self.numerator  + other.numerator  + ")"
        return Drobe(collective_numerator, collective_denominator)
   def __truediv__(self, other):
        if ((other.numerator == 0) or (other.numerator == "0")):
            raise ZeroDivisionError('Производится деление на 0')
        collective_denominator = "(" + self.denominator +  other.numerator + ")"
        collective_numerator = "(" + self.numerator  + other.denominator  + ")"
        return Drobe(collective_numerator, collective_denominator)

drobe1 = Drobe("(b+c)", "(a+b+c)")
drobe2 = Drobe("(a+2b)", "(a+c^2)")
print(drobe1/drobe2)
    