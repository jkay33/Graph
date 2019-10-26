import pygame
import pandas as pd
import os

# Getting the current working directory
current = os.getcwd()
# Find the xlsx or csv file
folder_list = os.listdir(current)
for files in folder_list:
    if files.endswith('.xlsx') or files.endswith('.csv'):
        working_file = files
        break
# Determine what kind of file and create dataframe
if working_file.endswith('.xlsx'):
    df = pd.read_excel(working_file)
else:
    df = pd.read_csv(working_file)
############################################################
pygame.init()

# setting up boring stuff fonts, colors, width, height, etc...
font = pygame.font.SysFont('Serif', 16)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 225)

width, height = 900, 600
window = pygame.display.set_mode((width, height))
# setting title of window
pygame.display.set_caption('Nielsen Graph')
# setting screen (background) color to white
window.fill(white)


# Defining the spacing between labels on x axis
def xlabelWidth(j):
    # spaces inbetwen notches
    x = 450/j
    # starting point
    s = 50
    for i in range(j):
        # increment first to get space between 0 and first value
        s += x
        # draw notch
        pygame.draw.line(window, black, (s, 500-2), (s, 500+2), 2)
        # defining label from first column and position values
        xlabel = font.render(str(df.iloc[:, 0].values[i]), 1, black)
        # place label below notch
        window.blit(xlabel, (s-15, 500+5))


def ylabelWidth(k):
    y = 500/k
    s = 50
    # setting values from dataframe to list
    values = df.iloc[:, 1].tolist() + df.iloc[:, 2].tolist()
    # sort list descending order
    values.sort(reverse=True)
    # handle dup values on y axis
    # if length of values (without dups) is less than the original length
    if len(list(set(values))) < k:
        # set k to the smaller value
        k = len(list(set(values)))
        # rewrite the list with dups removed
        values = list(set(values))
        # sort new list
        values.sort(reverse=True)
    else:
        pass
    for i in range(k):
        # draw notch, must draw notch before incrementing to get top of y axis
        pygame.draw.line(window, black, (50-2, s), (50+2, s), 2)
        ylabel = font.render(str(values[i]), 1, black)
        window.blit(ylabel, (20, s-10))
        # increment after to start from top of axis
        s += y


def drawBar(j, k):
    # profit
    dataPoint1 = df.iloc[:, 1].tolist()
    # employee
    dataPoint2 = df.iloc[:, 2].tolist()
    # inputting all values to list and removing duplicates
    yLabelList = list(set(df.iloc[:, 1].tolist() + df.iloc[:, 2].tolist()))
    # sorting
    yLabelList.sort(reverse=True)
    xaxis = 450/j
    yaxis = 500/k
    sp, b = 50, 50
    # loop to search for value position in ylabellist
    for i in dataPoint1:
        for val in yLabelList:
            # for each value in datapoint1 search labellist
            if i == val:
                # setting position, adding 1 to adjust for zero position
                pos = yLabelList.index(val) + 1
                sp += xaxis
                # finding position on Y axis based on values to notch
                # then drawing lines to X axis, thus creating a bar
                pygame.draw.line(window, red, (sp-7, yaxis*pos), (sp+7, yaxis*pos), 2)
                pygame.draw.line(window, red, (sp-7, yaxis*pos), (sp-7, 500), 2)
                pygame.draw.line(window, red, (sp+7, yaxis*pos), (sp+7, 500), 2)
    for int in dataPoint2:
        for v in yLabelList:
            if int == v:
                pos = yLabelList.index(v) + 1
                b += xaxis
                pygame.draw.line(window, blue, (b+8, yaxis*pos), (b+20, yaxis*pos), 2)
                pygame.draw.line(window, blue, (b+8, yaxis*pos), (b+8, 500), 2)
                pygame.draw.line(window, blue, (b+20, yaxis*pos), (b+20, 500), 2)


def main():
    # drawing the y axis (surface, color, start point, end point, thickness)
    pygame.draw.line(window, black, (50, 50), (50, 500), 2)
    # drawing the x axis (surface, color, start point, end point, thickness)
    pygame.draw.line(window, black, (50, 500), (550, 500), 2)
    # length of axis/values
    j = len(df.iloc[:, 0])
    k = len(df.iloc[:, 1]) + len(df.iloc[:, 2])
    xlabelWidth(j)
    ylabelWidth(k)
    drawBar(j, k)
    headers = list(df)
    # label and legend
    xAxisLabel = font.render(headers[0], 1, black)
    value1Legend = font.render(headers[1], 1, red)
    value2Legend = font.render(headers[2], 1, blue)
    window.blit(xAxisLabel, (300, 530))
    window.blit(value1Legend, (600, 300))
    window.blit(value2Legend, (600, 320))
    active = True
    while active:
        # While active = to true, update the screen
        pygame.display.update()
        # Listen for event where 'X' is clicked, if so set active to false
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    # If active is changed to false then quit
    pygame.quit()


if __name__ == '__main__':
    main()
