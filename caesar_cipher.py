alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ievadam mainīgos t,o, kuri ir funkcija e kura šifro tekstu, kura atbild par text, rotation
def encrypted(text, rotation):
  result = ""
  #komanda for lieto mainīgos c un t
  for character in text:
    #ja neatrdd burtu c, tad tas ir -1
    if (alfabet.find(character) == -1):
      result += character
      #ja atrad, tad pievieno rotāciju o un ievada to algoritmā
    else:
      result += (alfabet[(alfabet.find(character) + rotation) % len(alfabet)])
  return result
#ievadam mainīgos t,o, kuri ir funkcija d kura atšifro tekstu, kura atbild par text, rotation
def decrypt(text, rotation):
  result = ""
  #komanda for lieto mainīgos c un t
  for character in text:
    #ja neatrad burtu c, tad pārveido to par -1
    if (alfabet.find(character) == -1):
      result += character
      #ja atrad, tad atņem burtu o un ievada to algorit
    else:
      result += (alfabet[(alfabet.find(character) - rotation) % len(alfabet)])
  return result

word = """
1. Encrypt text

2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(word))
#izvēlamiea apstrādes modu 1
if mode == 1:
  #ievadam tekstu, kurš tiks apstrādāts
  text = input("Enter the text: ")
  #ievadam rotāciju
  rotation = int(input("Enter the rotation: "))
  #izvadam tekstu uz ekrāna
  print("Encrypted: " + encrypted(text, rotation))
  #izvēlamiea apstrādes modu 2
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypt(text, rotation))
  #izvēlamiea apstrādes modu 3
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
  #ZHOFRPH WR JUDYLWB IDOOV
