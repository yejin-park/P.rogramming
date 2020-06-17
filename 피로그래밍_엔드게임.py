import random

class Character:
    def __init__(self, name, attack, defense, energy):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.energy = energy


    def character_info(self):
        print("이름 : ", self.name, "\n공격력 : ",self.attack, "\n방어력 :  ", self.defense , "\n체력 : ", self.energy)


    
    def _attack(n):
        if n == "1":
            _attack = IronMan.attack 

        if n == "2":
            _attack = CaptainAmerica.attack

        if n == "3":
            _attack = Thor.attack

        if n == "4":
            _attack = Thanos.attack

        return _attack


    def _defense(m):
        if m == "1":
            _defense = IronMan.defense

        if m == "2":
            _defense = CaptainAmerica.defense

        if m == "3":
            _defense = Thor.defense

        if m == "4":
            _defense = Thanos.defense

        return _defense



    def _energy(l):
        if l == "1":
            _energy = IronMan.energy

        if l == "2":
            _energy = CaptainAmerica.energy

        if l == "3":
            _energy = Thor.energy

        if l == "4":
            _energy = Thanos.energy

        return _energy
    
    


IronMan = Character("IronMan","70","50","100")
CaptainAmerica = Character("CaptainAmerica","60", "50", "100")
Thor = Character("Thor","90", "20", "100")
Thanos = Character("Thanos","100", "50", "300")

    
#######################################################################

def gAME(num, cnt):

    
    if num == "1":
        IronMan.character_info()
       
    
    if num == "2":
        CaptainAmerica.character_info()
        
    
    if num == "3":
        Thor.character_info()


    print("--적 캐릭터--")

    numlist = [1, 2, 3]   

    del numlist[int(num) - 1]
    
    #추가조건 1 :: 내 캐릭터 != 적 캐릭터 
    ran_num = str(random.choice(numlist))
    
    global ran_temp         #전역변수 : 값이 유지되어야하므로 
    
    if cnt ==1:
        ran_temp = ran_num

       
    if cnt == 2:
        
        while ran_temp == ran_num:
            ran_num = str(random.choice(numlist))

    
    
    if cnt == 3:
        Thanos.character_info()
        print("--배틀--\n\n")
        
    else:
        
        if ran_num == "1":
            IronMan.character_info()
    
        if ran_num == "2":
            CaptainAmerica.character_info()
    
        if ran_num == "3":
            Thor.character_info()
        print("--배틀--\n\n")

    

    my_energy = int(Character._energy(num))
    ene_energy = int(Character._energy(ran_num))
    

    while my_energy > 0 and ene_energy > 0:
        ene_energy = ene_energy - (int(Character._attack(num)) - int(Character._defense(ran_num)))
        my_energy = my_energy - (int(Character._attack(ran_num)) - int(Character._defense(num)))

    
    if my_energy > 0: 
        print("당신이 이겼습니다!\n")

        #추가조건 2
        if cnt == 1:
            if num == "1":
                IronMan.defense = 60
                IronMan.energy = 100
    
            if num == "2":
                CaptainAmerica.defense = 60
                CaptainAmerica.energy = 100
    
            if num == "3":
                Thor.defense = 30
                Thor.energy = 100
            


        if cnt == 2:
            if num == "1":

                IronMan.attack = 80
                IronMan.defense = 70
                IronMan.energy = 300
    
            if num == "2":
                
                CaptainAmerica.attack = 70
                CaptainAmerica.defense = 60
                CaptainAmerica.energy = 300
    
            if num == "3":
                
                Thor.attack = 100
                Thor.defense = 30
                Thor.energy = 300
                
        return "1"

    else:
        print("당신이 졌습니다!")
        return "0"


    _attack = _defense = _final = 0






#################### 출력 ###########################


print("1. IronMan 2. CaptainAmerica 3. Thor")
print("당신의 캐릭터 번호를 선택해주세요 (1, 2, 3) : ",end="")
global num
num = input()



print("\n***첫 번째 스테이지***")
print("--내 캐릭터--")
cnt = 1
n = gAME(num, cnt)


#####################################################

if n == "0":
    pass
else:
    print("\n***두번째 스테이지***")
    print("--내 캐릭터--")
    cnt = 2
    n = gAME(num, cnt)



#####################################################
    
if n == "0":
   pass
else:
    print("\n***세 번째 스테이지***")
    print("--내 캐릭터--")
    cnt = 3
    gAME(num, cnt)


      
    
        
