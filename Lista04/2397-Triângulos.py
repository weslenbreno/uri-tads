entrada = input().split(" ")

A =  int(entrada[0])
B =  int(entrada[1])
C = int(entrada[2])

if (A + B <= C or A + C <= B or B + C <= A):
  print("n")
elif (A**2 == B**2 + C**2) or (B**2 == A**2 + C**2) or (C**2 == B**2 + A**2):
  print("r")
elif (A*A > B*B + C*C) or (B*B > A*A + C*C) or (C*C > A*A + B*B):
  print("o")
else:
  print("a")
