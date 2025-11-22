
def test(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    if "integer" in content:
        return False
    return True
