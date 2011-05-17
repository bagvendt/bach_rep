close all;
clear all;
n=1;
percentage=0.35;
%percentage=0.20;
base1 = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
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

I = I(ly:ry,lx:rx);
figure(n); n=n+1;
imagesc(double(I)); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Cuttet image');

%gausskerne = fspecial('gaussian',[5,5],2)
%gausskerne = Edge(I,'gauss')


%gaussres = filter2(gausskerne,I);'
for i = 1:20
    gaussres = EDGE(I,'log',i);
    size(gaussres);
    figure(n); n=n+1;
    imagesc(gaussres); axis image; colormap(gray); colorbar
end
%[testval1, testval2] = ginput(2);

% 
% iMax = size(listOfVessikels,1);
% for i = 1:(size(listOfVessikels,1))
%     J = double(imread(listOfVessikels(i,:)));
%     figure(n); n=n+1;
%     imagesc(J); axis image; colormap(gray); colorbar
%     set(gca,'fontsize',fntsz);
%     title('Template image');
%     fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
%     K=nlfilter(I,size(J),fun);
%     figure(n); n=n+1;
%     imagesc(K); axis image; colormap(gray); colorbar
%     set(gca,'fontsize',fntsz);
%     title('Distance map');
%     figure(n); n=n+1;
%     blackNWhiteImg = (K-min(K(:)))<percentage*(max(K(:))-min(K(:)));
%     imagesc(blackNWhiteImg); axis image; colormap(gray); colorbar
%     set(gca,'fontsize',fntsz);
%     title(sprintf('Smallest %d%% in distance map',round(percentage*100)));
% end
