(define (square x) (* x x))
(define (sum-of-square-min-two x y z) (cond ((or (<= x y z) (<= y x z)) (+ (square x) (square y)))
                                          ((or (<= y z x) (<= z y x)) (+ (square y) (square z)))
                                          ((or (<= z x y) (<= x z y)) (+ (square z) (square x)))
                                          ((= x y z) (+ (square x) (square x)))))

