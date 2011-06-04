close all;
clear all;
for i = 1:10:200
    img = imread('img1.png');
    img = rgb2gray(img);
    img = fft2(img);
    %img = fftshift(img);
    figure,hist(img);
    img = afl2(img,0,200-i);
    figure,hist(img);
    %img = fftshift(img);
    img = ifft2(img);
    figure();
    imagesc(abs(img.^2));
    colormap(gray);
end