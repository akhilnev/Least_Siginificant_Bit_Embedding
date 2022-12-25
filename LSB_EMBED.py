#CODE FOR LSB EMBEDDING - STEGANOGRAPHY
#AKHILESH SAKET NEVATIA - RESEARCH 
import numpy #module helping us store 2d arrays and perform neccesary functions among them
def embed(X,msg):
    cover = X
    #cover is the 2d ARRAY of an image ( numpy form)
    ans = int(input("type 1 if you want a key else type 0"))
    if(ans==1):
        key = int(input("Please enter seed value as key"))
    else:
        key=None;
    (I,Sh) = im2sig(cover, key , msg) # We get I , Sh from this 
    return (I.reshape(Sh),key)
def extract(Embedded , key ,length):
        I = Embedded.flatten()
        if key != None:
            makerandomarr=[]
            numpy.random.seed(key)
            while(len(makerandomarr)<length):
                num = (numpy.random.randint(I.size))
                if(num in makerandomarr):
                    continue
                else:
                    makerandomarr.append(num)
            return (I[makerandomarr]%2)
        else:
            return (I[:length])%2
def im2sig(cover,key,msg):
    #Sh returned is the shape of the image used while converting back
    #I is the flattened list or single line array made from the 2d array
    Sh = cover.shape# Stores the cover shape useful while converting back from a single list 
    I = cover.flatten()
    L = len(msg)#stores the length of message to be embedded in the image 
    if key != None:
        randomarr=[]
        numpy.random.seed(key)
        while(len(randomarr)<L):
            num = (numpy.random.randint(I.size))
            if(num in randomarr):
                    continue
            else:
                randomarr.append(num)
        print(randomarr)
        
        I[randomarr]=( I[randomarr]-I[randomarr]%2)
        I[randomarr]=I[randomarr]+msg
        return (I,Sh)
    else:
        I[:L] = I[:L]-(I[:L]%2)# taking a mod 2 for the length of the image in the single array gives us the least significant bit and that is removed 
        I[:L] += msg#Once the least significant bit is removed from the image we add the message in the place of the removed LSB 
        return (I,Sh)
    
# WE ARE MAKING A RANDOM 2D ARRAY OF AN IMAGE AND TRYING TO EMBED A MESSAGE IN THE MAIN
CoverImage = [[1,2,3,3],[2,3,4,5],[3,4,5,1],[1,7,8,2]]
CoverImage = numpy.array(CoverImage)
message = numpy.array([1,0,0])
(Embedded,key) = (embed(CoverImage,message))
print("The Cover Image is: ")
print(CoverImage)
print("The Embedded image is: ")
print(Embedded)
print("The extracted message is the following:")
print(extract(Embedded,key,len(message)))
