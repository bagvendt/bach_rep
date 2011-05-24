function [ ] = rocprep()
    

    close all;
    clear all;
    
    base1 = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base1 = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';

    %I = imread(strcat(base1,'test20_47.jpg'));
    %I = double(I(400+[0:255],100+[0:255]));

    %I = imread(strcat(base1,'test20_70.jpg'));
    %I = double(I(400+[0:155],1000+[0:155]));

    I = imread(strcat(base1,'test20_47.jpg'));
    I = double(I(400+[0:255],100+[0:255]));

    %I = imread(strcat(base1,'test20_58.jpg'));
    %I = double(I(450+[0:69],1100+[0:69]));
    
    % UNCOMMENT THE FOLLOWING IF YOU DONT WISH TO BUILD ALL IMAGES AGAIN.
    %rocPrep2(I);
    load('KSsss');
    
    imagesc(I); colormap(gray);
    
    dims = size(KS);
    percentages = [0.30 0.31 0.32 0.33 0.34 0.35 0.35 0.37 0.38];
    for j = percentages
        convImg = zeros(size(I));
        for i = 1:dims(1)
            K(:,:) = KS(i,:,:);
            percentage = j;
            K2 = (K-min(K(:)))<percentage*(max(K(:))-min(K(:)));
            if sum(sum(K2)) < 400
                convImg = convImg + K2;
            end
        end
        figure;
        rocCalc(I,convImg);
    end

    
            
end

