%Fb=imread('image.png');
Fb=[
    1	0	0	1	0	1;
    1	1	0	1	0	1;
    0	1	0	1	0	1;
    0	0	1	0	1	1;
    1	1	0	1	1	0;
    0	0	1	1	1	0
    ];
m1 = [1 1 0];
%ml = 'MSE vlogs';
d1 = size(m1,2);
d = size(Fb,1);
c = size(Fb,2);
m = 3;
n = 3;
K = [
    1 1 0; 
    1 1 1; 
    0 1 0
    ];
x=int32(c/n);
y=int32(d/m);
Fi = K;
num=1;
for i=1:x*y
    if(num<=d1)
        for j=1:m
            for k=1:n
                Fi(j,k)=Fb(j+n*floor(double(i-1)/floor(c/n)),k+n*mod(i-1,floor(c/n)));
            end
        end
        tam=['F',num2str(i),':'];
        disp(tam);
        disp(Fi);
        % 0<sum(Fi^K)<sum(K)
        tg = SUM(AND(Fi,K));
        tam1 = ['SUM(F',num2str(i),'^K)=',num2str(tg)];
        disp(tam1);
        if((0<tg)&&(tg<SUM(K)))
            tam01=['0<SUM(F',num2str(i),'^K]<SUM(K)'];
            disp(tam01);
            if(mod(tg,2)==m1(num))
                tam2=['SUM(F',num2str(i),'^K]mod 2=',num2str(m1(num)), 'cung chinh bang bit can giau nen ta giu nguyen F',num2str(i)];
                disp(tam2);
            elseif (tg==1)
                go=0;
                while(~go)
                    for j=1:m
                        for k= 1:n
                            if((Fi(j,k)==0)&&(K(j,k)==1))
                                Fb(j+n*floor(double(i-1)/floor(c/n)),k+n*mod(i-1,floor(c/n)))=1;
                                go=1;
                                tam3 = ['chon(', num2str(j),',',num2str(k),')co F (',num2str(j),',',num2str(k),')=0,K(',num2str(j),',',num2str(k)];
                                disp(tam3);
                                break;
                            end;
                        end;
                        if(go)
                            break;
                        end
                    end
                end
            elseif (tg==SUM(K)-1)
                tam4=['SUM(F',num2str(i),'^K]=SUM[K]-1'];
                disp(tam4);
                go=0;
                while(~go)
                    for j=1:m
                        for k= 1:n
                            if((Fi(j,k)==1)&&(K(j,k)==1))
                                Fb(j+n*floor(double(i-1)/floor(c/n)),k+n*mod(i-1,floor(c/n)))=0;
                                go=1;
                                tam5= ['chon(',num2str(j),',',num2str(k),') co F(',num2str(j),',',num2str(k)];
                                disp(tam5);
                                break;
                            end
                        end
                        if(go)
                            break;
                        end
                    end
                end
            else
                go=0;
                while(~go)
                    for j=1:m
                        for k= 1:n
                            if(K(j,k)==1)
                                Fb(j+n*floor(double(i-1)/floor(c/n)),k+n*mod(i-1,floor(c/n)))=~Fi(j,k);
                                go=1;
                                tam6 =['chon(',num2str(j),',',num2str(k),') co K (',num2str(j),',',num2str(k),')=1',];
                                disp(tam6);
                                break;
                            end
                        end
                        if(go)
                            break;
                        end
                    end
                end
            end
            num=num+1;
        end
    else
        break;
    end
end
if(num<d1)
    disp('thieu dung luong de nhung tin');
end