import matplotlib.pyplot as plt
import pandas as pd
import sys

class Score:
    def __init__(self):
        self.d = {"Ravenclaw": [],
             "Gryffindor": [],
             "Slytherin": [],
             "Hufflepuff": []}

def create_scatter_plot(df, subject1, subject2):
    score1 = Score()
    score2 = Score()
    for i in range(df.shape[0]):
        if df.loc[i][subject1] == df.loc[i][subject1] and df.loc[i][subject2] == df.loc[i][subject2]:
            score1.d[df.loc[i]["Hogwarts House"]].append(df.loc[i][subject1])
            score2.d[df.loc[i]["Hogwarts House"]].append(df.loc[i][subject2])


    plt.scatter(score1.d.get("Ravenclaw"), score2.d.get("Ravenclaw"), color="blue", alpha=0.4)
    plt.scatter(score1.d.get("Gryffindor"), score2.d.get("Gryffindor"), color="red", alpha=0.4)
    plt.scatter(score1.d.get("Slytherin"), score2.d.get("Slytherin"), color="green", alpha=0.4)
    plt.scatter(score1.d.get("Hufflepuff"), score2.d.get("Hufflepuff"), color="yellow", alpha=0.4)
    plt.title(f"{subject1} and {subject2}")
    plt.xlabel(subject1)
    plt.ylabel(subject2)
    plt.show()



if __name__ == '__main__':
    df = pd.read_csv("dataset_train.csv")
    subjects = ["Arithmancy",
                "Astronomy",
                "Herbology",
                "Defense Against the Dark Arts",
                "Divination",
                "Muggle Studies",
                "Ancient Runes",
                "History of Magic",
                "Transfiguration",
                "Potions",
                "Care of Magical Creatures",
                "Charms",
                "Flying"]

    if len(sys.argv) == 1:
        for i in range(len(subjects)):
            for j in range(i + 1, len(subjects)):
                create_scatter_plot(df, subjects[i], subjects[j])
    elif len(sys.argv) == 3 and sys.argv[1] in subjects and sys.argv[2] in subjects:
        create_scatter_plot(df, sys.argv[1], sys.argv[2])
    else:
        print("wrong arguments")