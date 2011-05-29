function [ ] = buildingTheDictionary( atomSize )
    count = 0;
    base = '/Users/claesladefoged/Dropbox/Skole/3/Bachelor/Billeder/csgb/';
    %base = '/home/marcus/Dropbox/Bachelor/Billeder/csgb/';
    
    %atomSize= 5;
    
    fntsz=18;
    
    %I = double(imread(strcat(base,'test20_48.jpg')));
    
    I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTrain.png'));
    
    %figure(n); n=n+1;
    %imagesc(I); axis image; colormap(gray); colorbar
    %set(gca,'fontsize',fntsz);
    %title('Subset image');
    %[x y] = ginput(2);
    %x = round(x);
    %y = round(y);
    %I = I(y(1):y(2),x(1):x(2));
    %I = double(I(200+[0:89],170+[0:44]));
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Train image');
%     
%     nrOfVessikels = 1;    
%     prompt={'Nr of vessikels to select'};
%     defans={'1'};
%     fields = {'num'};
%     info = inputdlg(prompt, 'How many vessikels do you want to select?', 1, defans);
%     if ~isempty(info)              %see if user hit cancel
%        info = cell2struct(info,fields);
%        nrOfVessikels = str2num(info.num);   %convert string to number
%     end
%     
%     close all;
%     
[height, width] = size(I);
height = height-mod(height,atomSize);
width = width-mod(width,atomSize);
%     
%     label_image = zeros(height,width);
%     
%     while nrOfVessikels > 0
%         
%         Ves = I(1:height,1:width);
% 
%         figure(n); n=n+1;
%         imagesc(Ves); axis image; colormap(gray); colorbar
%         set(gca,'fontsize',fntsz);
%         title('Subset image');
%         label_image = label_image + roipoly();
%         
%         close all;
% 
%         
%         nrOfVessikels = nrOfVessikels-1;
%         
%     end

    %label_image = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imGT.png'));
    label_image = zeros(size(I));
    for i = 1:60
        for j = 1:60
            if(j > 30)
               label_image(i,j) = 1;
            end
        end
    end
            
    figure();
    imagesc(label_image); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Label image');
    
    for i = 0:(height-atomSize)
        for j = 0:(width-atomSize)
            count = count + 1;
            y_from = i+1;
            y_to = i+atomSize;
            x_from = j+1;
            x_to = j+atomSize;

            cut_original = double(I(y_from:y_to,x_from:x_to));            

            cut_colored = double(label_image(y_from:y_to,x_from:x_to));
            [a,b] = size(cut_colored);
            var1 = reshape(cut_colored,1,a*b);
            var2 = reshape(cut_original,1,a*b);

            mat(count,1,:) = var2;
            mat(count,2,:) = var1;
        end
    end
    
    save('minmis','mat');
    
    'Dictionary has been build!'

%     train = SLD( I, atomSize, 1 );
%     figure();
%     imagesc(train); axis image; colormap(gray); colorbar
%     set(gca,'fontsize',fntsz);
%     title('Test Image');
    
end