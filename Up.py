class tools(): # Just Playing and practicing around 
    def __init__(self):
        pass

    def up(self):
        try: 
            self.value=input('Text to convert:  ')
            print(self.value.upper())
        except:
            print('This function just accept letters')

Uptext=tools()

Uptext.up()