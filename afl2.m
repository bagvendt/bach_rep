function [ out ] = afl2 ( IMG, D0, D1 )
    [n,m] = size(IMG);
    x = floor(n/2);
    y = floor(m/2);
    out = IMG;
    for u = 1:n
        for v = 1:m
                if sqrt((u-x)^2+(v-y)^2) < D0 && sqrt((u-x)^2+(v-y)^2) > D1
                    out(u,v) = 0;
                end
        end
    end
end