from Tkinter import *
import tkFileDialog
from PIL import Image,ImageTk
import numpy as np
import sys
import MySQLdb
import tkMessageBox
import nltk
import time


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Welcome_To_Sentiment_Analysis (root)
    root.mainloop()




class Welcome_To_Sentiment_Analysis:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 11 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.db = MySQLdb.connect("localhost", "root", "", "sentiment_analysis")

        top.geometry("1176x559")
        top.title("Welcome To Sentiment Analysis using DecisionTree")
        top.configure(background="#d9d9d9")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.16, relheight=0.76, relwidth=0.47)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#E7FF33")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=555)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.02, rely=0.02, height=31, width=127)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Testing:''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.11, rely=0.21, relheight=0.11, relwidth=0.8)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.11, rely=0.13, height=31, width=184)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#f4f4ff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Enter Test for Analysis:''')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.7, rely=0.38, height=52, width=108)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Test 1''')
        self.Button1.configure(command=self.test)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.11, rely=0.59, relheight=0.36, relwidth=0.8)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=444)
        self.Text1.configure(wrap=WORD)

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.03, rely=0.5, height=31, width=144)
        self.Label5.configure(activebackground="#f9f9ff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#f4f4ff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''OutPut:''')

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.5, rely=0.16, relheight=0.76, relwidth=0.47)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#E7FF33")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=555)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.02, rely=0.03, height=31, width=127)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Training:''')

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.07, rely=0.14, height=31, width=184)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#f4f4ff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Enter Training Test:''')

        self.Entry2 = Entry(self.Frame2)
        self.Entry2.place(relx=0.1, rely=0.21, relheight=0.11, relwidth=0.8)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.7, rely=0.56, height=52, width=108)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Submit''')
        self.Button2.configure(command=self.train)

        self.Listbox1 = Listbox(self.Frame2)
        self.Listbox1.place(relx=0.68, rely=0.35, relheight=0.16, relwidth=0.22)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(selectmode=SINGLE)
        self.Listbox1.configure(width=124)
        self.Listbox1.insert(0,"positive")
        self.Listbox1.insert(1,"negative")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.03, rely=0.05, height=31, width=347)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome to Sentiment Analysis using DecisionTree''')

    def train(self):
        cursor=self.db.cursor()
        training=self.Entry2.get()
        type=self.Listbox1.get(ACTIVE)
        sql="insert into training_set(training_data,type,entry_date) values('"+training+"','"+type+"',now())"
        try:
            cursor.execute(sql)
            self.db.commit()
            tkMessageBox.showinfo("Message", "Inserted Successfully.")
            self.Entry2.delete(0,END)
        except:
            self.db.rollback()

    def test(self):
        #self.Text1.delete(END)
        start = time.time()
        pos = []
        neg=[]
        tweets = []
        cursor=self.db.cursor()
        sql = "select * from training_set where type='positive'"
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            pos.append("('"+row[1]+"','"+row[2]+"')")
        sql = "select * from training_set where type='negative'"
        cursor.execute(sql)
        resultsneg = cursor.fetchall()
        for row in resultsneg:
            val="('"+row[1]+"','"+row[2]+"')"
            neg.append(val)


        pos_tweets = [('I love this car', 'positive'),
                      ('This view is amazing', 'positive'),
                      ('I feel great this morning', 'positive'),
                      ('I am so excited about the concert', 'positive'),
                      ('He is my best friend', 'positive'),
                      ('Going well', 'positive'),
                      ('Thank you', 'positive'),
                      ('Hope you are doing well', 'positive'),
                      ('I am very happy', 'positive'),
                      ('Good for you', 'positive'),
                      ('It is all good. I know about it and I accept it.', 'positive'),
                      ('This is really good!', 'positive'),
                      ('Tomorrow is going to be fun.', 'positive'),
                      ('Smiling all around.', 'positive'),
                      ('These are great apples today.', 'positive'),
                      ('How about them apples? Thomas is a happy boy.', 'positive'),
                      ('Thomas is very zen. He is well-mannered.', 'positive')]
        #print(pos_tweets)
        neg_tweets = [('I do not like this car', 'negative'),
                      ('This view is horrible', 'negative'),
                      ('I feel tired this morning', 'negative'),
                      ('I am not looking forward to the concert', 'negative'),
                      ('He is my enemy', 'negative'),
                      ('I am a bad boy', 'negative'),
                      ('This is not good', 'negative'),
                      ('I am bothered by this', 'negative'),
                      ('I am not connected with this', 'negative'),
                      ('Sadistic creep you ass. Die.', 'negative'),
                      ('All sorts of crazy and scary as hell.', 'negative'),
                      ('Not his emails, no.', 'negative'),
                      ('His father is dead. Returned obviously.', 'negative'),
                      ('He has a bomb.', 'negative'),
                      ('Too fast to be on foot. We cannot catch them.', 'negative')]

        for (words, sentiment) in pos_tweets + neg_tweets:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
            tweets.append((words_filtered, sentiment))

        self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))
        self.training_set = nltk.classify.apply_features(self.extract_features, tweets)
        self.classifier = nltk.DecisionTreeClassifier.train(self.training_set)
        #self.classifier = nltk.NaiveBayesClassifier.train(self.training_set)

        runtweets = []  # setup to import a list of tweets here if you wish into a python list
        runtweets.append(self.Entry1.get())  # test tweet incase
        poscount = 0
        negcount = 0
        for tweett in runtweets:
            valued = self.classifier.classify(self.extract_features(tweett.split()))
            print (valued)
            if valued == 'negative':
                negcount = negcount + 1
                print ('Positive count: %s \nNegative count: %s' % (poscount, negcount))
                self.Text1.insert(END,'Positive count: %s \nNegative count: %s\n' % (poscount, negcount))
            else:
                poscount = poscount + 1
                print ('Positive count: %s \nNegative count: %s' % (poscount, negcount))
                self.Text1.insert(END, 'Positive count: %s \nNegative count: %s\n' % (poscount, negcount))
        end = time.time()
        tkMessageBox.showinfo("Estimate Execution Time(Seconds)", end-start)
        print(end - start)

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


