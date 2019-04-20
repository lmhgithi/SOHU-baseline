# SOHU-baseline
# 搜狐算法大赛（实体抽取+情感预测）的baseline~

* 没有用深度模型，用的传统的lgb当成分类做的，这里的代码只用了一个非常基本的tfidf特征，模型搭建好了，大家可以自己按照自己的想法构建特征。

* 想先做实体的部分，就没做情感，可以加一个文件features/emo_features.py继续做，因为情正面感比例较大，可以直接全预测为POS。

* 跑代码前先把训练集和测试集放到/data文件夹里

* 文件说明
  - 先跑1.main_train_lmh.ipynb 再跑  1.main_test_lmh.ipynb
  - models文件里是放训练好的lgb（也可以别的）模型的
  - features里是放计算好的特征的
  - results
  
  如果想用传统（当做分类）的方法做，可以基于我的代码继续写下去，祝好运！心情好就点个star啦~
