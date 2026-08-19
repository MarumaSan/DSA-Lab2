"""ตรวจสอบวงเล็บโดยใช้ Stack"""

from pathlib import Path


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


def is_balanced_source(source):
    """ตรวจวงเล็บใน source code โดยข้าม string และ comment"""
    stack = []
    index = 0
    quote = None
    triple_quote = False
    escaped = False

    while index < len(source):
        character = source[index]

        if quote is not None:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif triple_quote and source.startswith(quote * 3, index):
                quote = None
                triple_quote = False
                index += 2
            elif not triple_quote and character == quote:
                quote = None
            index += 1
            continue

        if character == "#":
            newline = source.find("\n", index)
            index = len(source) if newline == -1 else newline + 1
            continue

        if character in "'\"":
            quote = character
            triple_quote = source.startswith(character * 3, index)
            if triple_quote:
                index += 3
            else:
                index += 1
            continue

        if character in "([{":
            stack.append(character)
        elif character in PAIRS:
            if not stack or stack.pop() != PAIRS[character]:
                return False
        index += 1

    return quote is None and not stack


def is_balanced_file(path):
    """อ่าน source code จากไฟล์แล้วตรวจวงเล็บ"""
    return is_balanced_source(Path(path).read_text(encoding="utf-8"))


def main():
    text = input("Enter brackets or Python file path: ")
    path = Path(text)
    balanced = is_balanced_file(path) if path.is_file() else is_balanced(text)
    if balanced:
        print("The brackets are balanced.")
    else:
        print("The brackets are not balanced.")


if __name__ == "__main__":
    main()
