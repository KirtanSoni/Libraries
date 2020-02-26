import math

"""Incomplete self made"""

OUTPUT_RANGE = 1   # -1,1

class PID:
    def __init__(self, K1 : float , K2 : float , K3 : float):
        self.kp=K1
        self.ki=K2
        self.kd=K3 
        self.integr = 0.0
        self.lastval=0.0
        self.output =0.0
    def intergrator(self,controlled_var)->float:    
        self.lastval = controlled_var 
        if abs(self.output)>= OUTPUT_RANGE * 0.9:
            return 0.0          # antiwinding mech
        else:
                self.integr += controlled_var*(1/120)
                return self.ki * self.integr
    
    def proportional(self,controlled_var)->float:
        return max(min(self.kp*controlled_var,1),-1)
        
    def derivative(self,controlled_var)->float:
        return  self.kd * (controlled_var-self.lastval)/(1/60)
    
    def contr_Output(self,controlled_var)->float:
        x = self.proportional(controlled_var) - self.derivative(controlled_var) + self.intergrator(controlled_var)
        self.output = x
        return self.output