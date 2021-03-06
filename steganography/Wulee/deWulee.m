%Trich xuat
disp('Trich xuat thong tin');
T=Fb;
num=1;
for i=1:x*y
    if(num<=d1)
        for j=1:m
            for k=1:n
                Fi(j,k)=Fb(j+n*floor(double(i-1)/floor(c/n)),k+n*mod(i-1,floor(c/n)));
            end
        end
        tamt = ['F',num2str(i),':'];
        disp(tamt);
        disp(Fi);
        tg= SUM(AND(Fi,K));
        tam1t=['SUM(F',num2str(i),'^K] = ',num2str(tg)];
        disp(tam1t);
        if((0<tg)&&(tg<SUM(K)))
            tam01t = ['0<SUM(F',num2str(i),'^K]<SUM(K)'];
            disp(tam01t);
            if(mod(tg,2)==0)
                tam2t= ['SUM(F',num2str(i),'^K]mod 2 =0 nen bit da giau la 0'];
                disp(tam2t);
            else
                tam3t= ['SUM(F',num2str(i),'^K]mod 2 =1 nen bit da giau la 1'];
                disp(tam3t);
            end
            num=num+1;
        end
    else
        break;
    end
end