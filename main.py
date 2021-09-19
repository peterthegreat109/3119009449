import numpy as np
import jieba

# 余弦法求相似度
def cos_distance(sentence1: str, sentence2: str) -> float:
    seg1 = [word for word in jieba.cut(sentence1)]
    seg2 = [word for word in jieba.cut(sentence2)]
    word_list = list(set([word for word in seg1 + seg2]))  # 建立词库
    get_word_vector_1 = []
    get_word_vector_2 = []
    for word in word_list:
        get_word_vector_1.append(seg1.count(word))  # 文本1统计在词典里出现词的次数
        get_word_vector_2.append(seg2.count(word))  # 文本2统计在词典里出现词的次数
    vec_1 = np.array(get_word_vector_1)
    vec_2 = np.array(get_word_vector_2)
    # 余弦公式
    try:
        num = vec_1.dot(vec_2.T)
        denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
        cos = num / denom
        sim = 0.5 + 0.5 * cos
        return sim
    except ZeroDivisionError:
        print("NULL")
        return 0

if __name__ == '__main__':
        """  
        path1 = input("第一篇文章地址:")
        path2 = input("第二篇文章地址:")
        """
        path1 = "D:/test/orig.txt"  # 论文原文的文件的绝对路径（作业要求）
        path2 = "D:/test/orig_0.8_dis_10.txt"  # 抄袭版论文的文件的绝对路径
        save_path = "D:/test/result.txt"  #输出结果绝对路径
        try:
            f1 = open(path1, 'r', encoding='UTF-8')
            f2 = open(path2, 'r', encoding='UTF-8')
            str1 = f1.read()
            str2 = f2.read()
            result = cos_distance(str1, str2)
            print("相似度 ：%.4f" % result)
            f = open(save_path,'w',encoding='utf-8')
            f.write("文章相似度：%.4f"%result)
            f.close()

        except FileNotFoundError:
            print("error")
