function [ NewI ] = SLD( I, atomSize )    
    load('minmis')    

    NewI = I.*0;

    [h,w] = size(I);
    [i1,c,i3] = size(mat);
    for i = 1:(h-atomSize)
        if(mod(round((i/(h-atomSize))*100),10)==0)
            strcat(num2str(round((i/(h-atomSize))*100)),'%')
        end
        for j = 1:(w-atomSize)
            cut = double(I(i+[0:(atomSize-1)],j+[0:(atomSize-1)]));
            cut = reshape(cut,1,i3);
            shortest_dist = 10^10;
            for x = 1:i1
                    patch = mat(x,1,:);
                    dist = 0;
                    for a=1:i3
                       dist = dist + (patch(a)-cut(a))^2;
                    end
                    dist = sqrt(dist);
                    if (dist < shortest_dist)
                        shortest_dist = dist;
                        short = x;
                    end
            end
            newPatch = mat(short,2,:);
            newPatch = reshape(newPatch,1,i3);
            newPatch = reshape(newPatch,atomSize,atomSize);
            NewI(i:(i+atomSize-1),j:(j+atomSize-1)) = NewI(i:(i+atomSize-1),j:(j+atomSize-1))+newPatch;
        end
    end
end

