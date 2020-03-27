from tkinter import*;
from tkinter import messagebox;
#@author Guillermo Gerardo Andres Urbano 


class Contacto():
	"""Representacion del contacto de la genda"""
	def __init__(self, nombre, apellidoPaterno, apellidoMaterno, telefono):
		self.nombre = nombre;
		self.apellidoPaterno = apellidoPaterno;
		self.apellidoMaterno = apellidoMaterno;
		self.telefono = telefono;

	def getNombre(self):
		return self.nombre;
	def getApellidoPaterno(self):
		return self.apellidoPaterno;
	def getApellidoMaterno(self):
		return self.apellidoMaterno;
	def getTelefeno(self):
		return self.telefono;

	def setNombre(self, nombre):
		self.nombre = nombre;
	def setApellidoPaterno(self, apellidoPaterno):
		self.apellidoPaterno = apellidoPaterno;
	def setApellidoMaterno(self, apellidoMaterno):
		self.apellidoMaterno = apellidoMaterno
	def setTelefeno(self, telefono):
		self.telefono = telefono;

	def __str__(self):
		"""Muestra a al contacto"""
		return str(self.apellidoPaterno) + " " + str(self.apellidoMaterno) + " " + str(self.nombre) + " Telefono: " + str(self.telefono);

	def equals(self, otro):
		if(self.nombre == otro.nombre and self.apellidoPaterno == otro.apellidoPaterno and self.apellidoMaterno == otro.apellidoMaterno and self.telefono == otro.telefono):
			return True;
		return False;

	def __cmp__(self, otro):

		if(self.getApellidoPaterno() < otro.getApellidoPaterno()):
			return -1;
		elif(self.getApellidoPaterno() > otro.getApellidoPaterno()):
			return 1;
		else:
			return 0;

#Estos son los que sirve en python 3.7
	def __gt__(self, otro):
		return self.getApellidoPaterno().upper() > otro.getApellidoPaterno().upper();

	def __ge__(self, otro):
		return self.getApellidoPaterno().upper() >= otro.getApellidoPaterno().upper();

	def __eq__(self, otro):
		return self.getApellidoPaterno().upper() == otro.getApellidoPaterno().upper();


def intercambiar(A, x, y):
	tmp = A[x];
	A[x] = A[y];
	A[y] = tmp;


def particionar(lista, p, r):
	i = p - 1;
	x = lista[r];
	for j in range(p, r):
		if(lista[j] <= x):
			i = i + 1;
			intercambiar(lista, i, j);
	intercambiar(lista, i + 1, r);
	return i + 1;


def quicksort(lista , p, r):
	if(p < r):
		q = particionar(lista, p, r);
		quicksort(lista, p, q -1);
		quicksort(lista, q+1, r);


class Gui():
	"""docstring for GUI"""
	def __init__(self, raiz):
		self.raiz = raiz;
		self.raiz.title("Agenda  autor: Andres Urbano Guillermo GerardoAgenda ");
		self.raiz.geometry("1050x680");
		self.raiz.resizable(False, False);
		self.listaContactos = [];
		self.nombre = StringVar();
		self.apellidoP = StringVar();
		self.apellidoM = StringVar();
		self.telefono = StringVar();
		self.frame1 = Frame(self.raiz).pack();
		self.frame2 = Frame(self.raiz).pack();
		self.agendaL = Label(self.frame1, text = "Agenda").pack();
		self.nombreL = Label(self.frame1, text = "Nombre ").pack();
		self.nombreE = Entry(self.frame1, textvariable = self.nombre).pack();
		self.apellidoPaternoL = Label(self.frame1, text = "Apellido Paterno").pack();
		self.apellidoPaternoE = Entry(self.frame1, textvariable = self.apellidoP).pack();
		self.apellidoMaternoL = Label(self.frame1, text = "Apellido Materno").pack();
		self.apellidoMaternoE = Entry(self.frame1, textvariable = self.apellidoM).pack();
		self.telefonoL = Label(self.frame1, text = "Telefono").pack();
		self.telefonoE = Entry(self.frame1, textvariable = self.telefono).pack();
		self.agregarContactoB = Button(self.frame1, text = "Agregar contacto", command = self.buttonAgregarContacto).pack();
		self.ordenarB = Button(self.frame1, text = "Ordenar", command = self.listenerOrdenar).pack();
		self.mostrarListaB = Button(self.frame1, text = "Mostrar lista", command = self.listenerMostrarLista).pack();
		self.text = Text(self.frame2); 
		self.text.pack();
		self.listaEnPantalla = False;
		pass;

	def listenerOrdenar(self):
		#lista = [2, 8, 7, 1, 3, 5, 6, 4];
		#print(self.listaContactos);
		quicksort(self.listaContactos, 0, len(self.listaContactos) - 1);
		messagebox.showinfo("information","Se ha ordenado la agenda, presione el boton mostrar lista para ver los cambios"); 

	def buttonAgregarContacto(self):
		if(not self.camposCorrectos()):
			messagebox.showerror("error","Debe de rellenar todos los campos de las casillas para poder agregar un contacto");
		else:
			contacto = Contacto(self.nombre.get(), self.apellidoP.get(), self.apellidoM.get(), self.telefono.get());
			#verificar si no hay repetidos
			if(self.estaRepetido(contacto)):
				messagebox.showinfo("information","Este contacto ya lo tienes");  
			else:
				self.listaContactos.append(contacto);
			pass
			
	def listenerMostrarLista(self):
		if(self.listaEnPantalla):
			self.text.destroy();
			self.text = Text(self.frame2);
			self.text.pack();
		self.listaEnPantalla = True;
		titulo = """Apellido Paterno  Apellido Materno  Nombre  Telefono\n """;
		self.text.insert(INSERT, titulo);
		for contacto in self.listaContactos:
			self.text.insert(INSERT, str(contacto) + "\n");
		pass
		self.text.config(state=DISABLED)


	def camposCorrectos(self):
		if(self.nombre.get() == "" or self.apellidoP.get() == "" or self.apellidoM.get() == "" or self.telefono.get() == ""):
			return False;
		return True;

	def estaRepetido(self, contacto):
		for item in self.listaContactos:
			if(item.equals(contacto)):
				return True
		return False;

raiz = Tk();
agenda = Gui(raiz);
raiz.mainloop();