;continued fraction calc pi
(define (cont-frac n d k)
   (define (frac-iter i result)
       (if (= i 0)
           result
           (frac-iter (- i 1.0) (/ (n i) (+ (d i) result)))))
   (frac-iter (- k 1.0) (/ (n k) (d k))))
 
(define (calc-pi k)
    (define (d i)
        (- (* 2 i) 1)) ;((2*i)-1)
    (define (n i)
        (if (= i 1)
            4
            (* (- i 1) (- i 1))))
    (cont-frac n d k))
 
(define (inc x)
    (+ x 1))
(define (enough? accuracy index)
    (define next_i index) ;next_i=index
    ;(print "idx:" index " next_i:" (inc next_i) " err:" (- (calc-pi index) (calc-pi (inc next_i))) )
    (if (< (abs (- (calc-pi index) (calc-pi (inc next_i)))) accuracy)
        (calc-pi (inc next_i))          ;true
        (enough? accuracy (inc index))) ;false
)
(define (pi epsilon)
    (enough? epsilon 1))
