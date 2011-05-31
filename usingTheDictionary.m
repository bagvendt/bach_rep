function [ ] = usingTheDictionary( )
    close all;
    clear all;

    base = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
    
    fntsz=18;
    
    atomSize = 3;
    
    %I = double(imread(strcat(base,'test20_48.jpg')));
    I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTest.png'));
    %figure(n); n=n+1;
    %imagesc(I); axis image; colormap(gray); colorbar
    %set(gca,'fontsize',fntsz);
    %title('Subset image');
    %[x y] = ginput(2);
    %x = round(x);
    %y = round(y);
    %I = I(y(1):y(2),x(1):x(2));
    %I = double(I(200+[0:255],100+[0:255]));
    
    close all;
    
    buildingTheDictionary(atomSize);
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');

    for i = 1
        NewI = SLD( I, atomSize, i );
    
        figure();
        imagesc(NewI); axis image; colormap(gray); colorbar
        set(gca,'fontsize',fntsz);
        title('New image from dict');
    end

    
end