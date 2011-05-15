close all;
clear all;
n=1;
fntsz=18;

%I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
%?I = double(I(400+[0:255],1100+[0:255]));

%width = 35;  %<-- ---ORIGIN
%height = 28; %<-- /
width = 70;
height = 63;
I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
I = double(I(465+[0:height-1],1100+[0:width-1]));

NewI = I.*0;


figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');

[h,w] = size(I);

% For each height pixel except the last 7 (size of cut)
for i = 1:(h-7)
    strcat(num2str(round((i/(h-7))*100)),'%')
    % For each width pixel except the last 7
    for j = 1:(w-7)
        cut = double(I(i+[0:7],j+[0:7]));
        shortest_dist = 10^10;
        shortest_name = '';
        % Run through each cut with x
        for x = 0:3
            % Run through each cut with y
            for y=0:4
                name1 = ['orig_',num2str(x),'_',num2str(y),'.txt'];
                patch = load(name1);
                dist = 0;
                for a=1:7
                    for b=1:7
                        dist = dist + (patch(a,b)-cut(a,b))^2;
                    end
                end
                dist = sqrt(dist);
                if (dist < shortest_dist)
                    shortest_dist = dist;
                    shortest_name = ['new_',num2str(x),'_',num2str(y),'.txt'];
                end
            end
        end
        % We have found shortest cut with name 'shortest_name' and dist
        % 'shortest_dist'. We then add each pixel value.
        newPatch = load(shortest_name);
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