%M�todo de ra�ces m�ltiples


fprintf('                  METODO RAICES MULTIPLES\n\n\n');
%fprintf me permite ingresar comentarios de manera textual que pueden
%orientar al usuario en el uso del programa

format long;
%format long permite utilizar la m�xima capacidad del computador 



Xo=-3;
Iter=500;
Tol=0.0005;
F='3.5*x^2+6.8*x-8';
%input es un comando de solicitud de entrada de datos del usuario.

f=str2sym(F);
%El comando inline permite hacer la asignaci�n posterior de variables en
%una funci�n.

Y1=f(Xo);
Di=diff (F);
%El comando diff permite calcular la derivada de una funci�n.
Der=char(Di);
%regresa los valores a texto
De=inline(Der);
%El comando inline permite hacer la asignaci�n posterior de variables en
%una funci�n.
D=De(Xo);
%Se eval�a la derivada en la X inicial, y as� saber si es adecuada para 
%ejecutar el resto del m�todo.
Di2=diff(F,2);
%El comando diff permite calcular la segunda derivada de una funci�n.
Der2=char(Di2);
%regresa los valores a texto
Deri2=inline (Der2);
%El comando inline permite hacer la asignaci�n posterior de variables en
%una funci�n.
D2=Deri2 (Xo);
Error=Tol+1;
Cont=0;
Denominador=D^2-(Y1*D2);
Z1= [Cont, Xo, Y1, D, Error];
Z= [Cont, Xo, Y1, D, Error];
%Z es una matriz la cual permitira observar lo datos como una tabla a la
%finalizacion del programa

%La sentencia While ejecuta todas las �rdenes mientras la expresi�n sea
%verdadera.
while Y1~=0 & Error>Tol & Cont<Iter & Denominador~=0

X1=Xo-((Y1*D)/(D^2-(Y1*D2)));
Y1=f(X1);
D=De(X1);
D2=Deri2(X1);
Error=abs((X1-Xo)/X1);
Cont=Cont+1;
Z(Cont,1)=Cont;
Z(Cont,2)=Xo;
Z(Cont,3)=Y1;
Z(Cont,4)=D;
Z(Cont,5)=D2;
Z(Cont,6)=Error;
%las z son las posiciones asignadas en la tabla a los resultados que se
% observar�n
Xo=X1;
end

if Y1==0
fprintf('\n\nSOLUCION:\n')
fprintf('%G es ra�z\n\n',Xo);
else
if Error<Tol
fprintf('\n\nSOLUCION:\n')
fprintf( '%g es una aproximacion a una ra�z con una tolerancia %g \n\n',Xo,Tol)
else
if Denominador==0
fprintf('\n\nSOLUCION:\n')
fprintf('Se est� haciendo divisi�n por cero\n\n')
else
fprintf('\n\nSOLUCION:\n')
fprintf('Fracaso en %g iteraciones\n\n',Iter);
end 
end
end
fprintf('TABLA\n\n Cont                   Xn                  f(Xn)              f�(Xn)                f��(Xn)              Error Relativo\n\n');
disp(Z1);
disp(Z);
%La funcion disp permite visualizar la tabla, obtenida de los resultados   de
%la secuencia while

ezplot(f);
%El comando ezplot permite grafica una funci�n.

grid on

%grid on permite observar una cuadricula en la grafica de la funcion.

