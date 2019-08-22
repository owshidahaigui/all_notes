def  print_msg():
    msg = "I'm closurs" # 自由变量
    def printer():
        print(msg)
    return printer

closurs = print_msg()

closurs()
