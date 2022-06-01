
function [msj]=Raices_Multiples(Xo,Iter,Tol,Fun)
%El comando format long me permite utilizar la m�xima capacidad de almacenamiento de decimales permitidos por la m�quina, de tal modo que el error por redondeo se disminuye, esto se explica al entender que tras cada iteraci�n las cifras que se ir�n contaminando son las �ltimas. Tambi�n pueden ser utilizados los comandos de formato simple o doble.
Xo=input('ingrese el valor inicial: ');
%El comando input me permite asignar a una variable un valor que ingresa el usuario. Xo, es uno de los valores in�ciales que se ingresa para comenzar la b�squeda de ra�ces
Iter=input('ingrese el n�mero de iteraciones: ');
Tol=input('ingrese la tolerancia que desea: ');
Fun=input('ingrese la funcion = ','s');
f=inline(Fun);
%Cuando ingreso funci�n esta se encuentra en un formato simb�lico, que no me sirve para utilizarla en el resto del programa, por esto se utiliza el formato inline, que la transforma y me permite evaluarla.
Y1=f (Xo);
%forma en la que eval�o la funci�n en el valor inicial, y al mismo tiempo le asigno el nombre de Y
Du=input('ingrese la primera derivada = ','s');
Der=inline(Du);
%inline, permite asignar a una variable el valor de una funci�n, para as� utilizarla en el resto del programa
D=Der(Xo);
Du2=input ('ingrese la segunda derivada de la funcion = ','s');
Der2=inline (Du2);
D2=Der2 (Xo);
Error=Tol+1;
%como solo he calculado un valor de X, utilizo cualquier valor que sea mayor que la tolerancia que necesito, para que me contin�e ejecutando el programa, pues cualquier valor que sea mayor que la tolerancia es inadecuado.
Cont=0;
% el contador hasta este momento est� en cero, porque no se ha realizado ninguna operaci�n
Denominador=D^2-(Y1*D2);
%Es necesario definir una variable solo para el denominador, pues se debe evaluar que este sea diferente de cero.
Z=[Cont,Xo,Y1,Error];
%Z, es una matriz en la que se almacenan los resultados de cada una de las iteraciones que realiza el programa.
    while Y1~=0 & Error>Tol & Cont<Iter & Denominador~=0
    %While es un comando que permite de manera repetitiva ejecutar un    estamento mientras la condici�n sea verdadera.
   %Operaciones que me ejecuta el m�todo para llegar a la ra�z
        X1=Xo-((Y1*D)/(D^2-(Y1*D2)));
        Y1=f(X1);
        D=Der(X1);
        D2=Der2(X1);
        Error=abs((X1-Xo)/X1);
        Cont=Cont+1;
        Z(Cont,1)=Cont;
        Z(Cont,2)=Xo;
        Z(Cont,3)=Y1;
        Z(Cont,4)=D;
        Z(Cont,5)=D2;
        Z(Cont,6)=Error;
        Xo=X1;
    end
%Eval�o las condiciones de �xito y de fracaso, utilizando el comando if
    if Y1==0
        fprintf('X1 es ra�z: ');
    else
        if Error<Tol
            fprintf('La ra�z es %g con un error de %g: ',X1,Error);
        else
            if Denominador==0
                fprintf('Se est� haciendo divisi�n por cero')
            else
            fprintf('Se llego al m�ximo de Iteraciones: ');
            end           
        end
    end
    fprintf('        Xo,         X1,         Y1,          D,          D2,         Error: ');
    disp(Z);
    %El comando disp muestra el contenido de la matriz Z.
   