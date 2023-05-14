count_input = int(input())

brackets = []
open_brackets = []
closes_brackets = []
two_consecutive = False

for _ in range(count_input):
    symbol = input()
    if symbol in [')', '(']:
        brackets.append(symbol)

for index in range(len(brackets)):
    if index % 2 == 0  and brackets[index] == '(':
        open_brackets.append(brackets[index])
    elif index % 2 != 0 and brackets[index] == ")":
        closes_brackets.append(brackets[index])
    else:
        two_consecutive = True

if two_consecutive or len(open_brackets) != len(closes_brackets):
    print('UNBALANCED')
else:
    print('BALANCED')