close all;
clear all;
n=1;
fntsz=18;

%I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
%?I = double(I(400+[0:255],1100+[0:255]));

%width = 35;  %<-- ---ORIGIN
%height = 28; %<-- /
%width = 70;
%height = 63;
load('minmis')
I = imread('/home/marcus/Dropbox/Bachelor/Billeder/csgb/test20_58.jpg');
%I = double(I(465+[0:height-1],1100+[0:width-1]));
I = double(I(400+[0:69],1100+[0:69]));

NewI = I.*0;


figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');

[h,w] = size(I);
[i1,i2,c,i3] = size(mat)

% For each height pixel except the last 7 (size of cut)
for i = 1:(h-7)
    strcat(num2str(round((i/(h-7))*100)),'%')
    % For each width pixel except the last 7
    for j = 1:(w-7)
        cut = double(I(i+[0:6],j+[0:6]));
        cut = reshape(cut,1,i3);
        shortest_dist = 10^10;
        % Run through each cut with x
        for x = 1:i1
            % Run through each cut with y
            for y=1:i2
                
                patch = mat(x,y,1,:);
                dist = 0;
                for a=1:i3
                   dist = dist + (patch(a)-cut(a))^2;
                end
                dist = sqrt(dist);
                if (dist < shortest_dist)
                    shortest_dist = dist;
                    shortx = x;
                    shorty = y;
                end
            end
        end
        % We have found shortest cut with name 'shortest_name' and dist
        % 'shortest_dist'. We then add each pixel value.
        newPatch = mat(shortx,shorty,2,:);
        newPatch = reshape(newPatch,1,i3);
        newPatch = reshape(newPatch,7,7);
        NewI(i:(i+6),j:(j+6)) = NewI(i:(i+6),j:(j+6))+newPatch;
    end
end

figure(n); n=n+1;
imagesc(NewI); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('New image from dict');

%percentage = 0.70;
%blackNWhiteImg = (NewI-min(NewI(:)))<percentage*(max(NewI(:))-min(NewI(:)));

blackNWhiteImg = zeros(size(NewI));
for i = 1:(h-7)
    for j = 1:(w-7)
        if(NewI(i,j) > 17)
            blackNWhiteImg(i,j) = 1;
        end
    end
end

figure(n); n=n+1;
imagesc(blackNWhiteImg); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Black and white image');  