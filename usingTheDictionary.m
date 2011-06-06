function [ ] = usingTheDictionary( )
    close all;
    clear all;
    
    fntsz=18;
    
    atomSize = 7;
    
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTest.png'));
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTest5.png'));
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New2/imTest9.png'));
    I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New3/imTest.png'));

    close all;
    
    %buildingTheDictionary(atomSize);
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');

    NewI = SLD( I, atomSize );

    figure();
    imagesc(NewI); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('New image from dict');
    
    save('NewI','NewI');
    
    for i = 60:80
         percentage = i/100;
         BNW = (NewI-min(NewI(:)))<percentage*(max(NewI(:))-min(NewI(:))); 
         figure();
         imagesc(BNW); axis image; colormap(gray); colorbar
         set(gca,'fontsize',fntsz);
         title(sprintf('Smallest %d%% in distance map',round(percentage*100)));
    end
end