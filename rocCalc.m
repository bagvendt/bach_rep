function [ ] = rocCalc( orig,blackNWhite)

    Inew = orig;
    
    [h, w] = size(orig);
    patchsize = 22;
    newImg = zeros(size(blackNWhite));
    newImg2 = zeros(size(blackNWhite));
    for i = 0:(floor(w/patchsize)-1)
        for j = 0:(floor(h/patchsize)-1)
            ys = (j*patchsize+1):((j+1)*patchsize);
            xs = (i*patchsize+1):((i+1)*patchsize);
            if(sum(sum(blackNWhite(ys,xs))) > 0)
                newImg(j*patchsize+1+floor(patchsize/2),i*patchsize+1+floor(patchsize/2)) = 1;
                newImg2(j*patchsize+1+floor(patchsize/2):j*patchsize+1+floor(patchsize/2)+4,i*patchsize+1+floor(patchsize/2):i*patchsize+1+floor(patchsize/2)+4) = 1;
                Inew(j*patchsize+1+floor(patchsize/2):j*patchsize+1+floor(patchsize/2)+4,i*patchsize+1+floor(patchsize/2):i*patchsize+1+floor(patchsize/2)+4) = 255;
            end
        end
    end
    
    i2 = 1;
    while i2+patchsize < w
        if(sum(sum(blackNWhite((j+1)*patchsize:h,(i2:(i2+patchsize))))) > 0)
            newImg((j+1)*patchsize+floor(patchsize/2),i2+floor(patchsize/2)) = 1;
            newImg2((j+1)*patchsize+floor(patchsize/2):(j+1)*patchsize+floor(patchsize/2)+4,i2+floor(patchsize/2):i2+floor(patchsize/2)+4) = 1;
            Inew((j+1)*patchsize+floor(patchsize/2):(j+1)*patchsize+floor(patchsize/2)+4,i2+floor(patchsize/2):i2+floor(patchsize/2)+4) = 255;
        end
        i2 = i2 + patchsize;
    end
    j2 = 1;
    while j2+patchsize < h
        if(sum(sum(blackNWhite(j2:(j2+patchsize),(i+1)*patchsize:w))) > 0)
            newImg(j2+floor(patchsize/2),(i+1)*patchsize+floor(patchsize/2)) = 1;
            newImg2(j2+floor(patchsize/2):j2+floor(patchsize/2)+4,(i+1)*patchsize+floor(patchsize/2):(i+1)*patchsize+floor(patchsize/2)+4) = 1;
            Inew(j2+floor(patchsize/2):j2+floor(patchsize/2)+4,(i+1)*patchsize+floor(patchsize/2):(i+1)*patchsize+floor(patchsize/2)+4) = 255;
        end
        j2 = j2 + patchsize;
    end
    
    newImg3 = orig;
    for i = 1:h
        for j = 1:w
            if(blackNWhite(i,j) > 0)
                newImg3(i:i+4,j:j+4)=255;
            end
        end
    end
    
    
    subplot(2,2,1), imagesc(orig)
    subplot(2,2,2), imagesc(blackNWhite)
    
    subplot(2,2,3), imagesc(newImg3)
    
    colormap(gray);

end

