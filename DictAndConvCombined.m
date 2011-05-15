close all;
clear all;
n=1;
percentage=0.35;
fntsz=18;

I = double(imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg'));
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

J = double(imread('/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves6.png'));
fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
K=nlfilter(I,size(J),fun);
figure(n); n=n+1;
convImg = (K-min(K(:)))<percentage*(max(K(:))-min(K(:)));
imagesc(convImg); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('convImg');

% DO USE OF DICT HERE

dictImg = I.*0;
[h,w] = size(I);

for i = 1:(h-7)
    strcat(num2str(round((i/(h-7))*100)),'%')
    for j = 1:(w-7)
        cut = double(I(i+[0:7],j+[0:7]));
        shortest_dist = 10^10;
        shortest_name = '';
        for x = 0:3
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
        dictImg(i:(i+6),j:(j+6)) = dictImg(i:(i+6),j:(j+6))+newPatch;
    end
end

figure(n); n=n+1;
imagesc(dictImg); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('dictImg');

% DO CROSS REFERENCE HERE
crossImg = zeros(size(dictImg));
for i = 1:h
    for j = 1:w
        if(convImg(i,j) > 0 && dictImg(i,j) > 17)
            crossImg(i,j) = 1;
        end
    end
end

figure(n); n=n+1;
imagesc(crossImg); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('crossImg');