close all;
clear all;

base1 = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
%base1 = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
base2 = '/Users/claesladefoged/Documents/bach_rep/images/vessikels/';
%base2 = '/home/marcus/Projekter/bach_rep/images/vessikels/';

n=1;
percentage=0.35;
fntsz=18;

I = double(imread(strcat(base1,'test20_58.jpg')));
figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');
[x y] = ginput(2);

lx = round(x(1));
ly = round(y(1));
rx = round(x(2));
ry = round(y(2));

I = I(ly:(floor(ry/7)*7),lx:(floor(rx/7)*7));
figure(n); n=n+1;
imagesc(double(I)); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Cuttet image');

% convImg = zeros(size(I));
% 
% for i = 0:12
%     name = strcat(strcat(base2,'ves'),strcat(num2str(i),'.png'));
%     J = double(imread(name));
%     fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
%     K=nlfilter(I,size(J),fun);
% 
%     K2 = (K-min(K(:)))<percentage*(max(K(:))-min(K(:)));
%     %figure(n); n=n+1;
%     %imagesc(convImg); axis image; colormap(gray); colorbar
%     %set(gca,'fontsize',fntsz);
%     %title('convImg');
%     if sum(sum(K2)) < 400
%         convImg = convImg + K2;
%     end
% end
% 
% figure(n); n=n+1;
% imagesc(convImg); axis image; colormap(gray); colorbar
% set(gca,'fontsize',fntsz);
% title('convImg');

load('minmis');

NewI = I.*0;

[h,w] = size(I);
[i1,c,i3] = size(mat);

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
        newPatch = mat(short,2,:);
        newPatch = reshape(newPatch,1,i3);
        newPatch = reshape(newPatch,7,7);
        NewI(i:(i+6),j:(j+6)) = NewI(i:(i+6),j:(j+6))+newPatch;
    end
end

figure(n); n=n+1;
imagesc(NewI); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('New image from dict');

% DO CROSS REFERENCE HERE
crossImg = zeros(size(NewI));
%crossImg = convImg;

for i= 1:h
    for j = 1:w
        if(NewI(i,j) > 20)
            crossImg(i,j) = 1;
        end
    end
end

figure(n); n=n+1;
imagesc(crossImg); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('crossImg');