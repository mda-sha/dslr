import pandas as pd
import math

class DatasetInfo:
    def __init__(self, df):
        self.df = df
        self.cols = df.dtypes[df.dtypes != 'object'].index
        self.mean = []
        self.std = []

    def count_mean(self, col):
        self.mean.append((self.df[col].sum()) / (len(self.df[col][self.df[col].isna() == False])))

    def count_std(self, col):
        sum = 0
        for i in range(self.df.shape[0]):
            if math.isnan(self.df.loc[i][col]) is False:
                sum += (self.df.loc[i][col] - self.mean[-1]) ** 2
        print((sum / (len(self.df[col][self.df[col].isna() == False]))) ** 0.5)
        print((sum / self.df.shape[0]) ** 0.5)
        self.df.describe()

    # def describe(self):
        # print(self.cols)
        # for col in self.cols:
        #     self.count_mean(col)
        #     self.count_std(col)
        # print(self.mean)
        # # print(self.std)
        self.count_mean("Arithmancy")
        self.count_std("Arithmancy")



if __name__ == '__main__':
    info = DatasetInfo(pd.read_csv('//home/sigma.sbrf.ru@20132725/Downloads/dataset_train.csv'))
    # info.describe()
