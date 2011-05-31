n=1;
percentage=0.35;
fntsz=18;
I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_48.jpg');
I = double(I(150+[0:255],60+[0:255]));
figure(n); n=n+1;
imagesc(I); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Subset image');
%J = I(75:100,120:145); % Vesikel 1 God-finder mange
%J = I(140:165,160:185); % Vesikel 2 Finder sig selv og 3 FP ligner det.
%J = I(179:204,62:87); % Vesikel 3 Finder kun sig selv
J = I(213:233,163:183); % Vesikel 4 Finder kun sig selv
%J = I(30:50,70:100); % Vesikel 5 Finder MEGET, mest snavs?
%J = I(30:55,75:100); % Vesikel 6, 5 pix lavere end vesikel 5- Finder kun sig selv
%J = I(110:145,50:85);
figure(n); n=n+1;
imagesc(J); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Template image');
fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
%fun = @(x) sum((x(:)-J(:)).^2);
K=nlfilter(I,size(J),fun);
figure(n); n=n+1;
imagesc(K); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title('Distance map');
figure(n); n=n+1;
imagesc((K-min(K(:)))<percentage*(max(K(:))-min(K(:)))); axis image; colormap(gray); colorbar
set(gca,'fontsize',fntsz);
title(sprintf('Smallest %d%% in distance map',round(percentage*100)));
