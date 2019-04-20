from utils.ner import ner
import jieba
import jieba.analyse
from joblib import dump,load
from tqdm import tqdm
import time
import json
import re
import numpy as np

class feature_ents():
    def __init__(self):
        self.ner_dict_path = "../models/nerDict.txt"
        self.train_file_path = "./data/coreEntityEmotion_train.txt"
        self.ner = ner()
        self.jieba = jieba
        
    def set_ners(self, news):
        self.ners = set(self.ner.pkuseg_cut(news))
        
    def get_ners(self):
        return self.ners
   
    # tfidf分数
    def get_tfidf_Score(self, news):
        title = news['title']
        content = news['content']
        article = title+ ' '+content
        tfidf = {}
        for ner, score in self.jieba.analyse.extract_tags(content, topK=50, withWeight=True):
            tfidf[ner] = score
        return tfidf
    
    
    # 把特征接到一起
    def combine_features(self, news):
        self.set_ners(news)
        tfidf = self.get_tfidf_Score(news)
        
        features = []
        for ner in self.ners:
            a = 0
            if ner in tfidf: #0
                a = tfidf[ner] 
            features.append([[ner],[a]])  #特征可以继续添加 b,c,d,e,f,g......
        return features
    
  
