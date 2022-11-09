import pandas as pd

def addPaperYear():
    #load working_papers.csv file from PART 1
    df = pd.read_csv('working_papers.csv') 
    #read all the publication date to list
    date = df['publication_date'].tolist()
    #create new list with year only
    date_year = []
    for item in date:
        date_year.append(item[0:4])
    #add the new column to dataframe
    df['paperYear'] = date_year
    #generate new csv file
    df.to_csv("working_papersUpdated.csv", index=False, sep=',')
    
def addFirstLastname():
    #load working_papers.csv file from PART 1
    df = pd.read_csv('authors.csv')
    #read all the full name to list
    fullname = df['authorName'].tolist()
    #create two new lists for first name and surname, middle name is ignored
    firstname = []
    surname = []
    for item in fullname:
       temp = item.split(" ")
       firstname.append(temp[0])
       surname.append(temp[-1])
    #add the new columns to dataframe
    df['firstname'] = firstname
    df['surname'] = surname
    #generate new csv file
    df.to_csv("authorsUpdated.csv", index=False, sep=',')

if __name__ == '__main__':
    print(pd.read_csv('authors.csv'))
    #addPaperYear()
    #addFirstLastname()
       