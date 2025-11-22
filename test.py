
def test(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    if "test" in content:
        return False
    return True
