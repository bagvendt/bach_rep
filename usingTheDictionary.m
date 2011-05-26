function [ ] = usingTheDictionary( )
    close all;
    clear all;

    base = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
    
    fntsz=18;
    
    atomSize = 15;
    
    I = double(imread(strcat(base,'test20_48.jpg')));
    
    %figure(n); n=n+1;
    %imagesc(I); axis image; colormap(gray); colorbar
    %set(gca,'fontsize',fntsz);
    %title('Subset image');
    %[x y] = ginput(2);
    %x = round(x);
    %y = round(y);
    %I = I(y(1):y(2),x(1):x(2));
    I = double(I(200+[0:255],100+[0:255]));
    
    close all;
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');

    for i = 100:10:200
        NewI = SLD( I, atomSize, i );
    
        figure();
        imagesc(NewI); axis image; colormap(gray); colorbar
        set(gca,'fontsize',fntsz);
        title('New image from dict');
    end

    
end