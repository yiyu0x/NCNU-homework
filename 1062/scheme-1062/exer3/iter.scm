(define (f-odd a b c i n)
    (if (= n i)
        c
        (f-odd (+ (- (* 2 a) b) c)
        a
        b
        (+ i 1)
        n
        ))
)

(define (f-even a b c i n)
    (if (= n i)
        c
        (f-even (+ (* 2 a) b c)
        a
        b
        (+ i 1)
        n
        ))
)

(define (f n)
    (if (< n 0)
        n
        (if (odd? n)
            (f-odd 2 1 0 0 n)
            (f-even 2 1 0 0 n)
        )
    )
)
