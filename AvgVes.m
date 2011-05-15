close all;
clear all;
n=1;

listOfVessikels = [
    '/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves5.png',
    '/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves6.png',
    '/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves1.jpg',
    '/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves2.jpg',
    '/Users/claesladefoged/Documents/bach_rep/images/vessikels/ves3.jpg'];
AvgCell = zeros(size(double(imread(listOfVessikels(1,:)))));
RotCell = zeros(size(double(imread(listOfVessikels(1,:)))));
for i = 1:(size(listOfVessikels,1))
    'reading vessikels into J'
    J = double(imread(listOfVessikels(i,:)));
    size_avgCell= size(AvgCell)
    size_J = size(J)
    AvgCell = AvgCell+J;
    for j = 1:4
        J = rot90(J,j);
        res = min(size(RotCell),size(J))
        RotCell = RotCell(1:res(1),1:res(2)) + J(1:res(1),1:res(2));
    end
end

AvgCell = round(AvgCell / size(listOfVessikels,1));
RotCell = round(RotCell / size(listOfVessikels,1));

figure(n); n=n+1;
imagesc(AvgCell); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('AvgCell');

figure(n); n=n+1;
imagesc(RotCell); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('RotCell');