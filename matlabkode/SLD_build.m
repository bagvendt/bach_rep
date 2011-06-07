function [ ] = SLD_build( atomSize )
    count = 0;
    atomSize= 3;
    
    fntsz=18;
    
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imTrain.png'));
    %I = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New2/imTrain2.png'));
    I = double(imread('C:\Users\Marcus\Dropbox\Bachelor\FuckMeRunning\New3\imTrain.png'));
    
    figure();
    imagesc(I); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Train image'); 
    [height, width] = size(I);
    height = height-mod(height,atomSize);
    width = width-mod(width,atomSize);
    %label_image = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New/imGT.png'));
    %label_image = double(imread('/Users/claesladefoged/Desktop/FuckMeRunning/New2/imGT.png'));
    label_image = double(imread('C:\Users\Marcus\Desktop\penis\imGT.png'));
    figure();
    imagesc(label_image); axis image; colormap(gray); colorbar
    set(gca,'fontsize',fntsz);
    title('Label image');
    
    for i = 0:(height-atomSize)
        (i/height)*100
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

    %train = SLD( I, atomSize );
    %figure();
    %imagesc(train); axis image; colormap(gray); colorbar
    %set(gca,'fontsize',fntsz);
    %title('Test Image');
    
end
