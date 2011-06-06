n=1;
percentage=0.35;
fntsz=18;
I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb2/AN 1-5_7.jpg');
I = double(I(250+[0:400],400+[0:300]));

J = double(imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/vesikler/1-5_7-1.png'));
fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
K=nlfilter(I,size(J),fun);

imwrite(imadjust(K),'dist.png','png');
   
for threshold = 25:35
    percentage = threshold/100;

    BNW = (K-min(K(:)))<percentage*(max(K(:))-min(K(:))); 
    imwrite(imadjust(K),strcat(num2str(threshold),'.png'),'png');
end

