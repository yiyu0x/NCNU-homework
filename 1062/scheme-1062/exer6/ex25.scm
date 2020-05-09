(define (cons m n)
    (* (expt 2 m)
       (expt 3 n)))

(define (car m)
    (if (= 0 (modulo m 2))
        (+ 1 (car (/ m 2)))
        0))

(define (cdr n)
    (if (= 0 (modulo n 3))
        (+ 1 (cdr (/ n 3)))
        0))
