import pandas as pd
import numpy as np
import math


class DatasetInfo:
    def __init__(self, df):
        self.df = df
        self.cols = df.dtypes[df.dtypes != 'object'].index
        self.count = []
        self.mean = []
        self.std = []
        self.min = []
        self.max = []
        self.quartile_25 = []
        self.quartile_50 = []
        self.quartile_75 = []


    def count_mean(self, col):
        self.mean.append((self.df[col].sum()) / (len(self.df[col][self.df[col].isna() == False])))

    def count_std(self, col):
        sum = 0
        for i in range(self.df.shape[0]):
            if math.isnan(self.df.loc[i][col]) is False:
                sum += (self.df.loc[i][col] - self.mean[-1]) ** 2
        self.std.append((sum / (len(self.df[col][self.df[col].isna() == False]) - 1)) ** 0.5)

    def count_percentile(self, sorted_data, perc, l):
        n = len(sorted_data)
        index = perc * (n - 1)
        if index == math.trunc(index):
          l.append(sorted_data[int(index)])
        else:
          l.append((sorted_data[int(np.floor(index))] * (np.ceil(index) - index)) + (sorted_data[int(np.ceil(index))]) * (index - np.floor(index))) 
          
    def describe(self):
        for col in self.cols:
            sorted_data = sorted([i for i in df[col] if i == i])
            self.count.append(len(sorted_data))
            self.count_mean(col)
            self.count_std(col)
            self.min.append(sorted_data[0])
            self.max.append(sorted_data[-1])
            self.count_percentile(sorted_data, 1/4, self.quartile_25)
            self.count_percentile(sorted_data, 1/2, self.quartile_50)
            self.count_percentile(sorted_data, 3/4, self.quartile_75)

        d = {'count': self.count,'mean': self.mean, 'std': self.std, 'min': self.min, '25%': self.quartile_25, '50%': self.quartile_50, '75%': self.quartile_75, 'max': self.max}
        description = pd.DataFrame(data = d, index=self.cols)
        return description.T


if __name__ == '__main__':
    info = DatasetInfo(pd.read_csv('//home/sigma.sbrf.ru@20132725/Downloads/dataset_train.csv'))
    info.describe()
