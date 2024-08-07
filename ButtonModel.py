class ButtonModel():
    idle=1
    hover=2
    pressIn=3
    pressOut=4
                
    def __init__(self, parent = None) :
        self.state=ButtonModel.idle
    
                    
    def Enter(self,state):
        if self.state==ButtonModel.idle:
            self.state=ButtonModel.hover
        elif self.state==ButtonModel.pressOut:
            self.state=ButtonModel.pressIn
            
    def Leave(self,state):
        if self.state==ButtonModel.hover:
            self.state=ButtonModel.idle
        elif self.state==ButtonModel.pressIn:
            self.state=ButtonModel.pressOut
                    
    def Press(self,state):
        if self.state==ButtonModel.hover:
            self.state=ButtonModel.pressIn
        
    def Release(self,state):
        if self.state==ButtonModel.pressOut:
            self.state=ButtonModel.idle
        elif self.state==ButtonModel.pressIn:
            self.Action()
            self.state=ButtonModel.hover
                    
    def Action(self):
            print("Action")