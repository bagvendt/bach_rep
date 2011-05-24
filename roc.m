function [ ] = roc( )
    
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
    
    rocPrep2(I);
    
            
end

