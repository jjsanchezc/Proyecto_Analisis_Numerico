%GaussPiv: Calcula la solución de un sistema de ecuaciones Ax=b, ya sea
% sin pivoteo piv=0, usando pivoteo parcial piv=1 o pivoteo totalpiv=2.
% Donde A es de tamaño nxn y b de tamaño nx1
%NORMA VECTORIAL Infinita es el X mayor absoluto
%norma euclideana es hallar el vector de todas las x
%

function [x, mark] = GaussPiv(A,b,n,Piv,z)
Ab=[A b];
mark=1:1:n;

for k=1:n-1
    if Piv==1
        Ab=pivpar(Ab,n,k);
    elseif Piv==2
        [Ab, mark]=pivtot(Ab,mark,n,k);
    end
    for i=k+1:n
        M=Ab(i,k)/Ab(k,k);
        for j=k:n+1
            Ab(i,j)=Ab(i,j)-M*Ab(k,j);
        end
    end
end
x=sustreg(Ab,n);
EV = abs([linsolve(A,b)-x]);
disp(EV)
EE = norm(EV,z);
disp(EE)

end

