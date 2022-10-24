
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_decrypt(start_text):
  end_text = ""
  for shift_amount in range(27):
    shift_amount *= -1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char
    end_text += '\n'
  print(f"Here are the results:\n\n{end_text}\n")



keep_running = True
while keep_running:

  text = input("Type your message to decrypt:\n").lower()  
 

  caesar_decrypt(start_text=text)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    keep_running = False
    print("Goodbye")