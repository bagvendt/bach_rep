function [ out ] = removeNeighbours(in,i,j,patchsize)
        out = in;
%         out(i,j) = 0;
%         if(out(i+1,j) > 0)
%             removeNeighbours(out,i+1,j);
%         end
%         if(out(i,j+1) > 0)
%             removeNeighbours(out,i+1,j);
%         end
%         if(out(i+1,j+1) > 0)
%             removeNeighbours(out,i+1,j);
%         end
        out(i:i+patchsize,j:j+patchsize) = 0;
end