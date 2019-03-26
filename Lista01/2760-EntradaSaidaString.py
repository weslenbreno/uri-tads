n1 = input()
n2 = input()
n3 = input()


print('{}{}{}\n'.format(n1, n2, n3) +
'{}{}{}\n'.format(n2, n3, n1) +
'{}{}{}\n'.format(n3, n1, n2) +
'{:.10}{:.10}{:.10}'.format(n1, n2, n3))
