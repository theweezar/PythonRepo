function y=AND(MT)
[p,q]=size(MT);
tg=0;
for i=1:p
    for j=1:q
        if MT(i,j)>0
            tg=tg+1;
        end
    end
end
y=tg;