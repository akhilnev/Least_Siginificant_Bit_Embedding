# author - AKHILESH SAKET NEVATIA
# LSB +- EMBEDDING CODE
# Modified LSB embedding into hidden projects
import numpy #module helping us store 2d arrays and perform neccesary functions among them

def reusable(I,i):
    store = (numpy.random.randint(2))
    if(store==1):
        I[i]+=1
    else:
        I[i]-=1
        
def embed(X,msg,key):
    cover = X
    #cover is the 2d ARRAY of an image ( numpy form)
    #ATTACH THIS IN THE BELOW PART
    # PUT KEY IN THE MAIN
    (I,Sh) = im2sig(cover, key , msg) # We get I , Sh from this 
    return (I.reshape(Sh))

def extract(Embedded ,key ,length):
    #add length to message 
    #message is giving the wrong extracted order as embedded is different from cover and we dont have access to cover and the permute function will not return the same permutation for the given values
        I = Embedded.flatten()
        L = len(I)
        index = 0
        I_ind = []
        for i in range(L):
            I_ind.append(index)
            index+=1
        if key != None:
            numpy.random.seed(key)
            makerandomarr = (numpy.random.permutation(I_ind)[:length]) 
            # Search for the extraction part more 
            # See how to
            return (I[makerandomarr]%2)
        else:
            return (I[:length])%2

def im2sig(cover,key,msg):
    #Sh returned is the shape of the image used while converting back
    #I is the flattened list or single line array made from the 2d array
    Sh = cover.shape# Stores the cover shape useful while converting back from a single list 
    I = cover.flatten()
    L = len(msg)#stores the length of message to be embedded in the image
    index = 0
    I_ind = []
    #constant time operation
    for i in range(len(I)):
        I_ind.append(index)
        index+=1
    #makes index subarray of the same length as I 
    print(I_ind)
    if key != None:
        numpy.random.seed(key)
        randomarr = (numpy.random.permutation(I_ind)[:len(message)])
        print(randomarr)
        #randomarr = numpy.random.choice(np.arange(0,I.size), replace=False, size=(L))
        #print(randomarr)
        #CHECK HOW TO ADD KEY TO THE CHOICE FUNCTION AND CHECK FOR METHODS
        #1 KEY
        #2 USE PERMUAT/SCRAMBLE ON COVER ARRAY / GREY VALUE USING KEY
        #3 TAKE MESSAGE IN SAME ORDER
        #4 EMBED THEM INTO THE COVER STANDARD WAY 
        #5 UNSCRAMBLE THE COVER USING THE KEY / INVERSE
        for i in range(L):#we iterate through the length of the message here 
            #as key is there we use our randomarr generator to go through the bits 
            #use XOR function for this part maybe
            if((I[randomarr[i]]%2==0 and message[i]%2!=0) or ((I[randomarr[i]%2]!=0) and message[i]%2==0)):
                reusable(I,randomarr[i])
        return (I,Sh)
    else:#WHEN NO KEY
        #very similar to the top code more direct
        for i in range(L):
            if((I[i]%2==0 and message[i]%2!=0) or ((I[i]%2!=0) and message[i]%2==0)) :
                reusable(I,i)#code removed from here into resuable part
        return (I,Sh)          
# MAIN PROGRAM - AKHILESH NEVATIA OCTOBER 4TH 2022
# WRITE A UML DIAGRAM FOR THE CODE ON PAPER AFTER PUTTING KEY INTO MAIN PROGRAMME - DONE 
# CHANGE REUABLE CODE PART - CHANGED AND ADDED RESUABLE FUNCTION  
# make the message size the length of the array and then run to see how many times it enters while loop - made a varibale and called to see how many times it enters loop
# count number of times it takes to go through the while loop -  #can generate the numbers without reusing but am not able to include seed in the fucntion anyhow
#adding new code here
# TO DO _____
#TRY ENTERING THE KEY VALUE IN THE MAIN PART INSTEAD -DONE  
#CHANGE THE KEY PART FOR EFFICIENCY USING NEW SHUFFLE METHOD - DONE

CoverImage = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]#toy example 
CoverImage = numpy.array(CoverImage)
message = numpy.array([1,1,1,1,0,1])
ans = int(input("type 1 if you want a key else type 0: "))
if(ans==1):
    key = int(input("Please enter seed value as key: "))
else:
    key=None;
(Embedded) = (embed(CoverImage,message,key))
print("The Cover Image is: ")
print(CoverImage)
print("The Embedded image is: ")
print(Embedded)
print("The extracted message is the following:")
print(extract(Embedded,key,len(message)))
#SCALING UP THE SIZE OF THE IMAGE NEXT
