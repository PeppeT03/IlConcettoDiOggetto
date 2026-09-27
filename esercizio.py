#Esercizio 1

class Studente:
    def __init__(self,nome,corso):
        self.nome= nome
        self.corso=corso
    def presentati(self):
            print(f"Il mio nome e : {self.nome} , e il mio corso di studi e : {self.corso} ")

Studente1=Studente("Marco","Gap")
Studente1.presentati()

Studente2=Studente("PincoPallino","Gay")
Studente2.presentati()

#Esercizio 2

class Persona():
     def __init__(self,nome):
          self.__nome=nome

     def get_nome(self):
        return self.__nome

     def set_nome(self,nuovo_nome):
          if nuovo_nome!="":
               self.__nome=nuovo_nome
          else:
               print("Errore: il nome non puo essere vuoto!")

     def presentati(self):
        print(f"Il mio nome e : {self.__nome}")

class Studentee(Persona):
     def __init__(self, nome,corso):
          super().__init__(nome)
          self.corso=corso
     def presentati(self):
        print(f"Il mio nome e : {self.get_nome()} e il mio corso e {self.corso} ")

Persona1=Persona("Paolo")
Persona1.presentati()

Studente1=Studentee("Peppe","Informatcia")
Studente1.presentati()

Studente1.set_nome("Giuseppe")
Studente1.presentati()

Studente1.set_nome("")
Studente1.presentati()

#Esecizio 3

class Studenteee():
     scuola="Liceo Classico"
     def __init__(self,nome):
          self.nome=nome
     def presentati(self):
          print(f"Il mio nome e {self.nome} e frequento la scuola {self.scuola}")

     @classmethod
     def cambiascuola(cls,nuova_scuola):
        cls.scuola=nuova_scuola

S=Studenteee("Vittoria")
S2=Studenteee("Pino")
S.presentati()
S2.presentati()
S.cambiascuola("ITIS")
S.presentati()
S2.presentati()

#Esercizio 4

class Studente4():
     def __init__(self,nome,eta):
        self.nome=nome
        self.eta=eta
     def presentati(self):
          return (f"Il mio nome e: {self.nome} e ho {self.eta} anni")

S4=Studente4("Vittoria",19)
S4.presentati()
S4.corso="Biotecnologie"
print(f"{S4.presentati()} e studio {S4.corso}")

#Esercizio 5

class Libro():
     def __init__(self,titolo,autore):
          self.titolo=titolo
          self.autore=autore
     def __str__(self):
          return f"Titolo: {self.titolo}, Autore: {self.autore}"

L=Libro("George Orwell",1984)
print(L)       

#Esercizio 5

class Automobile():
     ruote=4
     def __init__(self,modello):
          self.modello=modello
     def __str__(self):
          return f"Il modello dell auto e : {self.modello} e ha ben {self.ruote} ruote"

A=Automobile("Audi")
B=Automobile("BMW")
print(A.__str__())
print(B.__str__())

#Esercizio 6

class ContoBancario():
     def __init__(self):
          self.__saldo=0
     def deposita(self,importo):
          if importo>0:
               self.__saldo=self.__saldo+importo
          else:
               print("Hai inseirito un valore <0 ")
     def preleva(self,importo):
          if self.__saldo>=importo:
               self.__saldo=self.__saldo-importo
          else:
               print("Saldo insufficiente")
     def get_saldo(self):
          return self.__saldo

c=ContoBancario()
c.deposita(1000)
print(c.get_saldo())
c.deposita(100)
print(c.get_saldo())
c.preleva(100)
print(c.get_saldo())
c.preleva(2000)
print(c.get_saldo())

#Esercizio 7
 
class Animale():
     def __init__(self,nome):
          self.nome=nome
     def verso(self):
          return "Verso sconosciuto"
class Cane(Animale):
     def verso(self):
          return "BAU"
class Gatto(Animale):
     def verso(self):
          return "MIAO"

C=Cane("Canino")
G=Gatto("Gattino")
print(f"{C.nome} fa {C.verso()}")
print(f"{G.nome} fa {G.verso()}")

#Esercizio 8

class Forma():
     def Area(self):
          return 0

class Rettangolo(Forma):
     def __init__(self,base,altezza):
          self.base=base
          self.altezza=altezza
     def Area(self):
          return self.base*self.altezza
class Cerchio(Forma):
     def __init__(self, pi, r):
          self.pi = pi
          self.r = r
     def Area(self):
          return self.pi * self.r ** 2

forme = [
     Rettangolo(5, 3),
     Rettangolo(8, 2),
     Cerchio(3.14, 4),
     Cerchio(3.14, 6)
]
for figura in forme:
     print(f"L area misurata e: {figura.Area()}")

#Esercizio 9
from abc import ABC,abstractmethod
class Veicolo(ABC):
     @abstractmethod
     def muovi(self):
          pass

class Auto(Veicolo):
     def muovi(self):
          return "L auto si muove per strada"
class Aereo(Veicolo):
     def muovi(self):
          return "L aereo si muove in cielo"

def fai_muovere(Veicolo):
     return Veicolo.muovi()

Au=Auto()
Ae=Aereo()
print(fai_muovere(Au))
print(fai_muovere(Ae))

#Esercizio 9

class SStudente():
     def __init__(self,nome,eta,materia):
          self.nome=nome
          self.eta=eta
          self.materia=materia
          
     @classmethod
     def crea_da_stringa(cls,stringa):
          nome,eta,materia=stringa.split("-")
          return cls(nome,int(eta),materia)
     @property
     def anno_nascita(self):
          return 2026-self.eta
     @property
     def eta(self):
          return self.__eta
     @eta.setter
     def eta(self,nuovo_valore):
          if nuovo_valore>=0:
               self.__eta=nuovo_valore
          else:
               print("ERRORE")

S1 = SStudente("Peppe", 23, "Biotecnologie per la Salute")
print(f"{S1.nome} ha {S1.eta} anni, quindi è nato nel {S1.anno_nascita}.")
S2 = SStudente.crea_da_stringa("Luca-20-Matematica")
print(f"{S2.nome} studia {S2.materia} ed è nato nel {S2.anno_nascita}.")
S1.eta = 24
print(f"Compleanno di {S1.nome}! Ora ha {S1.eta} anni e risulta nato nel {S1.anno_nascita}.")
S1.eta = -5  
print(f"L'età di {S1.nome} dopo il tentativo fallito è rimasta: {S1.eta}")
S3 = SStudente("Hacker", -99, "Informatica")