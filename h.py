import hashlib
import os
im = """
                            ....please inter Option...
    [1]  Crack singel hash
    [2]  Crack multi hash on file
    [3]  A text to hash
    [4]  Multi text to hash on file
    [5]  Online crack
    [6]  Combo crack
    [7]  DEV INFO
    [9]  Exit...

                                     :"""
mode = input(im)
while mode != "9":
    if mode == '1':
        hash = input("Enter hash : ")
        typ = input('''   ENTER YOUR HASH TYPE
        SHA1, SHA224, SHA256, SHA384, SHA512 , FIPS , MD5
                    ''')
        f = input('WordList : ')
        n = 0
        for line in open(f,encoding='UTF-8'):

            #print(line)
            check = getattr(hashlib, typ)((line[:-1]).encode()).hexdigest()
            n = n + 1
            if n == 100000:
                n = 0
                print('Prosseing.....')
            if check == hash:
                print('Hash cracked your hash %s pass : % s' % (hash, line))
                break
            else:
                print('\t error not crack \n\n')
    if mode == "2":
        f = input('Wordlist file : ')
        typ = input('''   ENTER YOUR HASH TYPE
        HA1, SHA224, SHA256, SHA384, SHA512 , FIPS , MD5
                    ''')
        hashfile = input("Hash file neme : ")
        fo = open('cracked.txt' , 'w')
        n = 0
        ckn = 0
        for ll in open(hashfile):
            n = n + 1
            for line in open(f):
                check = getattr(hashlib, typ)((line[:-1]).encode()).hexdigest()
                #print(check,n)
                #print (ll)
                if check == ll[:-1]:
                    ckn =+ 1
                    print(line[:-1] ,"|", ll)
                    fo.write(line)
                    fo.flush()
                    break
        print('all hash %i | cracked hash : %i' % (n,ckn))
        fo.close()
    if mode == '3':
        tin = input('Pleas incert your text : ')
        typ = input('''   ENTER YOUR HASH TYPE
        HA1, SHA224, SHA256, SHA384, SHA512 , FIPS , MD5
                    ''')
        print('\n\n\n\n')
        print('Your hash  :',getattr(hashlib,typ)((tin).encode()).hexdigest())
        print('\n\n\n\n')
    if mode == '4':
        f = input('Pleas inter your file neme :')
        fi = open(f,'r',encoding='UTF-8',errors='ignore')
        if '.txt' in f:
            print('OK')
        else:
            f = f + '.txt'
        typ = input('''   ENTER YOUR HASH TYPE
        HA1, SHA224, SHA256, SHA384, SHA512 , FIPS , MD5
                    ''')
        hvat = typ.upper()+'-'+f
        fou = open(hvat, 'w')
        n = 0
        for line in fi:
            fou.write(getattr(hashlib, typ)((line.strip()).encode()).hexdigest()+'\n')
            n += 1
        fou.close()
        print('\n\n\n\n\n\n')
        print('\t finish %i item hashing | %s |' % (n,typ.upper()))
        print('\n\n\n')
    if mode == "5":
        print('OK')
    if mode == "6":
        mod2 = int(input('''    pleas insert mode 
                [1] Crack multiple files
                [2] Crack Singel File
                                        : '''))
        f = 'f.txt' #input('Pleas Inter Your file : ')
        typ = 'md5' #input('''   ENTER YOUR HASH TYPE
        #HA1, SHA224, SHA256, SHA384, SHA512 , FIPS , MD5
        #            ''')
        spc = ':' #input("Pleas Inter Split chrakter : ': ; , / and ....'  : ")
        pw = 'r.txt' #input('Ples inter WordList : ')
        of = open(f+'Cracked.txt', 'w')
        n = 0
        er = 0
        if mod2 == 1:
            dic = dict()
            for s2d in open(pw):
                crate = (getattr(hashlib, typ)((s2d[:-1]).encode()).hexdigest())
                dic[crate] = s2d
            for line in open(f):
                n += 1
                if spc in line:
                    lspc = line.split(spc)[1].strip()
                    user = line.split(spc)[0].strip()
                    if lspc in dic.keys():
                        print("YAFTAAAM : . . ....",lspc ,' | ',dic[lspc])
                        of.write(user+spc+dic[lspc])
                    else:
                        print('not find' ,lspc)
        if mod2 == 2:
            for line in open(f):
                n += 1
                try:
                    h = line.split(spc)[1].strip()
                    for l in open(pw):
                        cr = (getattr(hashlib, typ)((l.strip()).encode()).hexdigest())
                        #print(cr)
                        if h == cr:
                            print(h ,'\t', l.strip())
                            break
                except IndexError:
                    er += 1
        of.close()
    mode = input(im)
print(' CLOSEED PROGRRAM ')
