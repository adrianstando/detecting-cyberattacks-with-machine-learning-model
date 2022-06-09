import pandas as pd
import numpy as np
import pickle
import os
import copy


class Controller:
    def __init__(self, model_path, column_names_path, class_names_path):
        self.model = None
        self.columns = None
        self.classes = None
        self.last_prediction = None

        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        
        with open(column_names_path, 'rb') as f:
            self.columns = pickle.load(f)
        
        with open(class_names_path, 'rb') as f:
            self.classes = pickle.load(f)
    
    def predict_from_csv(self, path, return_pred = False):
        df = pd.read_csv(path)

        if(self.columns is not None):
            df = df[self.columns]
        
        self.last_prediction = self.model.predict(df)

        if return_pred:
            return self.last_prediction
    
    def predict_from_dataframe(self, df1, return_pred = False):
        df = copy.deepcopy(df1)
        if(self.columns is not None):
            df = df[self.columns]
        
        self.last_prediction = self.model.predict(df)
        
        if return_pred:
            return self.last_prediction

    def predict_from_pcap(self, path, return_pred = False):
        os.system('python3 -m cicflowmeter.src.cicflowmeter.sniffer -f ' + path + ' -c ./flows.csv')
        self.predict_from_csv('./flows.csv', return_pred)
        os.remove('flows.csv')

        if return_pred:
            return self.last_prediction

    def last_pred_summary(self):
        if self.last_prediction is None:
            return ""
        
        out = ""
        for classname in self.classes:
            val = np.count_nonzero(self.last_prediction == classname) / self.last_prediction.size * 100
            out += f"Type of an attack: {classname:20s} Percent of occurences: {val:.1f} % \n"
        
        return out
    
    def is_safe(self, safe_class="Normal", thresh=0.98):
        if self.last_prediction is None:
            return True
        
        if safe_class in self.classes:
            return np.count_nonzero(self.last_prediction == safe_class) / self.last_prediction.size > thresh
        else:
            return True
    
if __name__ == '__main__':
    # zapisanie ruchu sieciowego  sudo tcpdump -i wlp3s0 -w flows.pcap
    
    c = Controller(model_path = './model_files/rf_final.model', column_names_path = './model_files/column_changed.names', class_names_path='./model_files/classes.names')
    #c.predict_from_csv('example.csv')
    #c.predict_from_csv('X.csv')
    c.predict_from_pcap('example.pcap')
    print(c.last_pred_summary())
    print(f"Is computer safe: {c.is_safe()}")
    
    
    
    
    
