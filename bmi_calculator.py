# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 12:24:32 2021

@author: anura
"""
#BMI Calculator application

from pywebio.input import *
from pywebio.output import *

def BMI_CALC():
    height=input("Enter the height in cms",type=FLOAT)  
    weight=input("Enter the weight in kg",type=FLOAT)  
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16,'severely underweight'),(18.5,'underweight'),(25,'normal'),(30,'overweight'),
                (35,'moderately obese'),(float('inf'),'severely obese')]
    
    for t1,t2 in bmi_output:
        if bmi<=t1:
            put_text("your bmi is :%.1f and the person is :%s "%(bmi,t2))
            
            break





if __name__=="__main__":
    BMI_CALC()