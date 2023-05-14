def decode_morse(code):
  morse_code = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
  }

  morse_frase = ""
  morse_words = code.split("  ")

  for morse_word in morse_words:
    morse_letters = morse_word.split()
    for morse_letter in morse_letters:
      if morse_letter in morse_code:
        morse_frase += morse_code[morse_letter]
      elif morse_letter.endswith("*"):
        all_letters = morse_letter.replace("*", "")
        occurances = []
        for code, morse_letter in morse_code.items():
          if code.startswith(all_letters):
            occurances.append(morse_letter)
        occurances.sort()
        morse_frase += "[" + "".join(occurances) + "]"
    morse_frase += " "

  return morse_frase.strip()


code1 = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morse_frase1 = decode_morse(code1)
print(morse_frase1)

code2 = "-.-. .- -.. .-*  -- .- -.-. .- -.-. ---  -. ---  ... . ..-  --. .- .-.. .... ---"
morse_frase2 = decode_morse(code2)
print(morse_frase2)  # Saída esperada: "CAD[AJLPRW] MACACO NO SEU GALHO"

code3 = "-.-. .- ...* .-  -.. .  ..-. . .-. .-. . .. .-.* ---  . ... .--. . - ---  -.. .*  .--. .- ..-"
morse_frase3 = decode_morse(code3)
print(
  morse_frase3
)  # Saída esperada: "CA[HSV]A DE FERREI[LR]O ESPETO D[AEFHIJLPRSUVW] PAU"
