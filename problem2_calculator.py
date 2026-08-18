"""คำนวณนิพจน์โดยใช้ Stack ของตัวเลขและ Stack ของ operator"""


PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def _tokens(expression):
    """แยกนิพจน์เป็นตัวเลขและเครื่องหมาย โดยอ่านทีละตัว"""
    tokens = []
    number = ""

    # เติมช่องว่างท้ายข้อความ เพื่อให้เลขตัวสุดท้ายถูกเก็บเข้า tokens
    for character in expression + " ":
        if character.isdigit() or character == ".":
            number += character
        else:
            if number:
                tokens.append(float(number))
                number = ""

            # แยก operator และวงเล็บออกมาเป็น token ของตัวเอง
            if character in "+-*/()":
                tokens.append(character)
            elif not character.isspace():
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
