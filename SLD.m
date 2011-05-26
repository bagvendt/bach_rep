function [ NewI ] = SLD( I, atomSize, thres_dist )

    fntsz=18;
    
    load('minmis')    

    NewI = I.*0;

    [h,w] = size(I);
    [i1,c,i3] = size(mat);

    % For each height pixel except the last 7 (size of cut)
    for i = 1:(h-atomSize)
        if(mod(round((i/(h-atomSize))*100),10)==0)
            strcat(num2str(round((i/(h-atomSize))*100)),'%')
        end
        % For each width pixel except the last 7
        for j = 1:(w-atomSize)
            cut = double(I(i+[0:(atomSize-1)],j+[0:(atomSize-1)]));
            cut = reshape(cut,1,i3);
            shortest_dist = 10^10;
            % Run through each cut with x
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
            % We have found shortest cut with name 'shortest_name' and dist
            % 'shortest_dist'. We then add each pixel value.
            %if(shortest_dist < thres_dist)
                newPatch = mat(short,2,:);
                newPatch = reshape(newPatch,1,i3);
                newPatch = reshape(newPatch,atomSize,atomSize);
                newPatch = round(newPatch*thres_dist/shortest_dist);
                NewI(i:(i+atomSize-1),j:(j+atomSize-1)) = NewI(i:(i+atomSize-1),j:(j+atomSize-1))+newPatch;
            %end
        end
    end
    
    %for threshold = 1:10:100
    %    percentage = threshold/100;
    %    blackNWhiteImg = (NewI-min(NewI(:)))>percentage*(max(NewI(:))-min(NewI(:)));


    %    figure(n); n=n+1;
    %    imagesc(blackNWhiteImg); axis image; colormap(gray); colorbar
    %    set(gca,'fontsize',fntsz);
    %    title('Black and white image');  
    %end


end

