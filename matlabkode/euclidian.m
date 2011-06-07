clear all
n=1;
percentage=0.35;
fntsz=18;
I = imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/AN 1-5_7.jpg');
I = double(I(250+[0:400],400+[0:300]));
%I = imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/2-5_7.jpg');
%I = imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/Tv2.jpg');
%I = double(imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/Tv3.jpg'));
%I = double(imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/Tv4.jpg'));
%I = double(imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/Tv7.jpg'));
%I = double(imread('C:\Users\Marcus\Dropbox\Bachelor\Billeder\csgb2/Tv8.jpg'));
%I = double(I(300+[0:700],1+[0:700]));


figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Template image');


gray = mat2gray(I);
X = gray2ind(gray, 256);
imwrite(X, 'orig.jpg')

J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\1-5_7-1.png'));


%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv4-1.png'));
%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv4-2.png'));
%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv4-3.png'));
%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv8-1.png'));
%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv8-2.png'));
%J = double(imread('C:\Users\Marcus\Dropbox\Bachelor\vesikler\Tv8-3.png'));

fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
K=nlfilter(I,size(J),fun);

gray = mat2gray(K);
X = gray2ind(gray, 256);
imwrite(X, 'dist.jpg')
   
for threshold = 1:99
    percentage = threshold/100;

    BNW = (K-min(K(:)))<percentage*(max(K(:))-min(K(:))); 
    gray = mat2gray(BNW);      
    X = gray2ind(gray, 256);
    imwrite(X, strcat(num2str(percentage),'.jpg'))
    %imwrite(imadjust(BNW),strcat(num2str(threshold),'.png'),'png');
end

