# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:49:13 2021

@author: Sude
"""
#it can take few minutes to finish the whole execution
def Word_Order_Frequency_One_Book(Book,Word_Order,File_Output):
    
    #first the program checks the word order, if it is not 1 or 2 the program prints an error message.
    if Word_Order!=1 and Word_Order!=2:
        output_1= print("Error: Word_order must be 1 or 2.")
        return(output_1)
    #then program reads the file, if there is no such file it prints an error message.
    try:
        infile=open('book_1.txt','r',encoding='utf8')
        content=infile.read()
        content=content.lower()
        #if the char in the text is not alphabetic program removes it
        for char in content:
            if char.isalpha()==False and char.isspace()==False:
                content=content.replace(char,"")
        #program converts the text to list by using split
        list_of_content=content.split() # this list is the one program removes the stop words
        for_loop=content.split() # this list is the one program checks in for loop
        infile.close()
    except FileNotFoundError:
        output_1=print("Error: There is no such file or directory.")
        return(output_1)
    
  
    list_of_content_stops=['able', 'about', 'above', 'abroad', 'according', 'accordingly', 
                           'across', 'actually', 'adj', 'after', 'afterwards',
                           'again', 'against', 'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 
                           'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although',
                           'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 
                           'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway',
                           'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 
                           'are', 'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 
                           'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 
                           'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming',
                           'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe',
                           'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 
                           'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant', 
                           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly',
                           'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning', 'consequently',
                           'consider', 'considering', 'contain', 'containing', 'contains',
                           'corresponding', 'could', 'couldnt', 'course', 'cs', 'currently',
                           'dare', 'darent', 'definitely', 'described', 'despite', 'did', 'didnt',
                           'different', 'directly', 'do', 'does', 'doesnt', 'doing', 'done', 'dont',
                           'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 
                           'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 
                           'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody',
                           'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except',
                           'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five',
                           'followed', 'following', 'follows', 'for', 'forever', 'former', 
                           'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 
                           'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes',
                           'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 
                           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 
                           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi',
                           'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 
                           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im', 'immediate',
                           'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate', 'indicated',
                           'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward',
                           'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its', 'itself', 'ive', 'just',
                           'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately',
                           'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 
                           'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 
                           'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many',
                           'may', 'maybe', 'maynt', 'me', 'mean', 'meantime', 'meanwhile', 'merely',
                           'might', 'mightnt', 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 
                           'mostly', 'mr', 'mrs', 'much', 'must', 'mustnt', 'my', 'myself', 'name',
                           'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 
                           'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 
                           'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 
                           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel',
                           'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay',
                           'old', 'on', 'once', 'one', 'ones', 'ones', 'only', 'onto', 'opposite',
                           'or', 'other', 'others', 'otherwise', 'ought', 'oughtnt', 'our', 'ours',
                           'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular',
                           'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 
                           'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 
                           'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent',
                           'recently', 'regarding', 'regardless', 'regards', 'relatively', 
                           'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying',
                           'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming',
                           'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 
                           'seriously', 'seven', 'several', 'shall', 'shant', 'she', 'shed',
                           'shell', 'shes', 'should', 'shouldnt', 'since', 'six', 'so', 'some',
                           'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime',
                           'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified',
                           'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take',
                           'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks',
                           'thanx', 'that', 'thatll', 'thats', 'thats', 'thatve', 'the', 'their',
                           'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 
                           'thereby', 'thered', 'therefore', 'therein', 'therell', 'therere',
                           'theres', 'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd',
                           'theyll', 'theyre', 'theyve', 'thing', 'things', 'think', 'third',
                           'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing',
                           'wish', 'with', 'within', 'without', 'wonder', 'wont', 'would',
                           'wouldnt', 'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre',
                           'yours', 'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows',
                           'i', 'whens', 'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l',
                           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 
                           'z', 'i', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con',
                           'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven',
                           'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty',
                           'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 
                           'itse', 'mill', 'move', 'myse', 'part', 'put', 'show', 'side',
                           'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top',
                           'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted',
                           'affected', 'affecting', 'affects', 'ah', 'announce', 
                           'anymore', 'apparently', 'approximately', 'aren', 'arent',
                           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 
                           'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im',
                           'immediately', 'importance', 'important', 'index', 'information', 
                           'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line',
                           'll', 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 
                           'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page',
                           'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly',
                           'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly',
                           'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 
                           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                           'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state',
                           'states', 'stop', 'strongly', 'substantially', 'successfully',
                           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                           'world', 'youd', 'youre']
    
    
    
    # this for loop removes the stop words from the text
    for item in for_loop:
        if item in list_of_content_stops:
            list_of_content.remove(item)
    # here program creates an empty dictionary first, then adds the words in the text to that dictionary
    # if the word is already in the dictionary the program increases it's value by 1 everytime.
    if Word_Order==1:
        allWords={}
        for word in list_of_content:
            if word not in allWords:
                allWords[word] = 1
            else:
                allWords[word] += 1
    # if word order is two, program does the same thing as it's one but this time it checks the word and
    # the one comes after together.
    elif Word_Order==2:
        list_of_word_groups=[]
        for i in range(len(list_of_content)-1):
            for j in range(i+1,i+2):
                new_item=list_of_content[i]+" "+list_of_content[j]
                list_of_word_groups.append(new_item)
    # and program adds the word groups to an empty dictionary and counts.
        allWords={}
        for word in list_of_word_groups:
            if word not in allWords:
                allWords[word] = 1
            else:
                allWords[word] += 1
    # here program sorts the dictionary by it's values in a descending order.And writes the output in a file.
    lst=sorted(allWords.items(),reverse=True, key=lambda x: x[1])
    header="frequency sequence"
    output=('\n'.join(map(lambda x: str(x[1]) + '         ' + str(x[0]), lst)))                                                
    outfile=open('result_1.txt','w',encoding='utf-8')
    outfile.write(header+"\n"+output)
    outfile.close()

def Word_Order_Frequency_Two_Books(Book_1,Book_2,Word_Order,File_Output):
    # first the program checks the word order, if it is not 1 or 2 the program prints an error message.
    if Word_Order!=1 and Word_Order!=2:
        output_1= print("Error: Word_order must be 1 or 2.")
        return(output_1)
    # then program reads the file, if there is no such file it prints an error message.
    try:
        infile=open('book_1.txt','r',-1,'utf-8')
        content=infile.read()
        content=content.lower()
        # if the char in the text is not alphabetic program removes it
        for char in content:
           if char.isalpha()==False and char.isspace()==False:
              content=content.replace(char,"")
        # program converts the text to list by using split
        list_of_content_1=content.split() # this list is the one program removes the stop words
        for_loop=content.split() # this list is the one program checks in for loop
        infile.close()
    except FileNotFoundError:
        output_1=print("Error: There is no such file or directory.")
        return(output_1)
    
    try:
        infile_2=open('book_2.txt','r',-1,'utf-8')
        content_2=infile_2.read()
        content_2=content_2.lower()
        for char in content_2:
            if char.isalpha()==False and char.isspace()==False:
                content_2=content_2.replace(char,"")
        list_of_content_2=content_2.split()
        for_loop_2=content_2.split()
        infile_2.close()
    except FileNotFoundError:
        output_1=print("Error: There is no such file or directory.")
        return(output_1)       

    list_of_content_stops=['able', 'about', 'above', 'abroad', 'according', 'accordingly', 
                           'across', 'actually', 'adj', 'after', 'afterwards',
                           'again', 'against', 'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 
                           'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although',
                           'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 
                           'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway',
                           'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 
                           'are', 'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 
                           'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 
                           'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming',
                           'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe',
                           'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 
                           'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant', 
                           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly',
                           'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning', 'consequently',
                           'consider', 'considering', 'contain', 'containing', 'contains',
                           'corresponding', 'could', 'couldnt', 'course', 'cs', 'currently',
                           'dare', 'darent', 'definitely', 'described', 'despite', 'did', 'didnt',
                           'different', 'directly', 'do', 'does', 'doesnt', 'doing', 'done', 'dont',
                           'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 
                           'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 
                           'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody',
                           'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except',
                           'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five',
                           'followed', 'following', 'follows', 'for', 'forever', 'former', 
                           'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 
                           'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes',
                           'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 
                           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 
                           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi',
                           'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 
                           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im', 'immediate',
                           'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate', 'indicated',
                           'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward',
                           'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its', 'itself', 'ive', 'just',
                           'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately',
                           'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 
                           'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 
                           'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many',
                           'may', 'maybe', 'maynt', 'me', 'mean', 'meantime', 'meanwhile', 'merely',
                           'might', 'mightnt', 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 
                           'mostly', 'mr', 'mrs', 'much', 'must', 'mustnt', 'my', 'myself', 'name',
                           'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 
                           'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 
                           'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 
                           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel',
                           'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay',
                           'old', 'on', 'once', 'one', 'ones', 'ones', 'only', 'onto', 'opposite',
                           'or', 'other', 'others', 'otherwise', 'ought', 'oughtnt', 'our', 'ours',
                           'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular',
                           'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 
                           'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 
                           'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent',
                           'recently', 'regarding', 'regardless', 'regards', 'relatively', 
                           'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying',
                           'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming',
                           'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 
                           'seriously', 'seven', 'several', 'shall', 'shant', 'she', 'shed',
                           'shell', 'shes', 'should', 'shouldnt', 'since', 'six', 'so', 'some',
                           'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime',
                           'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified',
                           'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take',
                           'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks',
                           'thanx', 'that', 'thatll', 'thats', 'thats', 'thatve', 'the', 'their',
                           'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 
                           'thereby', 'thered', 'therefore', 'therein', 'therell', 'therere',
                           'theres', 'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd',
                           'theyll', 'theyre', 'theyve', 'thing', 'things', 'think', 'third',
                           'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing',
                           'wish', 'with', 'within', 'without', 'wonder', 'wont', 'would',
                           'wouldnt', 'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre',
                           'yours', 'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows',
                           'i', 'whens', 'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l',
                           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 
                           'z', 'i', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con',
                           'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven',
                           'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty',
                           'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 
                           'itse', 'mill', 'move', 'myse', 'part', 'put', 'show', 'side',
                           'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top',
                           'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted',
                           'affected', 'affecting', 'affects', 'ah', 'announce', 
                           'anymore', 'apparently', 'approximately', 'aren', 'arent',
                           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 
                           'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im',
                           'immediately', 'importance', 'important', 'index', 'information', 
                           'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line',
                           'll', 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 
                           'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page',
                           'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly',
                           'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly',
                           'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 
                           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                           'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state',
                           'states', 'stop', 'strongly', 'substantially', 'successfully',
                           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                           'world', 'youd', 'youre']
    # this for loop removes the stop words from the text
    for item in for_loop:
        if item in list_of_content_stops:
            list_of_content_1.remove(item)
    # this for loop removes the stop words from the text
    for item in for_loop_2:
        if item in list_of_content_stops:
            list_of_content_2.remove(item)
    # this is the list that contains both words of text 1 and text 2
    total_words=list_of_content_1+list_of_content_2
    # here program creates an empty dictionary first, then adds the words in the text to that dictionary
    # if the word is already in the dictionary the program increases it's value by 1 everytime. 
    if Word_Order==1:
        allWords_1={}  #this is for text 1
        for word in list_of_content_1:
            if word not in allWords_1:
                allWords_1[word] = 1
            else:
                allWords_1[word] += 1    
        allWords_2={}  # this is for text 2
        for word in list_of_content_2:
           if word not in allWords_2:
               allWords_2[word] = 1
           else:
               allWords_2[word] += 1
        

    # if word order is two, program does the same thing as it's one but this time it checks the word and
    # the one comes after together.  
    elif Word_Order==2:
        list_of_word_groups_1=[] #this is for text 1
        for i in range(len(list_of_content_1)-1):
            for j in range(i+1,i+2):
                new_item=list_of_content_1[i]+" "+list_of_content_1[j]
                list_of_word_groups_1.append(new_item)
        list_of_word_groups_2=[] #this is for text 2
        for i in range(len(list_of_content_2)-1):
            for j in range(i+1,i+2):
                new_item=list_of_content_2[i]+" "+list_of_content_2[j]
                list_of_word_groups_2.append(new_item)  
            

        allWords_1={}
        for word in list_of_word_groups_1:
            if word not in allWords_1:
                allWords_1[word] = 1
            else:
                allWords_1[word] += 1
        allWords_2={}
        for word in list_of_word_groups_2:
            if word not in allWords_2:
                allWords_2[word] = 1
            else:
                allWords_2[word] += 1


    outfile=open('result_2.txt','w',encoding='utf-8')
    outfile.write("")
    #now program finds the common words in two dictionaries and takes the sum of their values.
    allWords_4={}
    for key in allWords_1:
        if key in allWords_2:
            allWords_4[key] = allWords_2[key] + allWords_1[key]
        else:
            pass
    allWords_5={}
    for key in allWords_4:
        allWords_5[key]= allWords_4[key],allWords_2[key], allWords_1[key]
    # here program sorts the dictionary by it's values in a descending order.And writes the output in a file.
    lst=sorted(allWords_5.items(),reverse=True, key=lambda x: x[1])
    header="total book2  book1      word"
    output_1=('\n'.join(map(lambda x: str(x[1]) + '         ' + str(x[0]), lst)))  
    outfile.write(header+"\n"+output_1)
    outfile.close()
    

