function [KS] = rocPrep2(I)
    base2 = '/Users/claesladefoged/Documents/bach_rep/images/vessikels/';
    %base2 = '/home/marcus/Projekter/bach_rep/images/vessikels/';
    
    for i = 0:12
        i
        name = strcat(strcat(base2,'ves'),strcat(num2str(i),'.png'));
        J = double(imread(name));
        fun = @(x) sum(((x(:)-mean(x(:)))/std(x(:))-(J(:)-mean(J(:)))/std(J(:))).^2);
        K=nlfilter(I,size(J),fun);
        KS(i+1,:,:)=K;
    end
    save('KSsss','KS');
end

