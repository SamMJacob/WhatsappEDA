from collections import Counter
from tkinter import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from whatstk import WhatsAppChat
from whatstk import FigureBuilder
from plotly.offline import plot
import pandas as pd
import root
import ui

filepath = root.filepth()
chat = WhatsAppChat.from_source(filepath=filepath) #returns a parsed object containing pandas dataframe from file locaion.. obj.df will refer to the corresponding datadrame
init_date = chat.df.date.min() #whatstk fucntion that returns the date of the first message in the text
end_date = chat.df.date.max()
print(f"First date is: {init_date}\nLast date is: {end_date}")

usernames = chat.users #property of the whatstk object that returns list of user names
print(chat.df)
# Number of messages sent
message_counts = chat.df.groupby('username').agg(num_messages=('message', 'count')) #here num_mrssages is a name given to the column you create wiht the goupby.agg 'message is the column ur aggregating and count is the fucntion
print(message_counts)
def no_of_mssgs():
# Words to exclude from the top 10
    exclude_words = ['in','am','-','omitted>','<Media','and', 'a', 'you', 'I', 'to','the', 'i','I','pm','am','and','is',"I'm"]  # Add the words you want to exclude from the top 10
    for i in usernames:
        for x in i.split():
            exclude_words.append(x)
            exclude_words.append(x+':')
            print(x)
    entrywin = Tk()
    entrywin.geometry('1000x600+120+50')
    entrywin.title('entry')
    entrywin.configure(bg="#3D3D3D")
    new=[]
    def confirm():
        exclude_words.append(usernameEntry.get())
        new.append(usernameEntry.get())
        delwordslabel = Label(entrywin, bg="#3D3D3D", fg="#FFFFFF", text=str(new), #label that displays the words the user added to exclude
                              font=("Times New Roman", 15))
        delwordslabel.place(relx=0.4, rely=0.6, anchor=CENTER)
        usernameEntry.delete(0, END)
    def exi():
        entrywin.destroy()

    usernameLabel1 = Label(entrywin, bg="#3D3D3D", fg="#FFFFFF", text="Enter word to be exluded",
                           font=("Times New Roman", 30))
    usernameLabel1.place(relx=0.3, rely=0.4, anchor=CENTER)
    username = StringVar()
    usernameEntry = Entry(entrywin, textvariable=username, font=("Times New Roman", 20), width=15)
    usernameEntry.place(relx=0.7, rely=0.4, anchor=CENTER)
    enterButton = Button(entrywin, bg="#1ADC5B", text='ENTER', font=("Times New Roman", 20), command=confirm)
    enterButton.place(relx=0.8, rely=0.4, anchor=CENTER)
    exitButton = Button(entrywin, bg="#1ADC5B", text='Plot', font=("Times New Roman", 20), command=exi)
    exitButton.place(relx=0.8, rely=0.8, anchor=CENTER)
    entrywin.attributes('-topmost', True)
    entrywin.mainloop()


# Top 10 most used words (excluding specific words)
    all_messages = ' '.join(chat.df['message'].dropna().astype(str))  # dropna removes null rows
    l=all_messages.split()
    for i in range(len(l)):#strips words of trailing .'s
        while l[i].endswith('.'):
            l[i] = l[i][:-1]

    words_counter = Counter(l)  #returns a counter object which contains a dictionary with words and freq print it if you wnat to see what it looks like

# Remove excluded words
    for word in exclude_words:
        del words_counter[word]
#Remove dates (this is due to a bug i found in and this is the only fix i can think of
    for word in list(words_counter):
        if len(word)>=8:
            if word[2]=='/' or word[5]=='/':
                del words_counter[word]


    top_10_words = dict(words_counter.most_common(10)) #most_common is a collections function that returns values with highest freq
    print("Top 10 most used words :", top_10_words)

    # Plotting WordCloud for the top 10 words
    #plotwindow = Tk()
    #plotwindow.geometry('1000x600+120+50')

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_10_words) #generate from frequencies is a wordcloud library that accepts a dictionary input containing words and correspodning frequencies
    fig = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')  # biliniear makes the image less pixelated.. its an interpolation type like anti-aliasing
    plt.axis('off')  # removes the axis from the normal pyplot window
    plt.title('Top 10 Most Used Words ')
    plt.show()
    #canvas = FigureCanvasTkAgg(fig, master=plotwindow)
    #canvas.draw()
    #canvas.get_tk_widget().pack()
    #toolbar = NavigationToolbar2Tk(canvas, plotwindow)
    #toolbar.update()
    #canvas.get_tk_widget().pack()
    #plotwindow.attributes('-topmost', True)

fb = FigureBuilder(chat=chat)


def user_inter():
    # Additional code for user interventions count

    fig = fb.user_interventions_count_linechart(cumulative=True, title='User Text Count (cumulative)')
    plot(fig)


def no_char():
    # Number of characters sent
    fig1 = fb.user_interventions_count_linechart(cumulative=True, msg_length=True, title='Count OF characters (cumulative)')
    plot(fig1)

    fig = fb.user_msg_length_boxplot()
    plot(fig)


def distroftext():
    labels = message_counts.index
    sizes = message_counts['num_messages']
    colors = plt.cm.Paired(range(len(labels)))  # You can choose a different color map if needed

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Distribution of Texts Sent by Each Person')
    plt.show()


# Extracting day of the week, month, and hour information
chat.df['day_of_week'] = chat.df['date'].dt.day_name()
chat.df['month'] = chat.df['date'].dt.month_name()


def plotgr_dow():
    # Bar chart for messages sent on different days of the week
    plt.figure(figsize=(12, 5))
    custom_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    custom_day_cat = pd.Categorical(chat.df['day_of_week'], categories=custom_day_order, ordered=True) #returns a category type value that has a list of the days of the week and a list containing the order(categories) ordered attribute makes it so that monday<tuesday<so on...
    day_of_week_counts = custom_day_cat.value_counts().sort_index() #value_counts returns a series containing counts of unique values
    day_of_week_counts.plot(kind='bar', color='red')
    plt.title('Messages Sent on Different Days of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Messages')
    plt.show()



# Extract month from the timestamp
chat.df['month'] = chat.df['date'].dt.month_name()

# Create a Categorical data type with custom order
custom_month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][::-1]
custom_month_cat = pd.Categorical(chat.df['month'], categories=custom_month_order, ordered=True)

# Calculate the total number of messages sent in each month

def plotgr_month():
    # Create a bar graph
    month_counts = custom_month_cat.value_counts().sort_index(ascending=False)
    plt.figure(figsize=(10, 6))
    month_counts.plot(kind='bar', color='pink')
    plt.title('Total Messages Sent in Each Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Messages')
    plt.show()


# Calculate the time difference between consecutive messages for each participant
chat.df['time_diff'] = chat.df.groupby('username')['date'].diff()

# Extract the response time in seconds
chat.df['response_time_seconds'] = chat.df['time_diff'].dt.total_seconds()

# Calculate the average response time for each participant
average_response_time = chat.df.groupby('username')['response_time_seconds'].mean()

def plotgr_avgresp():
    # Create a bar graph
    plt.figure(figsize=(10, 6))
    average_response_time.sort_values().plot(kind='bar', color='maroon')
    plt.title('Average Response Time for Each Participant')
    plt.xlabel('Participant')
    plt.ylabel('Average Response Time (seconds)')
    plt.xticks(rotation=45, ha='right')
    plt.show()

# Calculate the time difference between consecutive messages for each participant
chat.df['time_diff'] = chat.df.groupby('username')['date'].diff()

# Set a threshold for inactivity (e.g., 1 hour)
inactivity_threshold = pd.Timedelta(hours=7) #This determines how much time gap defines a new conversation.. Yes it is slighty flawed but the definition of a new conversation is vague and will need ML tools to identify one

# Identify conversations started by each participant
chat.df['conversation_started'] = (chat.df['time_diff'] > inactivity_threshold) | chat.df['time_diff'].isnull()

# Count the number of conversations started by each participant
conversations_started_count = chat.df.groupby('username')['conversation_started'].sum()

def conversations_start():
    # Create a bar graph
    plt.figure(figsize=(10, 6))
    conversations_started_count.sort_values().plot(kind='bar', color='orange')
    plt.title('Number of Conversations Started by Each Participant')
    plt.xlabel('Participant')
    plt.ylabel('Number of Conversations Started')
    plt.xticks(rotation=45, ha='right')
    plt.show()

while True:
    funcopt = ui.ret()
    if funcopt == 1:
        no_of_mssgs()

    elif funcopt == 2:
        plotgr_dow()
    elif funcopt == 3:
        plotgr_month()
    elif funcopt == 4:
        plotgr_avgresp()
    elif funcopt == 5:
        conversations_start()
    elif funcopt == 6:
        user_inter()
    elif funcopt == 7:
        no_char()
    elif funcopt ==8:
        distroftext()
    elif funcopt == -2:
        break