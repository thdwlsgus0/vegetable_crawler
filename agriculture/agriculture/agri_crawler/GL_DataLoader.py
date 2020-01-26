"""
 CSV 데이터 로더 모듈
 CSV Data Loader Module
 created by Good_Learning
 date : 2018-08-21

 데이터를 CSV 파일로부터 불러오며, 배열로 변환하고 표준화 및 분리까지 담당한다.
"""
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import os
from . import GL_ModelCreator

class GLDataLoader:
    file_name = "vegetable/static/sung"
    full_path = file_name + '.csv'
    array_data_set = []
    look_back = 1
    for_test_x = []
    for_test_y = []
    for_train_x = []
    for_train_y = []
    test_size = 0
    train_size = 0
    scaler = 0
    date = []
    def __init__(self, x_axis, y_axis, way = 1):
        data_set = pd.read_csv(self.full_path, index_col=x_axis)
        array_data = data_set[y_axis].values[::way]
        array_data.astype('float32')
        data_set2 =pd.read_csv(self.full_path )
        self.date = data_set2[x_axis]
        self.array_data_set = np.reshape(array_data, [-1, 1])

        # 데이터 셋을 배열로 변환하는 함수
    def convert_data_to_array(self, dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset) - look_back - 1):
            a = dataset[i:(i + look_back)]
            dataX.append(a)
            dataY.append(dataset[i + look_back])
        return np.array(dataX), np.array(dataY)

    # 표준화하는 함수, 표준화란 데이터의 범위를 0과 1에 맞추는 것을 말함.
    def normalizing(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        nptf = self.scaler.fit_transform(self.array_data_set)
        return nptf

    def spliter(self, nptf):
        train_size = int(len(nptf) * 0.9)
        test_size = len(nptf) - train_size

        train, test = nptf[0:train_size], nptf[train_size:len(nptf)]
        train_x, train_y = self.convert_data_to_array(train, look_back=15)
        test_x, test_y = self.convert_data_to_array(test,look_back=15)

        train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
        test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

        self.test_size = test_size
        self.train_size = train_size

        self.for_test_x = test_x
        self.for_test_y = test_y
        self.for_train_x = train_x
        self.for_train_y = train_y


