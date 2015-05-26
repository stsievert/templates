func soft_threshold(threshold:Float=0.5){
    var i = linspace(-1, 1, num:100)
    var (x, y) = meshgrid(i, i)
    var z = x^2 + y^2 
    z[argwhere(z < threshold)] = 0.0
    z[argwhere(z > threshold)] -= threshold
    return z
}
