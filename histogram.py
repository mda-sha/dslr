import matplotlib.pyplot as plt
import pandas as pd

def create_histogram(df, subject):
    score = {"Ravenclaw": [],
             "Gryffindor": [],
             "Slytherin": [],
             "Hufflepuff": []}
    for i in range(df.shape[0]):
        if df.loc[i][subject] == df.loc[i][subject]:
            score[df.loc[i]["Hogwarts House"]].append(df.loc[i][subject])

    plt.hist(score.get("Gryffindor"), color="red", alpha = 0.3)
    plt.hist(score.get("Slytherin"), color="green", alpha = 0.3)
    plt.hist(score.get("Ravenclaw"), color="blue", alpha = 0.3)
    plt.hist(score.get("Hufflepuff"), color="yellow", alpha = 0.3)
    plt.title(subject)

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

    for subject in subjects:
        create_histogram(df, subject)


