import matplotlib.pyplot as plt
from . import GL_ModelCreator as gmc
from . import GL_DataLoader as gdl
import numpy as np
import csv

class Analysis:
    def __init__(self, x_axis, y_axis):
        data_loader = gdl.GLDataLoader(x_axis, y_axis)
        nptf =data_loader.normalizing()

        data_loader.spliter(nptf)
        scaler = data_loader.scaler
        model = gmc.ModelsCreator()
        model.settingLearningEnvironment()
        last_x = nptf[-1]
        last_x = np.reshape(last_x, (1, 1, 1))

        hist = model.training(data_loader.for_train_x, data_loader.for_train_y, data_loader.for_test_x, data_loader.for_test_y)
        test_predict, test_y = model.tester(data_loader.for_test_x, data_loader.for_test_y, nptf, scaler)


        plt.plot(test_predict, "g-")
        plt.plot(test_y, "r-")
        plt.show()
        plt.close()
        fig, loss_ax = plt.subplots()
        acc_ax = loss_ax.twinx()
        loss_ax.plot(hist.history['loss'], 'y', label='train loss')
        loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
        loss_ax.set_xlabel('epoch')
        loss_ax.set_ylabel('loss')
        loss_ax.legend(loc='upper left')
        plt.show()
        extest=np.array([1.6,1.2,1.2,1.3,1.2,1,0.4,-0.1,0.6,1.5,2.3,3,4.4,4.3,3.6])
        look_back = 15
        day=30
        log=[]
        for step in range(day): 
            extest2 = np.reshape(extest, [-1, 1])
            extest2 = scaler.fit_transform(extest2)
            extest2 = extest2.reshape([1, 1, look_back])
            temp=scaler.inverse_transform(model.model.predict(extest2))
            print("day",step+1,":",temp)
            log.append(temp[0][0])
        for i in range(len(extest)-1):
            extest[i]=extest[i+1] 
            extest[look_back-1]=temp
        plt.plot(log)
        plt.show()
        
        f = open('output.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(['Date , late'])
        np.reshape(test_predict, [-1])
        print(np.shape(test_predict))
        for i in range(test_predict.size):
            wr.writerow([data_loader.date[i], test_predict[i, 0]])
        f.close()
