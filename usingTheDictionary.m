function [ ] = usingTheDictionary( )
    close all;
    clear all;
    
    fntsz=18;
    
    atomSize = 3;
    
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTest.png'));
    I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/RunningMeFuck/imTest.png'));
    
    close all;
    
    buildingTheDictionary(atomSize);
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');

    NewI = SLD( I, atomSize );

    figure();
    imagesc(NewI); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('New image from dict');

    
end