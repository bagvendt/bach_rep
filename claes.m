close all;
clear all;
n=1;
percentage=0.35;
%percentage=0.20;
fntsz=18;
I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_48.jpg');
I = double(I(200+[0:255],100+[0:255]));
%I = double(imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/celle1.png'));
figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');

listOfVessikels = [
    '/Users/claesladefoged/Desktop/celle1.png',
    '/Users/claesladefoged/Desktop/celle2.png'];

iMax = size(listOfVessikels,1);
for i = 1:(size(listOfVessikels,1))
    J = double(imread(listOfVessikels(i,:)));
    figure(n); n=n+1;
    imagesc(J); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Template image');
    fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
    K=nlfilter(I,size(J),fun);
    figure(n); n=n+1;
    imagesc(K); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Distance map');
    figure(n); n=n+1;
    blackNWhiteImg = (K-min(K(:)))<percentage*(max(K(:))-min(K(:)));
    imagesc(blackNWhiteImg); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title(sprintf('Smallest %d%% in distance map',round(percentage*100)));
end
