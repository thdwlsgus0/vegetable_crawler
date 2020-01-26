'''
 모델 생성 모듈
 Model Creating Module
 created by Good_Learning
 date : 2018-08-21

 모델을 생성하는 부분을 맡는다.
 RNN 중 LSTM의 전반적인 계층관계와 구조, 학습과정을 여기서 결정한다.
'''
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Dropout
from keras.callbacks import EarlyStopping
import keras
import math
import numpy as np


class ModelsCreator:
    model = Sequential()
    look_back = 15
    def __init__(self):
        self.model.add(LSTM(32, input_shape=(1, self.look_back), activation='relu'))
        self.model.add(Dense(1, activation='relu'))

    def settingLearningEnvironment(self, loss='mean_squared_error', optimizer='adam'):
        self.model.compile(loss=loss, optimizer=optimizer)

    def training(self, trainX, trainY,valid_x, valid_y):
        early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=2, mode='auto')
        hist = self.model.fit(trainX, trainY, validation_data=(valid_x, valid_y), epochs=10, batch_size=1, shuffle=False, verbose=2, callbacks=[early_stopping])
        return hist


    def tester(self, test_x, test_y, nptf, scaler):
        test_predict = self.model.predict(test_x)
        test_predict = scaler.inverse_transform(test_predict)
        test_y = scaler.inverse_transform(test_y)
        test_score = math.sqrt(mean_squared_error(test_y, test_predict))
        print('Train Score: %.2f RMSE'  % test_score)

        # predict last value (or tomorrow?)
        #last_x = nptf[-1]
        #last_x = np.reshape(last_x, (1, 1, 1))
        #last_y = self.model.predict(last_x)
        #last_y = scaler.inverse_transform(last_y)
        #print('Predict the Close value of final day: %d' % last_y)  # 데이터 입력 마지막 다음날 종가 예측
        return test_predict, test_y

        # 아이템, 왜필요했는지 - 범용 CSV 시계열 데이터 분석기
        #분석할때 데이터 어떻게 썻고 - 시계열 데이터를 사용했다.
        #이런 데이터를 썼는데 이런 애트리뷰트가 제일 많고, 중요하고 그래프를 통해서 보여주면 중요할거같아요
        #분석하기 위해서 어떤 방법을 썼는지 정확도가 어떤지
