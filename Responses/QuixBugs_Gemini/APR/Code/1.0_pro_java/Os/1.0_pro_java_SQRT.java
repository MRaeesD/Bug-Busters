while (Math.abs(x-approx) * Math.abs(x-approx) > epsilon * epsilon) {
            //this line of code was changed
            approx = 0.5d * (approx + x / approx);
        }
