from textblob import TextBlob
import pandas as pd
import numpy as np

df = pd.read_excel('Feedback_Feature_List.xlsx')

comment = df['Comment']
date = df['Created_Date'].astype(str)

comment_1 = np.array(comment.loc[0:18000])
date_1 = np.array(date.loc[0:18000])
comment_2 = np.array(comment.loc[18001:36000])
date_2 = np.array(date.loc[18001:36000])
comment_3 = np.array(comment.loc[36001:54000])
date_3 = np.array(date.loc[36001:54000])
comment_4 = np.array(comment.loc[54001:])
date_4 = np.array(date.loc[54001:])

comments = [comment_1, comment_2, comment_3, comment_4]
dates = [date_1, date_2, date_3, date_4]

for j in range(4):
    sentence_positive = []
    date_positive = []
    sentence_negative = []
    date_negative = []
    sentence_neutral = []
    date_neutral = []
    sentence_bad = []
    date_bad = []

    positive = [sentence_positive, date_positive]
    negative = [sentence_negative, date_negative]
    neutral = [sentence_neutral, date_neutral]
    bad = [sentence_bad, date_bad]
    
    for i in range(len(comments[j])):
        sentence = str(comments[j][i]).capitalize()
        datetime = dates[j][i][:10]
        analysis = TextBlob(sentence)
        #try:
        print(i)
        try :
            analysis = analysis.translate(from_lang='id', to='en')
            polarity = analysis.polarity

        except:
            try:
                analysis.translate(from_lang="en", to="id")
                polarity = analysis.polarity

            except:
                polarity = 2

        if 0 < polarity <= 1:
            positive[0].append(sentence)
            positive[1].append(datetime)
        elif polarity < 0:
            negative[0].append(sentence)
            negative[1].append(datetime)
        elif polarity == 0:
            neutral[0].append(sentence)
            neutral[1].append(datetime)
        else:   
            bad[0].append(sentence)
            bad[1].append(datetime)
    
    pos = pd.DataFrame({"Date":positive[1],"Positive":positive[0]})
    neg = pd.DataFrame({"Date":negative[1],"Negative":negative[0]})
    neut = pd.DataFrame({"Date":neutral[1],"Neutral":neutral[0]})
    badd = pd.DataFrame({"Date":bad[1],"Bad":bad[0]})
    
    pos.to_excel("Positive_Sentiment_"+str(j)+".xlsx")
    neg.to_excel("Negative_Sentiment_"+str(j)+".xlsx")
    neut.to_excel("Neutral_Sentiment_"+str(j)+".xlsx")
    badd.to_excel("Bad_Sentence_"+str(j)+".xlsx")