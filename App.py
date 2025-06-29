def welcome (* , name) :
    print(f"Hello {name} Is The Best Ever")

#? Error The Down Code
#! welcome("Alireza") 

welcome(name="Alireza")

#* multiple caracters

def mixed (x , / , y ,* , z) :
    print(x , y , z)
    
mixed(15 , "s" , z="Alireza")

#! Error
# mixed(x=15 , y="s" , z="js")

#! Error
# mixed(16 , y="alr" , "js")

mixed(16 , "alir" , z="za")