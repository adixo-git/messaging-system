import pickle
import os
adm = "BruteForce"
f = open("server.dat","ab")
f.close()
jk=""
bm=""
print("# INSTRUCTIONS")
print("    1. Type 'ctrl+z' to undo your actions, but it might not work on actions that are permanently done like removal of account.")
print("    2. Here 'Username' is treated as 'Unique key' and 'Password' is considered to be 'Private key'.")
print("_"*148)
print()


def Crt():
    srv=[]
    psd=[]
    with open("server.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                srv.append(rec[0])
                psd.append(rec[1])
            except: break
    data=[]
    while True:
        acc = input("Enter Username : ")
        if acc in "                                                                                                                                                                                                 ":
            print("A blank Username isn't allowed")
        elif acc in srv:
            print("Given Username already exists")
        else: break
    while True:
        wrd = input("""Enter Password (Atleast 8 characters) : """)
        if len(wrd)<8:
            print("Password is too small")
        else: break
    date = input("Enter Birthdate (dd/mm/yyyy) : ")
    adr = input("Enter Address : ")
    while True:
        try:
            phn =int(input("Enter Phone number : "))
            if phn in range(1000000000,10000000000):
                break
            else:
                print("Invalid Phone Number")
        except:
            print("Invalid Phone Number")
    while True:
        try:
            hgt = float(input("Enter Height (in feet) : "))
            break
        except:
            print("Please enter a numerical value")
    while True:
        try:
            wgt =float(input("Enter Weight (in kg) : "))
            if wgt>=90.0:
                print("Try to do exercise daily !")
                break
            elif wgt<=40.0:
                print("Try to eat nutrisious food !")
                break
            else:
                break
        except:
            print(" Please enter a numerical value")
    rec=[acc,wrd,date,phn,hgt,wgt,adr]
    data.append(rec)
    with open("server.dat","ab") as f:
        for rec in data:
            pickle.dump(rec,f)
    g = open(f"{acc}.dat","ab")
    g.close()


def Data():
    key = input("Enter Admin No. : ")
    if key == adm:
        heading='''=================================================================================================
Name                            Birthdate                       Ph.No.                 Height             Weight               Address
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        
        gap = " "
        print(f'{"Database":^155s}')
        print(heading)
        with open("server.dat","rb") as f:
            while True:
               try:
                    rec = pickle.load(f)
                    if len(rec[0])<4:
                        a = gap*(25+2*len(rec[0]))
                    else:
                        a = gap*(25-len(rec[0]))
                    res =f"{rec[0]}{a}{rec[2]}{gap*15}{rec[3]}{gap*15}{rec[4]}{gap*20}{rec[5]}{gap*18}{rec[6]}"
                    print(res)
                    print('-'*167)
               except: break
    else: print("Wrong Admin No. ")


def Log():
    f = open("server.dat","rb")
    f.close()
    krt =input("Enter Username : ")
    krd =input("Enter Password : ")
    gk = []
    gt = []
    with open("server.dat","rb") as f:
        while True:
            try:
                cd = pickle.load(f)
                gk.append(cd[0])
                gt.append(cd[1])
                for i in cd:
                    if krt==cd[0] and krd==cd[1]:
                        g = open(f"{krt}.dat","ab")
                        g.close()
            except: break
    flag=0
    if krt in gk and flag==0:
        i=gk.index(krt)
        if krd==gt[i]:
            

            def Add():
                ztf =[]
                with open(f"server.dat","rb") as f:                           
                    while True:
                        try:
                            rc=pickle.load(f)
                            ztf.append(rc[0])
                        except: break                
                srv = []
                with open(f"{krt}.dat","rb") as g:                           
                    while True:
                        try:
                            rc=pickle.load(g)
                            srv.append(rc[0])
                        except: break
                fr = []
                more='y'
                while more in 'yY':
                    while True:
                        ad = input("Enter Username of Friend : ")
                        if ad in ztf:
                            if ad in srv:
                                print("Given Username already exists")
                            elif ad == krt:
                                print("You can't add your self")
                            else: break
                        else:
                            print("Username doesn't exists")
                    with open("server.dat","rb") as f:
                        while True:
                            try:
                                cp = pickle.load(f)
                                for i in cp:
                                    if ad==cp[0]:
                                        rc=cp
                            except: break                       
                    fr.append(rc) 
                    more=input("More data (y/n)? --> ")
                with open(f"{krt}.dat","ab") as g:
                    for rc in fr:
                        pickle.dump(rc,g)


            def FrL():
                heading='''=================================================================================================
Name                            Birthdate                       Ph.No.                 Height             Weight               Address
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

                gap = " "
                print(f'{"Friend List":^155s}')
                print(heading)
                with open(f"{krt}.dat","rb") as g:
                    while True:
                       try:
                            rec = pickle.load(g)
                            if len(rec[0])<4:
                                a = gap*(25+2*len(rec[0]))
                            else:
                                a = gap*(25-len(rec[0]))
                            rs = f"{rec[0]}{a}{rec[2]}{gap*15}{rec[3]}{gap*15}{rec[4]}{gap*20}{rec[5]}{gap*18}{rec[6]}"
                            print(rs)
                            print('-'*167)
                       except: break


            def ReF():
                    ztf =[]
                    with open(f"server.dat","rb") as f:                           
                        while True:
                            try:
                                rc=pickle.load(f)
                                ztf.append(rc[0])
                            except: break
                    srv=[]
                    data=[]
                    with open(f"{krt}.dat","rb") as g:
                        while True:
                            try:
                                rec=pickle.load(g)
                                data.append(rec)
                                srv.append(rec[0])
                            except: break
                    more='y'
                    while more in 'yY':
                        while True:
                            acc =input("Enter Friend's name to remove: ")
                            if acc in ztf:
                                if (acc in srv):
                                    ind=srv.index(acc)
                                    data.pop(ind)
                                    srv.pop(ind)                       
                                    break                       
                                else: print("Friend doesn't exists, please re-enter")
                            else: print("You can't remove a non-existing Account")
                        more=input("More to remove (y/n)? -->")                        
                    with open(f"{krt}.dat","wb") as g:
                        for rec in data:
                            pickle.dump(rec,g)


            def Txt():
                srv = []
                with open(f"{krt}.dat","rb") as g:                           
                    while True:
                        try:
                            rc=pickle.load(g)
                            srv.append(rc[0])
                        except: break
                x =0
                for h in srv:
                    print(f"{x}. {h}")
                    x+=1
                while True:
                    try:
                        chs =int(input(f"Choose friend to text (0-{x-1}) : "))
                        if chs<=x:
                            with open(f"{krt}.dat","rb") as g:                           
                                while True:
                                    try:
                                        rc=pickle.load(g)
                                        r = rc[0]
                                        k = srv[chs]
                                        if r==k:
                                            b = open(f"{krt}to{k}.dat","ab")
                                            z = open(f"{k}to{krt}.dat","ab")
                                            b.close()
                                            z.close()
                                    except: break
                            print("# CHAT BOX")
                            print("*(press enter to leave chat box)*")
                            print("-"*167)
                            with open(f"{krt}to{k}.dat","rb") as b:
                                while True:
                                    try:
                                        zx = pickle.load(b)
                                        print(zx)
                                    except: break
                            while True:
                                a = input("You --> ")
                                if a=="":
                                    break
                                mnt=f"You --> {a}"
                                ext = f"{krt} --> {a}"
                                with open(f"{krt}to{k}.dat","ab") as b:
                                    pickle.dump(mnt,b)
                                with open(f"{k}to{krt}.dat","ab") as z:
                                    pickle.dump(ext,z)
                            print("-"*167)
                            break
                        else:
                            print("Invalid Choice")
                    except:
                        print("Invalid Choice")
                        
            # Log Table
            rh=""
            while True:
                print("1. Add New Friend")
                print("2. Friend List")
                print("3. Remove Friend")
                print("4. Text Friend")
                print("7. Log out")
                rh=input("# Enter Your Choice : ")
                print("-"*167)
                if rh=="1":
                    Add()
                elif rh =="2":
                    FrL()
                elif rh=="3":
                    ReF()
                elif rh=="4":
                    Txt()
                elif rh=="7":
                    flag=1
                    break
                else:
                    print("Invalid Choice")
        else:
            if flag==0:
                print("Invalid Account")
                Log()
    else:
        if flag==0:
            print("Invalid Account")
            Log()


def Del():
    srv=[]
    data=[]
    psv = []
    with open("server.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                data.append(rec)
                srv.append(rec[0])
                psv.append(rec[1])
            except: break
    chk =""
    if ch=="3":
        acc =input("Enter Acount to delete: ")
        wrd = input("Enter Password to delete: ")
        chk = input("Are You Sure (yes/no)? --> ")
    else:
        global jk
        acc = jk
        global bm
        wrd = bm
        chk="yes"
    if chk =="yes":
            if acc in srv:
                i=srv.index(acc)
                if wrd==psv[i]:
                    ind=i
                    data.pop(ind)
                    srv.pop(ind)
                    with open("server.dat","wb") as f:
                        for rec in data:
                            pickle.dump(rec,f)
                    if ch=="3":
                        os.remove(f"{acc}.dat")
                        for i in srv:
                            try:
                                rsd = f"{acc}to{i}.dat"
                                frd = f"{i}to{acc}.dat"
                                os.remove(rsd)
                                os.remove(frd)
                            except: pass
                    with open("server.dat","rb") as f:
                        kc = []
                        while True:
                            try:
                                bv=pickle.load(f)
                                kc.append(bv[0])
                            except: break
                        for kr in kc:
                            srd=[]
                            fr=[]
                            with open(f"{kr}.dat","rb") as g:
                                while True:
                                    try:
                                        rc=pickle.load(g)
                                        fr.append(rc)
                                        srd.append(rc[0])
                                    except: break
                            fg = acc
                            if (fg in srd):
                                ind=srd.index(fg)
                                fr.pop(ind)
                                srd.pop(ind) 
                                                
                            with open(f"{kr}.dat","wb") as g:
                                for rc in fr:
                                    pickle.dump(rc,g)
                else:
                    print("Account doesn't exists, please re-enter")
                    Del()                           
            else:
                print("Account doesn't exists, please re-enter")
                Del()
    else: print("Good Choice. Have a nice day!")


def Mod():
    srv=[]
    data=[]
    psv = []
    with open("server.dat","rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                data.append(rec)
                srv.append(rec[0])
                psv.append(rec[1])
            except: break
    while True:
        acc =input("Enter Acount to Modify : ")
        wrd = input("Enter Password : ")
        if acc in srv:
            i=srv.index(acc)
            if wrd==psv[i]:
                ind=i
                break
            else: print("Account does not exist, please re-enter")
        else: print("Account does not exist, please re-enter")
    dt=[]
    with open("server.dat","rb") as f:
        while True:
            try:
                rk=pickle.load(f)
                if rk[0]==acc and rk[1]==wrd:
                    for j in rk:
                        dt.append(j)
            except: break    
    print("(To update account, enter new data. Or press enter to skip)")
    while True:
        acc1 = input("Enter Username : ")
        if acc1=="":
            acc1=dt[0]
            break
        elif acc1 in srv:
            print("Given Username already exists")
        elif acc1 in "                                                                                                                                                                          ":
            print("A blank Username isn't allowed")
        else:
            data[ind][0]=acc1
            break
    while True:
        wrd1=input("Password : ")  
        if wrd1=="":
            wrd1=dt[1]
            break
        elif len(wrd1)<8:
            print("Password is too small, please re-enter") 
        else:
            data[ind][1]=wrd1
            break
    date=input("Birthdate : ")
    if date=='':
        date=dt[2]
    else:
        data[ind][2]=date
    while True:
        try:
            phn=input("Phone No. : ")
            if phn=="":
                phn=dt[2]
                phn = int(phn)
                break
            elif len(phn)!=10:
                print("Invalid Phone No.")
            else:
                data[ind][3]=int(phn)
                break
        except:
            print("Invalid Phone No.")
    while True:
            try:
                hgt=input("Height :  ")
                if hgt=="":
                    hgt=dt[4]
                    hgt=float(hgt)
                    break
                else:
                    data[ind][4]=float(hgt)
                    break
            except:
                print("Please enter numercal value")
    while True:
        try:
            wgt=input("Weight :  ")
            if wgt=='':
                wgt=dt[5]
                wgt= float(wgt)
                break
            else:
                data[ind][5]=float(wgt)
                break
        except:
            print("Please enter numercal value")            
    adr=input("Address : ")
    if adr=='':
            adr=dt[6]
    else: data[ind][6]=adr
    scv = acc
    mrt =[]    
    with open("server.dat","rb") as f:
        while True:
            try:
                rec = pickle.load(f)
                mrt.append(rec[0])
            except: break
    kct = []
    for j in mrt:
        mr2 = []
        with open(f"{j}.dat","rb") as g:
            while True:
                try:
                    rc=pickle.load(g)
                    mr2.append(rc[0])
                    for k in mr2:
                        if k==scv:
                            kct.append(j)
                except: break
    global jk
    jk = acc
    global bm
    bm = wrd
    Del()
    abc = f"{acc}.dat"
    efg =f"{acc1}.dat"
    os.rename(abc,efg)
    for i in srv:
        try:
            rsd = f"{acc}to{i}.dat"
            frd = f"{acc1}to{i}.dat"
            rs2 =f"{i}to{acc}.dat"
            fr2 = f"{i}to{acc1}.dat"
            os.rename(rsd,frd)
            os.rename(rs2,fr2)
        except:
            pass
    with open("server.dat","ab") as f:    
        for rec in data:
            if rec[0]==acc1:
                pickle.dump(rec,f)
    for m in kct:
        with open(f"{m}.dat","ab") as g:
            for rec in data:
                if rec[0]==acc1:
                    pickle.dump(rec,g) 

# Menu Table
ch=""
while True:
    print("1. Create New Account")
    print("2. Show Database")
    print("3. Delete Account")
    print("4. Log In")
    print("5. Modify Account")
    print("7. Exit")
    ch=input("# Enter Your Choice : ")
    print("-"*167)
    if ch=="1":
        Crt()
    elif ch=="2":
        Data()
    elif ch =="3":
        Del()
    elif ch =="4":
        Log()
    elif ch=="5":
        Mod()
    elif ch=="7":
        break
    else:
        print("Invalid Choice")
        

