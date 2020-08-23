import sys
from Tkinter import *
import ttk
import MySQLdb
import tkMessageBox
import nltk
import time
import matplotlib.pyplot as plt

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)

    root.mainloop()


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"


        top.geometry("1384x785+174+87")
        top.title("Movie Reviews Analysis")
        top.configure(background="#808080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.db = MySQLdb.connect("localhost", "root", "", "movie_review")
        self.top = top
        self.labels = 'Negative', 'Positive'

        self.colors = ['red', 'yellowgreen']
        self.explode = (0.1, 0)  # explode 1st slice

        self.Label1 = Label(top)
        self.Label1.place(relx=0.34, rely=0.05, height=31, width=407)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#808080")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ANALYSIS ON REVIEWS''')

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.16, rely=0.2, relheight=0.61
                , relwidth=0.68)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief=FLAT)
        self.Labelframe1.configure(text='''ANALYSIS''')
        self.Labelframe1.configure(background="#c0c0c0")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=940)

        self.Entry1 = Entry(self.Labelframe1)
        self.Entry1.place(relx=0.29, rely=0.19, relheight=0.12, relwidth=0.11)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.09, rely=0.21, height=34, width=162)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#c0c0c0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ENTER MOVIE ID''')

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.67, rely=0.32, height=34, width=162)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#c0c0c0")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''RESULT''')

        self.Entry2 = Entry(self.Labelframe1)
        self.Entry2.place(relx=0.57, rely=0.46, relheight=0.35, relwidth=0.4)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.1, rely=0.44, height=62, width=158)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''PROCESS''')
        self.Button1.configure(command=self.process)

        self.Listbox1 = Listbox(self.Labelframe1)
        self.Listbox1.place(relx=0.30, rely=0.43, relheight=0.16, relwidth=0.22)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(selectmode=SINGLE)
        self.Listbox1.configure(width=124)
        self.Listbox1.insert(0, "Movie")
        self.Listbox1.insert(1, "Actor")


    def process(self):
        # self.Text1.delete(END)
        start = time.time()
        pos = []
        neg = []
        tweets = []
        cursor = self.db.cursor()
        sql = "select * from training_set where type='positive'"
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            pos.append((row[1], row[2]))

        sql = "select * from training_set where type='negative'"
        cursor.execute(sql)
        resultsneg = cursor.fetchall()
        for row in resultsneg:
            neg.append((row[1], row[2]))
        print neg

        for (words, sentiment) in pos + neg:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
            tweets.append((words_filtered, sentiment))

        self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))
        self.training_set = nltk.classify.apply_features(self.extract_features, tweets)
        self.classifier = nltk.NaiveBayesClassifier.train(self.training_set)
        runtweets = []  # setup to import a list of tweets here if you wish into a python list
        type = self.Listbox1.get(ACTIVE)
        id = self.Entry1.get()
        if type=="Movie":
            sql = "select * from rating_tb where movie_or_actor='m' and data_id='"+id +"'"
        else:
            sql = "select * from rating_tb where movie_or_actor='a' and data_id='"+id +"'"

        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            runtweets.append(row[5])
        poscount = 0
        negcount = 0
        sentensepos = 0
        sentenseneg = 0
        countno = 0
        for tweett in runtweets:
            sentensepos = 0
            sentenseneg = 0
            sentenses = tweett.split(".")
            if len(sentenses) > 1:
                for sen in sentenses:
                    print sen
                    valued = self.classifier.classify(self.extract_features(sen.split()))
                    print (valued)
                    if valued == 'negative':
                        sentenseneg = sentenseneg + 1
                    else:
                        sentensepos = sentensepos + 1

                if sentenseneg > sentensepos:
                    negcount = negcount + 1
                elif sentensepos > sentenseneg:
                    poscount = poscount + 1

            else:
                valued = self.classifier.classify(self.extract_features(tweett.split()))
                print (valued)
                if valued == 'negative':
                    negcount = negcount + 1
                    print ('Positive count: %s \nNegative count: %s' % (poscount, negcount))
                    self.Entry2.insert(END, 'Positive count: %s \nNegative count: %s\n' % (poscount, negcount))
                else:
                    poscount = poscount + 1
                    print ('Positive count: %s \nNegative count: %s' % (poscount, negcount))
                    self.Entry2.insert(END, 'Positive count: %s \nNegative count: %s\n' % (poscount, negcount))
        end = time.time()
        tkMessageBox.showinfo("Estimate Execution Time(Seconds)", end - start)
        print(end - start)
        self.sizes = [negcount, poscount]
        # Plot
        plt.pie(self.sizes, explode=self.explode, labels=self.labels, colors=self.colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()


    def get_words_in_tweets(self,tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_word_features(self,wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features

    def extract_features(self,document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features




if __name__ == '__main__':
    vp_start_gui()


