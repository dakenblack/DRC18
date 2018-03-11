img = imread('img0401.jpg');
labelled = imread('img0402.bmp');
index = labelled(:,:,1) == 255 & labelled(:,:,3) == 255;
r = img(:,:,1);
g = img(:,:,2);
b = img(:,:,3);
boxplot([r(index), g(index), b(index)]);
title('RGB boxplots');

boundary = [0.25, 0.7];
disp('RED');
bounds = quantile(double(r(index)), boundary);
disp( [bounds(1) - 1.5*(bounds(2) - bounds(1)), bounds(1) + 1.5*(bounds(2) - bounds(1))] )
disp('GREEN');
bounds = quantile(double(g(index)), boundary);
disp([bounds(1) - 1.5*(bounds(2) - bounds(1)), bounds(1) + 1.5*(bounds(2) - bounds(1))])
disp('BLUE');
bounds = quantile(double(b(index)), boundary);
disp([bounds(1) - 1.5*(bounds(2) - bounds(1)), bounds(1) + 1.5*(bounds(2) - bounds(1))])

