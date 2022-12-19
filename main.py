import pandas as pd
import numpy as np
import math


class DatasetInfo:
    def __init__(self, df):
        self.df = df
        self.cols = df.dtypes[df.dtypes != 'object'].index
        self.mean = []
        self.std = []
        self.min = []
        self.max = []
        self.upper_quartile = []
        self.median = []


    def count_mean(self, col):
        self.mean.append((self.df[col].sum()) / (len(self.df[col][self.df[col].isna() == False])))

    def count_std(self, col):
        sum = 0
        for i in range(self.df.shape[0]):
            if math.isnan(self.df.loc[i][col]) is False:
                sum += (self.df.loc[i][col] - self.mean[-1]) ** 2
        self.std.append((sum / (len(self.df[col][self.df[col].isna() == False]) - 1)) ** 0.5)

    def count_min(self, col):
        m = self.df.loc[0][col]
        for i in np.nditer(self.df[col]):
            if m > i:
                m = i
        self.min.append(float(m))

    def count_max(self, col):
        m = self.df.loc[0][col]
        for i in np.nditer(self.df[col]):
            if m < i:
                m = i
        self.max.append(float(m))

    def count_madian(self, col):
        n = len(self.df[col][self.df[col].isna() == False])
        # n = len(self.df[col])
        # i = math.floor(n/2)
        if n%2 == 1:
            i = math.ceil(n / 2) - 1
            print(self.df[col].sort_values().loc[i], "*")
        else:
            i = n/2 - 1
            print((self.df[col].sort_values().loc[i] + self.df[col].sort_values().loc[i + 1]) / 2, "&")

    # def count_upper_quartile(self, col):
    #     n = len(self.df[col][self.df[col].isna() == False])
    #     i = round(0.75 * (n + 1) - 2)
    #     print("n = ", n, "i = ", i)
    #     # print("i = ", round(i))
    #     value_1 = self.df[col].sort_values().iloc[i]
    #     value_2 = self.df[col].sort_values().iloc[i + 1]
    #     if n%2 == 0:
    #         print((value_2 - value_1) * 0.75 + value_1, "&")
    #     else:
    #         print(value_2, "*")


        # print(self.df[col].sort_values().iloc[i])
        # print(np.percentile(self.df[col], 75))
        # self.upper_quartile.append(self.df[col].sort_values()[i])

    def describe(self):
        print(self.cols)
        for col in self.cols:
            self.count_mean(col)
            self.count_std(col)
            self.count_min(col)
            self.count_max(col)
            self.count_madian(col)
            # self.count_upper_quartile(col)


        print(self.mean)
        print(self.std)
        print(self.min)
        print(self.max)
        print(self.upper_quartile)





if __name__ == '__main__':
    info = DatasetInfo(pd.read_csv('//home/sigma.sbrf.ru@20132725/Downloads/dataset_train.csv'))
    info.describe()
