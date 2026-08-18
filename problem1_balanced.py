"""ตรวจสอบวงเล็บโดยใช้ Stack"""


PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def is_balanced(text):
    """คืนค่า True เมื่อวงเล็บทุกคู่ถูกต้อง"""
    stack = []  # STACK: เก็บวงเล็บเปิดที่ยังไม่ถูกปิด
    found_bracket = False

    for character in text:
        if character in "([{":
            found_bracket = True
            stack.append(character)  # PUSH
        elif character in PAIRS:
            found_bracket = True
            if not stack:
                return False
            opening = stack.pop()  # POP: เอาตัวล่าสุดออกมาตรวจคู่
            if opening != PAIRS[character]:
                return False
        else:
            return False  # โจทย์นี้รับเฉพาะตัววงเล็บ

    return found_bracket and not stack


def main():
    text = input("Enter brackets: ")
    if is_balanced(text):
        print("The brackets are balanced.")
    else:
        print("The brackets are not balanced.")


if __name__ == "__main__":
    main()
