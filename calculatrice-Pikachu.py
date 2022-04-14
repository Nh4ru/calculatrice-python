# Importation de la bibliothèque Tkinter
from tkinter import *

# Définition de la variable fenêtre
fenetre = Tk()

# Definition du titre de la fenêtre
fenetre.title("Cas tkinter")

# Configuration de la taille de la fenêtre
#fenetre.configure(bg="purple")
fenetre.geometry("500x500")
fenetre.resizable(width=False, height=False)
photo = PhotoImage(file='images\pikachu.png')
label = Label(fenetre, image=photo)
label.place(x='0', y='0')


# FONCTIONS



def addition():
    text_valeur1 = int(input1.get())
    text_valeur2 = int(input2.get())
    resultat = text_valeur1+text_valeur2
    input3.insert(0,resultat)
    
def soustraction():
    text_valeur1 = int(input1.get())
    text_valeur2 = int(input2.get())
    resultat = text_valeur1-text_valeur2
    input3.insert(0,resultat)
    

def multiplication():
    text_valeur1 = int(input1.get())
    text_valeur2 = int(input2.get())
    resultat = text_valeur1*text_valeur2
    input3.insert(0,resultat)
    

def division():
    text_valeur1 = int(input1.get())
    text_valeur2 = int(input2.get())
    resultat = text_valeur1/text_valeur2
    input3.insert(0,resultat)

def clear():
    input1.delete(0, END)
    input2.delete(0, END)
    input3.delete(0, END)
    
   
# Définition des valeurs
valeur1 = Label(fenetre, text="Première valeur", width=20)
valeur2 = Label(fenetre, text="Deuxième valeur", width=20)
resultat = Label(fenetre, text="Résultat", width=20)

# Définition variable
#phrase = StringVar()
valeur_nombre1 = IntVar()
valeur_nombre2 = IntVar()

# Création des éléments
input1 = Entry(fenetre, width=20)
input2 = Entry(fenetre, width=20)
input3 = Entry(fenetre, width=20)

#text1 = Label(fenetre, text=phrase)

#def show_text():
#   text1 = Label(fenetre, text=phrase.get())
#   text1.grid(row=1, padx=20, pady=20)
#   input1.delete(0, END)



bouton1 = Button(fenetre, text="+", command=addition, bg="red", fg="blue")
bouton2 = Button(fenetre, text="-", command=soustraction, bg="yellow", fg="blue")
bouton3 = Button(fenetre, text="*", command=multiplication, bg="red", fg="blue")
bouton4 = Button(fenetre, text="/", command=division, bg="yellow", fg="blue")
bouton5 = Button(fenetre, text="Clear", command=clear, width=20, bg="red", fg="blue")

# Placement des éléments

bouton1.grid(row=0, column=3, padx=20, pady=20)
bouton2.grid(row=1, column=3, padx=20, pady=20)
bouton3.grid(row=2, column=3, padx=20, pady=20)
bouton4.grid(row=3, column=3, padx=20, pady=20)
bouton5.grid(row=8, column=1, padx=20, pady=20)

valeur1.grid(row=0, column=0, padx=20, pady=20)
valeur2.grid(row=1, column=0, padx=20, pady=20)

input1.grid(row=0, column=1, padx=20, pady=20)
input2.grid(row=1, column=1, padx=20, pady=20)
input3.grid(row=2, column=1, padx=20, pady=20)

resultat.grid(row=2, column=0, padx=20, pady=20)

# Lancement de la fenêtre
fenetre.mainloop()