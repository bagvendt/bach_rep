function [ ] = DictOfAwesomeness( )
    close all;
    clear all;
    count = 0;
    base = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
    
    n=1;
    fntsz=18;
    
    width = 35;
    height = 28;
    
    I = imread(strcat(base,'test20_58.jpg'));
    I = double(I(465+[0:height-1],1100+[0:width-1]));
    
    NewI = I.*0;

    figure(n); n=n+1;
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');
    abe = roipoly()
    size(abe)
    
    figure(n); n=n+1;
    imagesc(abe); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');    
    
    for i = 0:(height/7-1)
        for j = 0:(width/7-1)
            count = count + 1;
            y_from = i*7+1;
            y_to = i*7+7;
            x_from = j*7+1;
            x_to = j*7+7;
            
            cut_original = double(I(y_from:y_to,x_from:x_to));            
            
            cut_colored = double(abe(y_from:y_to,x_from:x_to));
            [x,y] = size(cut_colored);
            [x1,y1] = size(cut_original);
            var1 = reshape(cut_colored,1,x*y);
            var2 = reshape(cut_original,1,x1*y1);
            
            mat(count,1,:) = var2;
            mat(count,2,:) = var1;
        end
    end
    save('minmis','mat');
    close all;

end



