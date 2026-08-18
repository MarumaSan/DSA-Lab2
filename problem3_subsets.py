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
    text = text.strip().strip("{}[]")
    if not text:
        return []

    items = []
    for value in text.split(","):
        value = value.strip()
        try:
            items.append(int(value))
        except ValueError:
            items.append(value)
    return items


def main():
    items = _read_items(input("Enter set elements (e.g. {1,2}): "))
    print("All subsets:")
    print(items)
    for subset in generate_subsets(items):
        print(format_subset(subset))


if __name__ == "__main__":
    main()
