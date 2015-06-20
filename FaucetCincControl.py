#
#
#
#
#
# Determine OS
# Small GUI
#   - Start
#   - Stop
#   - Restart Logstash Only
#   - Service Status
#
#
#
import sys
from Tkinter import *


class Application(Frame):
    
    def startAll(self):
        pass
    
    def stopAll(self):
        pass
    
    
    def createButton(self, text, row, column, command):
        pass
    
    def createWidgets(self):
        
        
        #Elasticsearch - Row 0
        self.e_label = Label(self)
        self.e_label["text"] = "ElasticSearch"
        self.e_label["anchor"] = "w"
        self.e_label.grid(row = 0, column = 0, sticky = "w")
        
        self.e_start = Button(self)
        self.e_start["text"] = "Start"
        self.e_start["fg"]   = "green"
        self.e_start.grid(row = 0, column = 1)
        
        self.e_stop = Button(self)
        self.e_stop["text"] = "Stop"
        self.e_stop["fg"] = "red"
        self.e_stop.grid(row = 0, column = 2)
        
        self.e_pid = Label(self)
        self.e_pid["text"] = "pid goes here"
        self.e_pid.grid(row = 0, column = 3)
        
        #Logstash - Row 1
        self.l_label = Label(self)
        self.l_label["text"] = "Logstash"
        self.l_label["anchor"] = "w"
        self.l_label.grid(row = 1, column = 0, sticky = "w")
        
        
        self.l_start = Button(self)
        self.l_start["text"] = "Start"
        self.l_start["bg"]   = "green"
        self.l_start.grid(row = 1, column = 1)
    
        self.l_stop = Button(self)
        self.l_stop["text"] = "Stop"
        self.l_stop["bg"] = 'red'
        self.l_stop.grid(row = 1, column = 2)
        
        self.l_pid = Label(self)
        self.l_pid["text"] = "pid goes here"
        self.l_pid.grid(row = 1, column = 3)
        
        
        #Kibana - Row 2
        self.k_label = Label(self)
        self.k_label["text"] = "Kibana"
        self.k_label["anchor"] = "w"
        self.k_label.grid(row = 2, column = 0, sticky = "w")
        
        self.k_start = Button(self)
        self.k_start["text"] = "Start"
        self.k_start["background"]   = 'green'
        self.k_start.grid(row = 2, column = 1)
        
        self.k_stop = Button(self)
        self.k_stop["text"] = "Stop"
        self.k_stop["background"] = 'red'
        self.k_stop.grid(row = 2, column = 2)
        
        self.k_pid = Label(self)
        self.k_pid["text"] = "pid goes here"
        self.k_pid.grid(row = 2, column = 3)
        
        #All - Row 3
        self.a_label = Label(self)
        self.a_label["text"] = "All"
        self.a_label.grid(row = 3, column = 0, sticky = "w")
        
        self.a_start = Button(self)
        self.a_start["text"] = "Start"
        self.a_start["fg"]   = "green"
        self.a_start.grid(row = 3, column = 1)
        
        self.a_stop = Button(self)
        self.a_stop["text"] = "Stop"
        self.a_stop["fg"] = "red"
        self.a_stop.grid(row = 3, column = 2)
        
        #Drop Box Chooser
        
        self.input_label = Label(self)
        self.input_label["text"] = "Input: "
        self.input_label.grid(row = 4, column = 0, sticky = "w") 
        
        self.input_location = Text(self)
        self.input_location["height"] = 1
        self.input_location["width"] = 50
        self.input_location["bg"] = "white"
        
        self.input_location.grid(row = 4, column = 1, columnspan=2)
        
        self.input_browse = Button(self)
        self.input_browse["text"] = "..."
        self.input_browse.grid(row = 4, column = 3)
        
        
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        
        self.QUIT.grid(column = 3, sticky = SE)
        

        
        
        
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.master.title('Faucet CINC Controller')
    app.mainloop()
    root.destroy()
