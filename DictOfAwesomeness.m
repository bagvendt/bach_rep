function [ ] = DictOfAwesomeness( )

    close all;
    clear all;
    n=1;
    fntsz=18;
    
    width = 35;
    height = 28;

    %I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
    %I = double(I(400+[0:255],1100+[0:255]));
    
    I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
    I = double(I(465+[0:height-1],1100+[0:width-1]));
    
    %I = imread('/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/test20_58.jpg');
    %5I = double(I(467+[0:height-1],1108+[0:width-1]));
    
    NewI = I.*0;


    figure(n); n=n+1;
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');
    [x,y] = ginput(2);

    xc = x(1);
    yc = y(1);
    radi = sqrt((x(1)-x(2))^2+(y(1)-y(2))^2);

    for i = 1:(height-1)
        for j = 1:(width-1)
            if(sqrt((i-yc)^2+(j-xc)^2) <= radi)
                NewI(i,j) = 1;
            end
        end
    end

    figure(n); n=n+1;
    imagesc(NewI); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Image with selected vessikel');
    
    for i = 0:(height/7-1)
        for j = 0:(width/7-1)
            y_from = i*7+1;
            y_to = i*7+7;
            x_from = j*7+1;
            x_to = j*7+7;
            
            cut_original = double(I(y_from:y_to,x_from:x_to));
            newname1 = ['orig_',num2str(i),'_',num2str(j),'.txt'];
            dlmwrite(newname1, cut_original, 'delimiter', '\t', 'precision', 6);
            cut_colored = double(NewI(y_from:y_to,x_from:x_to));
            newname2 = ['new_',num2str(i),'_',num2str(j),'.txt'];
            dlmwrite(newname2, cut_colored, 'delimiter', '\t', 'precision', 6);            
        end
    end

end

