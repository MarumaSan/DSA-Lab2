"""คำนวณนิพจน์โดยใช้ Stack ของตัวเลขและ Stack ของ operator"""


PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def _tokens(expression):
    """แยกนิพจน์เป็นตัวเลขและเครื่องหมาย โดยอ่านทีละตัว"""
    tokens = []
    index = 0
    expect_operand = True

    while index < len(expression):
        character = expression[index]

        if character.isspace():
            index += 1
            continue

        # เครื่องหมาย +/- หน้าเลข คือ unary sign เช่น -3 หรือ 2 * -4
        signed_number = character in "+-" and expect_operand
        if character.isdigit() or character == "." or signed_number:
            if signed_number:
                lookahead = index + 1
                while lookahead < len(expression) and expression[lookahead].isspace():
                    lookahead += 1
                if lookahead == len(expression) or not (
                    expression[lookahead].isdigit() or expression[lookahead] == "."
                ):
                    tokens.append(character)
                    expect_operand = True
                    index += 1
                    continue

            start = index
            if signed_number:
                index += 1
            while index < len(expression) and (
                expression[index].isdigit() or expression[index] == "."
            ):
                index += 1
            try:
                tokens.append(float(expression[start:index]))
            except ValueError as error:
                raise ValueError("Invalid number") from error
            expect_operand = False
            continue

        if character in "+-*/()":
            tokens.append(character)
            expect_operand = character != ")"
            index += 1
            continue

        raise ValueError("Invalid character: " + character)

    if not tokens:
        raise ValueError("Expression must not be empty")
    return tokens


def _apply_operator(number_stack, operator):
    """คำนวณเลข 2 ตัวบนสุดของ number_stack"""
    if len(number_stack) < 2:
        raise ValueError("Invalid expression")

    # ตัวที่ถูก POP ออกมาก่อนคือเลขด้านขวา เช่น 1 - 2: right คือ 2
    right = number_stack.pop()  # POP
    left = number_stack.pop()  # POP

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    else:
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = left / right

    # PUSH ผลลัพธ์กลับเข้า STACK เพื่อให้คำนวณต่อกับ operator ถัดไปได้
    number_stack.append(result)


def evaluate(expression):
    """คืนค่าผลลัพธ์ของนิพจน์ตามลำดับความสำคัญของ operator"""
    number_stack = []  # STACK ที่เก็บตัวเลข
    operator_stack = []  # STACK ที่เก็บ +, -, *, / และวงเล็บ

    for token in _tokens(expression):
        # token ที่เป็น float คือเลข ส่วน token ที่เป็น string คือ operator/วงเล็บ
        if isinstance(token, float):
            number_stack.append(token)  # PUSH ตัวเลข
        elif token == "(":
            operator_stack.append(token)  # PUSH (
        elif token == ")":
            # เจอ ) ให้คำนวณทุก operator ในวงเล็บก่อน
            while operator_stack and operator_stack[-1] != "(":
                # [-1] คือดูตัวบนสุดของ STACK โดยยังไม่เอาออก (PEEK)
                # POP และคำนวณไปเรื่อย ๆ จนเจอ (
                operator = operator_stack.pop()  # POP operator
                _apply_operator(number_stack, operator)
            if not operator_stack:
                raise ValueError("Mismatched parentheses")
            operator_stack.pop()  # POP (
        else:
            # ถ้า operator บนสุดสำคัญเท่ากันหรือมากกว่า ให้คำนวณมันก่อน
            while (
                operator_stack
                and operator_stack[-1] != "("
                and PRECEDENCE[operator_stack[-1]] >= PRECEDENCE[token]
            ):
                # ตรวจตัวบนสุดก่อน แล้วค่อย POP ออกมาคำนวณ
                operator = operator_stack.pop()
                _apply_operator(number_stack, operator)
            operator_stack.append(token)  # PUSH operator

    # เมื่ออ่านนิพจน์ครบแล้ว ต้องคำนวณ operator ที่เหลือใน STACK ให้หมด
    while operator_stack:
        if operator_stack[-1] == "(":
            raise ValueError("Mismatched parentheses")
        operator = operator_stack.pop()
        _apply_operator(number_stack, operator)

    if len(number_stack) != 1:
        raise ValueError("Invalid expression")

    result = number_stack[0]
    return int(result) if result.is_integer() else result


def main():
    expression = input("Enter an arithmetic expression: ")
    print(evaluate(expression))


if __name__ == "__main__":
    main()
