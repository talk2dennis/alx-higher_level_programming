#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for arg in name:
        if arg[0] != "_":
            print(arg)
