from  datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return ("hey, How's it going?")
    
    if user_message in ("who are you","who are you ?","what are you?","what are you"):
        return ("I am Your helper bot")

    if user_message in ("how can you help me?","help me then",):
        return ("I am a bot in developmenent by Param and Kuldeep to help people in the fields of Development,Education and Medical")

    if user_message in ("can you find the best institutions for me","institutions for me?"):
        return ('''top institutions that i reccommend are :
        1> Chandigarh University
        2> VIT Vellore
        3> Amity University''')
    
    if user_message in ("Is chandigarh university good?","is chandigarh university good", "chandigarh university good ?"):
        return ("The teachers and courses at chandigarh university are some of the best the country has to offer.")

    if user_message in ("thank you","ty"):
        return ("Anytime, i am always hear to help")

    if user_message in ("what do you know about development"):
        return ('''A developer - also known as a programmer, coder or software 
        engineer - is an IT professional who uses programming languages to create 
        computer software. for more information visit zdnet.com ''' )

    if user_message in ("is software developing a good career?"):
        return ("software development is one of the most demanding and well paying jobs in the market")

    if user_message in ("how can i become a good developer"):
        return ('''focus on one or two languages rather than all, do real life application projects, 
        participate in hackathons. following these steps will definately help you in becoming a good developer one day, Good Luck!''')

    if user_message in ("whats a good coding school"):
        return ("chandigarh university offers one the the best computer science courses in the country")

    if user_message in ("i dont think i am feeling very well"):
        return ("what are your symptoms")
    
    if user_message in ("time", 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str (date_time)
    else:
        return ("I don't understand you.")