function [ ] = DictOfAwesomeness( )
    close all;
    clear all;
    count = 0;
    base = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
    
    n=1;
    fntsz=18;
    
    
    I = double(imread(strcat(base,'test20_58.jpg')));
    
    figure(n); n=n+1;
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');
    [x y] = ginput(2);
    x = round(x);
    y = round(y);
    % Found a smaller cut.
    I = I(y(1):y(2),x(1):x(2));
    
    close all;
    
    nrOfVessikels = 3;
    
    prompt={'Nr of vessikels to select'};
    defans={'3'};
    fields = {'num'};
    info = inputdlg(prompt, 'How many vessikels do you want to select?', 1, defans);
    if ~isempty(info)              %see if user hit cancel
       info = cell2struct(info,fields);
       nrOfVessikels = str2num(info.num);   %convert string to number
    end
    
    figure(n); n=n+1;
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Subset image');
    [x y] = ginput(nrOfVessikels*2);
    x = floor(x);
    y = ceil(y);
    while nrOfVessikels > 0
        
        x1 = x(nrOfVessikels*2-1);
        y1 = y(nrOfVessikels*2-1);
        x2 = x(nrOfVessikels*2);
        y2 = y(nrOfVessikels*2);
        
        height = y2-y1;
        width = x2-x1;
        
        restx = mod(width,7);
        resty = mod(height,7);
        
        Ves = I(y1:(y2+resty),x1:(x2+restx));

        figure(n); n=n+1;
        imagesc(Ves); axis image; colormap(gray); colorbar
        set(gca,'fontsize',fntsz);
        title('Subset image');
        abe = roipoly();
        
        close all;

        for i = 0:(height/7-1)
            for j = 0:(width/7-1)
                count = count + 1;
                y_from = i*7+1;
                y_to = i*7+7;
                x_from = j*7+1;
                x_to = j*7+7;

                cut_original = double(I(y_from:y_to,x_from:x_to));            

                cut_colored = double(abe(y_from:y_to,x_from:x_to));
                [a,b] = size(cut_colored);
                [x1,y1] = size(cut_original);
                var1 = reshape(cut_colored,1,a*b);
                var2 = reshape(cut_original,1,x1*y1);

                mat(count,1,:) = var2;
                mat(count,2,:) = var1;
            end
        end
        
        nrOfVessikels = nrOfVessikels-1;
        
    end
    
    save('minmis','mat');
    close all;
    
    'Done J0hn'

end



