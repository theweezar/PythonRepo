function y=AND(Fi,K)
[p,q]=size(K);
tg=K;
for i=1:p
    for j=1:q
        if((Fi(i,j)==1)&&(K(i,j)==1))
            tg(i,j)=1;
        else
            tg(i,j)=0;
        end
    end
end
y=tg;