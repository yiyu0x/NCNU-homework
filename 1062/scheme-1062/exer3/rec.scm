(define (f-odd n)
    (if (< n 3)
        n
        (+ (- (* 2 (f-odd(- n 1)))
              (f-odd(- n 2)))
           (f-odd(- n 3)))
    )
)

(define (f-even n)
    (if (< n 3)
        n
        (+ (+ (* 2 (f-even(- n 1)))
              (f-even(- n 2)))
           (f-even(- n 3)))
    )
)

(define (f n)
    (if (odd? n)
        (f-odd n)
        (f-even n)
    )
)
