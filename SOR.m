%SOR: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método Gauss Seidel (relajado), depende del valor de w 


%[E,s] = SOR(x0,A,b,Tol,niter,w);
function [E,s] = SOR(x0,A,b,Tol,niter,w)

    x0=str2double(x0);
    A=str2mat(A);
    b=str2mat(b);
    Tol=str2double(Tol);
    niter=str2double(niter);
	w=str2double(w);

    n(1)=0;
    c=n(1);
    mx=x0';
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);
    E(c+1)=1;
    while error>Tol && c<niter

        T=inv(D-w*L)*((1-w)*D+w*U);
        C=w*inv(D-w*L)*b;
        x1=T*x0+C;
        E(c+2)=norm(x1-x0,'inf');
        error=E(c+2);
        mx=[mx;x1'];
        x0=x1;
        n(c+2)=c+1;
        c=n(c+2);
    end
    if error < Tol
        s=x0;
        fprintf('es una aproximación de la solución del sistmea con una tolerancia= %f',Tol)
    else 
        s=x0;
        fprintf('Fracasó en %f iteraciones',niter) 
    end
    fprintf(', el vector:\n');
    disp(s);
    disp('la tabla de iteraciones es:');
    Tabla=table(n',E',mx,'variableNames',{'n','error n','vector solucion (con orden x1 x2 x3.....xn)'});
    disp(Tabla);
    disp('Matriz de Transición')
    disp(T);
    disp('Radio Espectral Matriz Transición');
    R_esp_T=max(abs(eig(T)));
    disp(R_esp_T)
end