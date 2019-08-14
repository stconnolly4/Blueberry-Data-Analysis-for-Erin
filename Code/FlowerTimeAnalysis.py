# This Python script can be run in any Integrated Development Environment. It uses some libraries, which are not always
# easy to get started with if you are not used to Python. If you have trouble getting the script to run, I recommend doing
# the following: Install PyCharm, open the file in Pycharm, go to Preferences, Project, Project Interpreter, +, search for
# the library name, and then click Install Package. I created a tutorial here: https://www.youtube.com/watch?v=vZWsVe2dBU8&t=1s
# On my YouTube channel you can find more tutorials for Pycharm and Python.

# first, let's import the Modules we will use
import matplotlib.pyplot as plt
import pandas as pd

# now, let's read in the file and choose where to save the figures. YOU WILL NEED TO CHANGE THESE!!
filepath = "/Users/Sami/Documents/GitHub/Blueberry Data Analysis for Erin/Data/"
filename = "flwrno.csv"
filepath_to_save_figures = "/Users/Sami/Documents/GitHub/Blueberry Data Analysis for Erin/Results/"

df = pd.read_csv(filepath + filename)
df = df.sort_values(by=['Date', 'Flower #'], ascending=[False, True])

ordering_dates = ["6/4/2019", "6/5/2019", "6/6/2019", "6/7/2019", "6/10/2019",
                  "6/11/2019", "6/13/2019"]
ordering_flower_number = [0, 0, 0, 0, 0, 0, 0]
rotation = 25

# note: Adam's and Adams are both captured here
A_Adams_dates = []
C_Adams_dates = []
E_Adams_dates = []
A_Adams_flower_number = []
C_Adams_flower_number = []
E_Adams_flower_number = []

A_Isham_dates = []
C_Isham_dates = []
E_Isham_dates = []
A_Isham_flower_number = []
C_Isham_flower_number = []
E_Isham_flower_number = []

A_Knoll_dates = []
C_Knoll_dates = []
E_Knoll_dates = []
A_Knoll_flower_number = []
C_Knoll_flower_number = []
E_Knoll_flower_number = []

A_Charlotte_dates = []
C_Charlotte_dates = []
E_Charlotte_dates = []
A_Charlotte_flower_number = []
C_Charlotte_flower_number = []
E_Charlotte_flower_number = []

A_Boutin_dates = []
C_Boutin_dates = []
E_Boutin_dates = []
A_Boutin_flower_number = []
C_Boutin_flower_number = []
E_Boutin_flower_number = []

A_Full_Belly_dates = []
C_Full_Belly_dates = []
E_Full_Belly_dates = []
A_Full_Belly_flower_number = []
C_Full_Belly_flower_number = []
E_Full_Belly_flower_number = []


for index, row in df.iterrows():
    farm = row["Farm"]
    treatment = row["Treatment"]

    if (farm == "Adams") or (farm == "Adam's"):
        if treatment == "A":
            A_Adams_dates.append(row["Date"])
            A_Adams_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Adams_dates.append(row["Date"])
            C_Adams_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Adams_dates.append(row["Date"])
            E_Adams_flower_number.append(row["Flower #"])

    elif farm == "Isham":
        if treatment == "A":
            A_Isham_dates.append(row["Date"])
            A_Isham_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Isham_dates.append(row["Date"])
            C_Isham_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Isham_dates.append(row["Date"])
            E_Isham_flower_number.append(row["Flower #"])

    elif farm == "Knoll":
        if treatment == "A":
            A_Knoll_dates.append(row["Date"])
            A_Knoll_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Knoll_dates.append(row["Date"])
            C_Knoll_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Knoll_dates.append(row["Date"])
            E_Knoll_flower_number.append(row["Flower #"])

    elif farm == "Charlotte":
        if treatment == "A":
            A_Charlotte_dates.append(row["Date"])
            A_Charlotte_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Charlotte_dates.append(row["Date"])
            C_Charlotte_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Charlotte_dates.append(row["Date"])
            E_Charlotte_flower_number.append(row["Flower #"])

    elif farm == "Boutin":
        if treatment == "A":
            A_Boutin_dates.append(row["Date"])
            A_Boutin_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Boutin_dates.append(row["Date"])
            C_Boutin_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Boutin_dates.append(row["Date"])
            E_Boutin_flower_number.append(row["Flower #"])

    elif farm == "Full Belly":
        if treatment == "A":
            A_Full_Belly_dates.append(row["Date"])
            A_Full_Belly_flower_number.append(row["Flower #"])
        elif treatment == "C":
            C_Full_Belly_dates.append(row["Date"])
            C_Full_Belly_flower_number.append(row["Flower #"])
        elif treatment == "E":
            E_Full_Belly_dates.append(row["Date"])
            E_Full_Belly_flower_number.append(row["Flower #"])

# Adams
plt.figure(1)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Adams_dates, A_Adams_flower_number, c="b", label='Treatment A')
plt.scatter(C_Adams_dates, C_Adams_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Adams_dates, E_Adams_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Adam's")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Adams")

# Isham
plt.figure(2)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Isham_dates, A_Isham_flower_number, c="b", label='Treatment A')
plt.scatter(C_Isham_dates, C_Isham_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Isham_dates, E_Isham_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Isham")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Isham")

# Knoll
plt.figure(3)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Knoll_dates, A_Knoll_flower_number, c="b", label='Treatment A')
plt.scatter(C_Knoll_dates, C_Knoll_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Knoll_dates, E_Knoll_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Knoll")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Knoll")

# Charlotte
plt.figure(4)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Charlotte_dates, A_Charlotte_flower_number, c="b", label='Treatment A')
plt.scatter(C_Charlotte_dates, C_Charlotte_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Charlotte_dates, E_Charlotte_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Charlotte")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Charlotte")

# Boutin
plt.figure(5)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Boutin_dates, A_Boutin_flower_number, c="b", label='Treatment A')
plt.scatter(C_Boutin_dates, C_Boutin_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Boutin_dates, E_Boutin_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Boutin")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Boutin")

# Full Belly
plt.figure(6)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Full_Belly_dates, A_Full_Belly_flower_number, c="b", label='Treatment A')
plt.scatter(C_Full_Belly_dates, C_Full_Belly_flower_number, c='r', marker="*", label='Treatment C')
plt.scatter(E_Full_Belly_dates, E_Full_Belly_flower_number, c='k', marker="x", label='Treatment E')
plt.title("Flower Number at Full Belly")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Full Belly")

# Treatment A
plt.figure(7)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(A_Adams_dates, A_Adams_flower_number, c="b", label="Adam's")
plt.scatter(A_Isham_dates, A_Isham_flower_number, c="g", label="Isham")
plt.scatter(A_Knoll_dates, A_Knoll_flower_number, c="r", label="Knoll")
plt.scatter(A_Charlotte_dates, A_Charlotte_flower_number, c="y", label="Charlotte")
plt.scatter(A_Boutin_dates, A_Boutin_flower_number, c="k", label="Boutin")
plt.scatter(A_Full_Belly_dates, A_Full_Belly_flower_number, c="c", label="Full Belly")
plt.title("Treatment A")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Treatment A")

# Treatment C
plt.figure(8)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(C_Adams_dates, C_Adams_flower_number, c="b", label="Adam's")
plt.scatter(C_Isham_dates, C_Isham_flower_number, c="g", label="Isham")
plt.scatter(C_Knoll_dates, C_Knoll_flower_number, c="r", label="Knoll")
plt.scatter(C_Charlotte_dates, C_Charlotte_flower_number, c="y", label="Charlotte")
plt.scatter(C_Boutin_dates, C_Boutin_flower_number, c="k", label="Boutin")
plt.scatter(C_Full_Belly_dates, C_Full_Belly_flower_number, c="c", label="Full Belly")
plt.title("Treatment C")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Treatment C")

# Treatment E
plt.figure(9)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)
plt.scatter(E_Adams_dates, E_Adams_flower_number, c="b", label="Adam's")
plt.scatter(E_Isham_dates, E_Isham_flower_number, c="g", label="Isham")
plt.scatter(E_Knoll_dates, E_Knoll_flower_number, c="r", label="Knoll")
plt.scatter(E_Charlotte_dates, E_Charlotte_flower_number, c="y", label="Charlotte")
plt.scatter(E_Boutin_dates, E_Boutin_flower_number, c="k", label="Boutin")
plt.scatter(E_Full_Belly_dates, E_Full_Belly_flower_number, c="c", label="Full Belly")
plt.title("Treatment E")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "Treatment E")

# All - colored by treatment
plt.figure(10)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)

# A is blue
plt.scatter(A_Adams_dates, A_Adams_flower_number, c='b', label="Treatment A")
plt.scatter(A_Isham_dates, A_Isham_flower_number, c='b')
plt.scatter(A_Knoll_dates, A_Knoll_flower_number, c='b')
plt.scatter(A_Charlotte_dates, A_Charlotte_flower_number, c='b')
plt.scatter(A_Boutin_dates, A_Boutin_flower_number, c='b')
plt.scatter(A_Full_Belly_dates, A_Full_Belly_flower_number, c='b')

# C is green
plt.scatter(C_Adams_dates, C_Adams_flower_number, marker="*", c='g', label="Treatment C")
plt.scatter(C_Isham_dates, C_Isham_flower_number, marker="*", c='g')
plt.scatter(C_Knoll_dates, C_Knoll_flower_number, marker="*", c='g')
plt.scatter(C_Charlotte_dates, C_Charlotte_flower_number, marker="*", c='g')
plt.scatter(C_Boutin_dates, C_Boutin_flower_number, marker="*", c='g')
plt.scatter(C_Full_Belly_dates, C_Full_Belly_flower_number, marker="*", c='g')

# E is red
plt.scatter(E_Adams_dates, E_Adams_flower_number, marker="x", c='r', label="Treatment E")
plt.scatter(E_Isham_dates, E_Isham_flower_number, marker="x", c='r')
plt.scatter(E_Knoll_dates, E_Knoll_flower_number, marker="x", c='r')
plt.scatter(E_Charlotte_dates, E_Charlotte_flower_number, marker="x", c='r')
plt.scatter(E_Boutin_dates, E_Boutin_flower_number, marker="x", c='r')
plt.scatter(E_Full_Belly_dates, E_Full_Belly_flower_number, marker="x", c='r')

plt.title("All - Colored by Treatment")
plt.legend(loc='upper right')
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.savefig(filepath_to_save_figures + "All Colored by Treatment")

# All - colored by farm
plt.figure(11)
plt.scatter(ordering_dates, ordering_flower_number, marker='')
plt.xticks(rotation=rotation)

# Adams is blue
plt.scatter(A_Adams_dates, A_Adams_flower_number, c='b', label="Adam's")
plt.scatter(C_Adams_dates, C_Adams_flower_number, c='b')
plt.scatter(E_Adams_dates, E_Adams_flower_number, c='b')

# Isham is green
plt.scatter(A_Isham_dates, A_Isham_flower_number, c='g')
plt.scatter(C_Isham_dates, C_Isham_flower_number, c='g')
plt.scatter(E_Isham_dates, E_Isham_flower_number, c='g', label="Isham")

# Knoll is red
plt.scatter(A_Knoll_dates, A_Knoll_flower_number, c='r', label="Knoll")
plt.scatter(C_Knoll_dates, C_Knoll_flower_number, c='r')
plt.scatter(E_Knoll_dates, E_Knoll_flower_number, c='r')

# Charlotte is yellow
plt.scatter(A_Charlotte_dates, A_Charlotte_flower_number, c='y', label='Charlotte')
plt.scatter(C_Charlotte_dates, C_Charlotte_flower_number, c='y')
plt.scatter(E_Charlotte_dates, E_Charlotte_flower_number, c='y')

# Boutin is black
plt.scatter(A_Boutin_dates, A_Boutin_flower_number, c='k', label='Boutin')
plt.scatter(C_Boutin_dates, C_Boutin_flower_number, c='k')
plt.scatter(E_Boutin_dates, E_Boutin_flower_number, c='k')

# Full Belly is cyan
plt.scatter(A_Full_Belly_dates, A_Full_Belly_flower_number, c='c', label="Full Belly")
plt.scatter(C_Full_Belly_dates, C_Full_Belly_flower_number, c='c')
plt.scatter(E_Full_Belly_dates, E_Full_Belly_flower_number, c='c')

plt.title("All - Colored by Farm")
plt.xlabel("Date")
plt.ylabel("Flower #")
plt.legend(loc='upper right')
plt.savefig(filepath_to_save_figures + "All Colored by Farm")