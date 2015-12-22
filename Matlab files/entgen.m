function [ XX, x, xmax ] = entgen( control_parameter, M) 
    

    
    rate_portfolio = 'path to portfolio csv';
    X = csvread(rate_portfolio,1,1);
    rowcount = size(X);
    colcount = rowcount(1,2);
    rowcount = rowcount(1,1);
    relative_precision = (1/100);
    h = (1/rowcount) * ones(1,rowcount);
    w = h*X;
    fun = @(x)-w*x;
    lb = relative_precision*ones(colcount,1);
    ub = 100*ones(colcount,1);
    Aeq = ones(colcount,1)';
    beq = [ 1];
    A = [getEntropy' ];
    b = [(control_parameter)*ones(1,colcount)*getEntropy ];
    x0 = rand(colcount,1);
    x = fmincon(fun,x0,A,b,Aeq,beq,lb,ub);
    
    s = size(control_parameter);
    XX = control_parameter;
    
    XX = M*x;
    xmax = XX(1,1);
    
    XX = XX;
    
end

