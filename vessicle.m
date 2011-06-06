n=1;
percentage=0.35;
fntsz=18;
%I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_48.jpg');
I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb2/AN 2-3_7.jpg');
%I = imread('/Users/claesnl/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_48.jpg');
%I = double(I(150+[0:255],60+[0:255]));
I = double(I(200+[0:400],500+[0:350]));

%J4 = I(75:100,120:145); % Vesikel 1 God-finder mange
%J4 = I(140:165,160:185); % Vesikel 2 Finder sig selv og 3 FP ligner det.
%J4 = I(213:233,163:183); % Vesikel 4 Finder meget. Test med threshold.
J4 = I(145:165,135:155); % Vesikel 5 NY VES FRA 2-3_7

%I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_48.jpg');
%I = double(I(500+[0:255],200+[0:255]));
figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');

figure(n); n=n+1;
imagesc(J4); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Template image');

%fun1 = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J1(:)-mean(J1(:)))/std(J1(:))).^2);
%fun2 = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J2(:)-mean(J2(:)))/std(J2(:))).^2);
%fun3 = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J3(:)-mean(J3(:)))/std(J3(:))).^2);
fun4 = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J4(:)-mean(J4(:)))/std(J4(:))).^2);

%K1=nlfilter(I,size(J1),fun1);
%K2=nlfilter(I,size(J2),fun2);
%K3=nlfilter(I,size(J3),fun3);
K4=nlfilter(I,size(J4),fun4);

figure(n); n=n+1;
imagesc(K4); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Distance Map');
   
for threshold = 25:35
    percentage = threshold/100;

    %BNW1 = (K1-min(K1(:)))<percentage*(max(K1(:))-min(K1(:)));
    %BNW2 = (K2-min(K2(:)))<percentage*(max(K2(:))-min(K2(:)));
    %BNW3 = (K3-min(K3(:)))<percentage*(max(K3(:))-min(K3(:)));
    BNW4 = (K4-min(K4(:)))<percentage*(max(K4(:))-min(K4(:))); 
    
    BNW = BNW4;
    figure(n); n=n+1;
    imagesc(BNW); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title(sprintf('Smallest %d%% in distance map',round(percentage*100)));

    Test = I;
    [h w] = size(I);
    for i = 1:h
        for j = 1:w
            if(BNW(i,j) > 0)
                Test(i:i+4,j:j+4)=255;
            end
        end
    end
    figure(n); n=n+1;
    imagesc(Test); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title(strcat('Res combined - ',num2str(percentage)));
end

