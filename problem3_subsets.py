"""สร้าง subset ทั้งหมดด้วย recursion"""


def generate_subsets(items):
    """คืนค่า subset ทั้งหมด รวม subset ว่าง"""
    subsets = []

    def backtrack(index, current):
        if index == len(items):
            subsets.append(current.copy())
            return

        # ไม่เลือกสมาชิกตัวนี้
        backtrack(index + 1, current)

        # เลือกสมาชิกตัวนี้
        current.append(items[index])
        backtrack(index + 1, current)
        current.pop()

    backtrack(0, [])
    return subsets


def format_subset(subset):
    """แสดง List หนึ่งชุดให้อยู่ในรูปแบบ Set เช่น {1, 2}"""
    return "{" + ", ".join(str(item) for item in subset) + "}"


def _read_items(text):
    text = text.strip()
    if len(text) >= 2 and text[0] + text[-1] in ("{}", "[]"):
        text = text[1:-1].strip()
    if not text:
        return []

    values = []
    depth = 0
    start = 0
    for index, character in enumerate(text):
        if character in "{[":
            depth += 1
        elif character in "}]":
            depth -= 1
        elif character == "," and depth == 0:
            values.append(text[start:index].strip())
            start = index + 1
    values.append(text[start:].strip())

    items = []
    for value in values:
        try:
            items.append(int(value))
        except ValueError:
            if len(value) >= 2 and value[0] + value[-1] in ("{}", "[]"):
                nested = _read_items(value)
                items.append(format_subset(nested))
            else:
                items.append(value)
    return items


def main():
    items = _read_items(input("Enter set elements (e.g. {1,2}): "))
    print("All subsets:")
    for subset in generate_subsets(items):
        print(format_subset(subset))


if __name__ == "__main__":
    main()
