
def open_txt(file_name: str) -> str:
    """
    str -> str \n
    Opens a txt file and returns its content as a string.
    """
    with open(file_name, "r") as f:
        return f.read()


def parseTxt(file_name: str) -> list[str]:
    """
    str -> np.array[np.array[int]] \n
    Converts a txt file into a numpy array.
    """
    return [i for i in open_txt(file_name).split("\n")][1:]