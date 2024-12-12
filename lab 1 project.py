from GUI import *

def main():
    window = Tk()
    window.title("Ballot")
    window.geometry("400x400")
    window.resizable(False , False)
    GUI(window)
    window.mainloop()

if __name__  ==  '__main__':
    main()