func soft_threshold(N:Int=1e3){
    var i = linspace(-1, 1, num:N)
    var (x, y) = meshgrid(i, i)
    var z = x^2 + y^2
    z[argwhere(z < 0.5)] = 0
    z[argwhere(z > 0.5)] -= 0.5
}

# comment
