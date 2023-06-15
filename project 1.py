# pyhton quiz game TEKA GENRE LAGU
print("MUSIC GENRE GUESSING GAME")
print("****************************")
print("guess the genre song for each song below")
soalan=("*Golden Hour***\n",
        "**You Really Got Me**\n",
        "**Rapper's Delight**\n"
        "**Stay**\n\n",)

def pilih():
        print("A. pop music ")
        print ("B. rock ")
        print ("C.hip hop  ")
        print ("D. rap ")
        print ("E. latin ")

        
jawapan =("A","B","C","D","E")
teka=[]
score=0
bil_soalan=0

for soalan in soalan:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(soalan)
        pilih() # function menu pilihan jawapan
        
        guess=input("Sila pilih (A,B,C,D,E): ").upper()
        teka.append(guess)
        if guess == jawapan[bil_soalan]:
            score +=1
            print("Tahniah,jawapan anda tepat!")
        else:
            print("\n Maaf jawapan anda salah,sila coba lagi!")
            print(f"{jawapan[bil_soalan]} ialah jawapan yang tepat")
        bil_soalan +=1


# papar keputusan
print("\n**********************")
print("        RESULT!!!!              ")
print("**********************")

print("CORRECT ANSWER: ", end="")
for answer in jawapan:
    print("/",answer, end="")
print()

print("TEKAAN: ", end="")
for guess in teka:
     print("/",guess, end="")
print()

#kira jumlah markah
markah = (score / bil_soalan )* 100

# papar keputusan markah
print("total question:", bil_soalan)
print("Correct answer:", score)
print("Points Collected: ", round (score,2), "%")
print("**********************")
