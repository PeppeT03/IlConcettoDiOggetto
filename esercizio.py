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