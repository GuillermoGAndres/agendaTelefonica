from tkinter import*;
from tkinter import messagebox;
from functools import partial;


def listenerOrdenar(lista): 
	#list - contiene los numeros pero de modo cadena, utilizando el metodo lista.get()
	if(listaCorrecta(lista)):
		#mostrar lista originlal
		#frame4
		#-----------------------
		frame4 = Frame(raiz);
		resultados = Label(frame4, text = "Resultados").pack();
		listaOriginal = Label(frame4, text = "Lista Original").pack();
		listaO = Label(frame4);
		listaNumeros = [];
		toString = "[ "
		for item in lista:
			toString += item.get() + ", ";
			listaNumeros.append(int(item.get()));
		toString += " ]";
		listaO.config(text = toString); #colocando texto en la etiqueta
		listaO.pack();

		labelListaFinal = "Lista ordenada";
		if(radio.get() == 1):
			listaOrdenada = bubble_sort(listaNumeros);
			labelListaFinal += " con BubbleSort";
		elif(radio.get() == 2):
			listaOrdenada = merge_sort(listaNumeros);
			labelListaFinal += " con MergeSort";

		labelListaOrde = Label(frame4, text = labelListaFinal);
		labelListaOrde.pack();
		labelListaOrdena = Label(frame4, text = str(listaOrdenada));
		labelListaOrdena.pack();
		frame4.pack();


def estaRepetido(elemnt, lista):
	count = 0;
	for item in lista:
		if(elemnt == item.get()):
			count+= 1;
	return count > 1;


def listaCorrecta(lista):
	for x in lista:
		if(x.get() == ""): #verifica el contenido de las cajas
			#print("Le falta escribir numeros en la casillas")
			messagebox.showerror("error","Debe de rellenar todos los numeros de las casillas para poder ordenar"); 
			return False;
		elif(estaRepetido(x.get(), lista)):
			messagebox.showerror("error","No se puede repetir los numeros, favor de escribir reescribir");
			return False;
	return True;



def bubble_sort(lista):
	tam = len(lista) - 1;
	for x in lista:
		for i in range(0, tam):
			if(lista[i] > lista[i+1]):
				tmp = lista[i];
				lista[i] = lista[i+1];
				lista[i+1] = tmp
		tam-=1;
	return lista;



def merge_sort(lista):
	if(len(lista) < 2):
		return lista;
	medio = int(len(lista)/2);
	izq = merge_sort(lista[:medio]);
	der = merge_sort(lista[medio:]);
	return merge(izq, der);

def merge(lista1, lista2):
	i, j = 0, 0;
	resultado = [];
	while(i < len(lista1) and j < len(lista2)):
		if(lista1[i] < lista2[j]):
			resultado.append(lista1[i]);
			i += 1;
		else:
			resultado.append(lista2[j]);
			j += 1;

	resultado += lista1[i:];
	resultado += lista2[j:];

	return resultado;


def listenerBotonIngresar(number, raiz):
	if(number.get() == ""):
		#print("Tienes que poner un numero");
		messagebox.showwarning("warning","Caja vacia! Tienes que poner un numero del 1 a 20");
	elif ( int(number.get()) > 20 or int(number.get()) <= 0 ):
		messagebox.showwarning("warning","Rango invalido! Tienes que poner un numero del 1 a 20");
	else:
		#buttonIngresar.config(state = "disabled");
		#print(number.get());
		listaCajasText = [];
		#Cajas que contendran los valores
		for i in range(1, int(number.get()) + 1):
			listaCajasText.append(StringVar());
		#Frame3
		#--------------------------
		frame3 = Frame(raiz);
		for num in range(0, int(number.get())):
			frameAux2 = Frame(frame3); #Esto es para que se vea mas bonito poniendo en horizontal
			label = Label(frameAux2, text = "Elemento " + str(num + 1)).pack(side = LEFT);
			caja = Entry(frameAux2, textvariable = listaCajasText[num], width = 5).pack(side = RIGHT);
			frameAux2.pack();

		listenerOrdenar2 = partial(listenerOrdenar,listaCajasText);
		buttonOrdenar = Button(frame3, text = "Ordenar", command = listenerOrdenar2,activebackground = "gray").pack();
		frame3.pack()
		#---------------------------------------
	



raiz = Tk();	
raiz.title("Bubble sort and Merge sort");
raiz.geometry("800x800");

#Frame1
#---------------------------------
frame1 = Frame(raiz);
titulo = Label(frame1, text = "Selecccione el metodo de ordenamiento");
titulo.pack();
radio = IntVar() #es un valor especial de tkinter para los radioButtons
frameAux = Frame(frame1); #este frame es para que sea mas bonito y aparezca los botones izquierda y derecha
#ListenerSeleccion = partial(seleccion, radio);
buttonBubble = Radiobutton(frameAux, text = "Burbuja", variable = radio, value = 1);
buttonBubble.select();
buttonMerge = Radiobutton(frameAux, text = "Mezcla", variable = radio, value = 2);
buttonBubble.pack(side = LEFT);
buttonMerge.pack(side = RIGHT);
frameAux.pack();
frame1.pack();
#Fin de frame1
#----------------------------------

#Frame2 
#-------------------------------------
frame2 = Frame(raiz);
numeroElemento = Label(frame2, text = "Numero de Elementos ").grid(row = 1, column = 0);
respuestaCaja = StringVar() # es es igual = tkinter.StringVar()
box = Entry(frame2, textvariable = respuestaCaja).grid(row = 1, column = 1);
listenerButonI = partial(listenerBotonIngresar, respuestaCaja, raiz);
buttonIngresar = Button(frame2, text = "Ingresar datos", command = listenerButonI,activebackground = "gray").grid(row = 2, column = 0);
frame2.pack();
#Fin de frame2
#------------------------------


	

raiz.mainloop();