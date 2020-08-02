from os.path import isfile
import argparse



class Vigenere:#{
    S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(self):#{
        parser = argparse.ArgumentParser()
        parser.add_argument("-filename", help="your text file goes here.")
        parser.add_argument("-action", help="what you like to do? encypt/decrypt.")
        args = parser.parse_args()

        if args.filename==None:#{
            self.fileName = self.sf("Enter text File Name: ")
        #}
        else:#{
            self.fileName = args.filename
        #}
        if args.action==None:#{
            self.action = self.sf("Enter your choice [E/D]: ")
        #}
        else:#{
            self.action = args.action
        #}
        self.action = self.action.lower()
        try:#{
            self.readFile()
        #}
        except:#{
            self.pf('Error in openning file.')
            quit()
        #}
        self.pf(self.fileName + ":" + self.action.lower())
    #}
    def pf(self, s):#{
        print(s)
    #}
    def sf(self, s):#{
        return input(s)
    #}
    def readFile(self):#{
        with open(self.fileName, 'r') as fob:#{
            self.data = fob.read()
            self.data = self.data.upper()
            fob.close()
        #}
    #}
    def writeFile(self, data):#{
        filename = 'output000.txt'
        i = 1
        while isfile(filename):#{
            filename=filename[:-7]+'%3i.txt'%i
            filename=filename.replace(' ', '0')
            i = i + 1
        #}
        with open(filename, 'w') as fob:#{
            fob.write(data)
            fob.close()
        #}
    #}
    def run(self):#{
        if self.action=='e':#{
            self.encrypt()
        #}
        elif self.action=='d':#{
            self.decrypt()
        #}
        else:#{
            self.pf('Invalid action command type e for encrypt or d for decrypt.')
            quit()
        #}
    #}
    def encrypt(self):#{
        self.K = self.sf("Enter Key string to Encrypt: ")
        self.K = self.K.upper()
        i = 0
        l = len(self.K)
        self.pf(self.K+':'+str(l))
        E = ''
        for m in self.data:#{
            if m in self.S:#{
                c = (self.S.index(m) + self.S.index(self.K[i%l])) % 26
                E = E + self.S[c]
                i = i + 1
            #}
            else:#{
                E = E + m
            #}
            #self.pf(m+":"+E)
        #}
        self.pf(E)
        self.writeFile(E)
        return 'Encrypting Successful.'
    #}
    def decrypt(self):#{
        self.K = self.sf("Enter Key string to Decrypt: ")
        self.K = self.K.upper()
        i = 0
        l = len(self.K)
        self.pf(self.K+':'+str(l))
        D = ''
        for c in self.data:#{
            if c in self.S:#{
                m = (self.S.index(c) - self.S.index(self.K[i%l]) + 26) % 26
                D = D + self.S[m]
                i = i + 1
            #}
            else:#{
                D = D + c
            #}
            #self.pf(c+":"+D)
        #}
        self.pf(D)
        self.writeFile(D)
        return 'Decrypting Successful.'
    #}
#}

V = Vigenere()
print(V.run())