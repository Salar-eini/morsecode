
def english_to_morse(x):
  dict_morse = {
    'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','.': '.-.-.-',',': '--..--','?': '..--..',"'": '.----.','!': '-.-.--','/': '-..-.','(': '-.--.',')': '-.--.-','&': '.-...',':': '---...',';': '-.-.-.','=': '-...-','+': '.-.-.','-': '-....-','_': '..--.-','"': '.-..-.','$': '...-..-','@': '.--.-.',' ': '/'
    }
  morse_code = ''
  for a in x:

    if a.upper() in dict_morse:
      morse_code += dict_morse[a.upper()] + ' '

    else:
        print("Please write a text in English. There is an unknown character in your text. Your text should include A-Z,0-9 and . , ? ' ! / ( ) & : ; = + - _ $ @ ")
    continue
  print(morse_code)
def morse_to_eng(x):
    dict_eng = morse_code_dict = {
    '.-': 'A','-...': 'B','-.-.': 'C','-..': 'D','.': 'E','..-.': 'F','--.': 'G','....': 'H','..': 'I','.---': 'J','-.-': 'K','.-..': 'L','--': 'M','-.': 'N','---': 'O','.--.': 'P','--.-': 'Q','.-.': 'R','...': 'S','-': 'T','..-': 'U','...-': 'V','.--': 'W','-..-': 'X','-.--': 'Y','--..': 'Z','-----': '0','.----': '1','..---': '2','...--': '3','....-': '4','.....': '5','-....': '6','--...': '7','---..': '8','----.': '9','.-.-.-': '.','--..--': ',','..--..': '?','.----.': "'",'-.-.--': '!','-..-.': '/','-.--.': '(','-.--.-': ')','.-...': '&','---...': ':','-.-.-.': ';','-...-': '=','.-.-.': '+','-....-': '-','..--.-': '_','.-..-.': '"','...-..-': '$','.--.-.': '@','/': ' '
    }
    english_text = ''
    for a in x.split():
        if a in dict_eng:
            english_text += dict_eng[a]
        else:
            print("Please write a text in Morse Code, There was an unknown character in your text.")
        continue
    print(english_text)


while True:
    req = input('To translate your text from English to Morse Code, please enter 1, and to translate from Morse Code to English enter 2:')
    if req == '1':
        txt = input('Please write your text in English:')
        english_to_morse(txt)
    elif req == '2':
        txt = input('Please write your text in Morse Code:')
        morse_to_eng(txt)
    else:
        print('Please enter a value between 1 and 2.')
        continue
