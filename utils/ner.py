import jieba
import re
import json
import csv
import pkuseg
import time
import os
from tqdm import tqdm
class ner():
    def __init__(self):
        self.train_file_path = "../data/coreEntityEmotion_train.txt"
        self.get_stopwords()
        self.pku = pkuseg.pkuseg()
        
    def get_stopwords(self):
        stopwordfile = open("./data/stopwords.txt")
        self.stopwords = set()
        for stp in stopwordfile:
            self.stopwords.add(stp)
        
    def is_json(self, news):
        try:
            json.loads(news)
            return True
        except:
            return False
    
    def pkuseg_cut(self, news):
        title = news['title']
        content = news['content']
        nerdict = set()
        
        sentences = []
        for seq in re.split(r'[\n。，、：‘’“""”？！?!《》]', title+" "+content):
            seq = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",seq)
            if len(seq) > 2:
                sentences.append(seq)
        for seq in sentences:
            ner_list = self.pku.cut(seq)
            for ner in ner_list:
                if len(ner) > 1:
                    if ner not in self.stopwords:  #去停用词
                        nerdict.add(ner)
        return nerdict #set
    
        