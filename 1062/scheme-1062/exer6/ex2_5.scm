(define (num-cons a b)
    (* (expt 2 a) (expt 3 b)))

 
(define (num-car n)
  (if (= 0 (modulo n 2))
      (+ 1 (num-car (/ n 2)))
      0))
 
(define (num-cdr n)
  (if (= 0 (modulo n 3))
      (+ 1 (num-cdr (/ n 3)))
      0))
