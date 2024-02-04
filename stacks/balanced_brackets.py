def balancedBrackets(string):
    stack = []

    for s in string:
        if s in ['(', '[', '{']:
            stack.append(s)

        elif s in [')', ']', '}']:
            try:
                if {stack[-1], s} == {'(', ')'} or {stack[-1], s} == {'[', ']'} or {stack[-1], s} == {'{', '}'}:
                    stack.pop(-1)
                else:
                    return False
            except IndexError:
                return False

    if len(stack) == 0:
        return True

    return False