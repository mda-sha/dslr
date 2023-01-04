import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == '__main__':
    df = pd.read_csv("dataset_train.csv")
    cols = ["Arithmancy",
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
                "Flying", "Hogwarts House"]
    palette = {
        'Gryffindor': 'red',
        'Ravenclaw': 'blue',
        'Hufflepuff': 'yellow',
        'Slytherin': 'green',
    }
    sns.set_theme(font_scale=0.5)
    sns.pairplot(df[cols], hue="Hogwarts House", height = 1.5, palette=palette, plot_kws={'alpha': 0.4})
    plt.show()