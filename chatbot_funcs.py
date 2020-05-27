def print_message():
  print("I'm sorry, I did not undersatnd your selection. Please enter the corresponding letter fo your response.") 


def get_size():
    res = input("what size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res == "a":
        return "Small"
    elif res == "b":
        return "Medium"
    elif res == "c":
        return "Large"
    else:
      print_message()
      get_size() 

def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    if res == "a":
        return "2% milk latte"
    elif res == "b":
        return "Non-fat milk latte"
    elif res == "c":
        return "Soy milk latte"
    else:
        print_message()
        order_latte()