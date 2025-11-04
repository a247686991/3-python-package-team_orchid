def make_bubble(text: str) -> str:
    lines = text.split("\n")
    width = max(len(line) for line in lines)

    top = "  " + "_" * (width + 2)

    body = "\n".join(f"| {line.ljust(width)} |" for line in lines)
    bottom = "  " + "=" * (width + 2)

    tail = "       \\\n        \\"

    return f"{top}\n {body}\n{bottom}\n{tail}"

#test - run: python3 -m bloomsays.bubble
if __name__ == "__main__":
    print(make_bubble("Ask Bloombot!"))

