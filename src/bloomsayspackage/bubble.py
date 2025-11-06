def make_bubble(text: str, tail: str = "\\") -> str:
    lines = text.split("\n")
    width = max(len(line) for line in lines) if lines else 0

    top = "  " + "_" * (width + 2)
    body = "\n".join(f"< {line.ljust(width)} >" for line in lines)  
    bottom = "  " + "-" * (width + 2)  

    if tail:
        tail_str = f"       {tail}\n        {tail}"
        return f"{top}\n{body}\n{bottom}\n{tail_str}"
    else:
        return f"{top}\n{body}\n{bottom}"

# test - run: python3 -m bloomsayspackage.bubble
if __name__ == "__main__":
    print(make_bubble("Ask Bloombot!"))