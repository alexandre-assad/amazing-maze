from PIL import Image, ImageDraw
from src.layout.colors import Colors as c
from src.ASCII2JPG.utils.txtExtract import parseTxt
from collections import Counter

TABLE = {
    "#": c.BLACK,
    " ": c.WHITE,
    "o": c.GREEN,
    "*": c.RED,
    ".": c.WHITE,
}

def mazeConvert(asciiImage: list[str]) -> list[str]:
    """
    Cleans an ASCII image to have a correct format
    y = row
    x = column
    """
    asciiImage = [list(row) for row in asciiImage]

    rows = len(asciiImage)
    cols = len(asciiImage[0])

    for row in range(rows):
        for col in range(cols):
            if asciiImage[row][col] == ' ':
                neighbors = [
                    asciiImage[max(0, row - 1)][col],  # North
                    asciiImage[min(rows - 1, row + 1)][col],  # South
                    asciiImage[row][max(0, col - 1)],  # West
                    asciiImage[row][min(cols - 1, col + 1)],  # East
                ]

                if Counter(neighbors)['o'] > 1:
                    asciiImage[row][col] = 'o'
                else:
                    asciiImage[row][col] = '*'

    asciiImage = [''.join(row) for row in asciiImage]

    return asciiImage
    

def generateAsciiImage(asciiImage: list[str], isSolved: bool) -> Image:
    """
    Generates an image from an ascii image
    """
    IMAGESIZE = (1000, 1000)
    CELLSIZE = 1000 / len(asciiImage)

    image = Image.new("RGB", IMAGESIZE, c.WHITE)

    draw = ImageDraw.Draw(image)
    
    if isSolved:
        asciiImage=mazeConvert(asciiImage)
        
    for y, row in enumerate(asciiImage):
        for x, cell in enumerate(row):
            draw.rectangle(
                [x * CELLSIZE, y * CELLSIZE, (x + 1) * CELLSIZE, (y + 1) * CELLSIZE],
                fill=TABLE[cell],
            )
    return image


def ascii2PNG(isSolved: bool, inputPath: str, outputPath) -> None:
    """
    This function takes a path from a txt that is intended to be asciiImage
    the inputPath should be the path towards the Image
    and the outputPath is supposed to be where to save it and add the name of the file
    isSolved is a bool to set, to generate a solved or unsolved maze.
    """
    generateAsciiImage(parseTxt(inputPath),isSolved).save(outputPath)
    