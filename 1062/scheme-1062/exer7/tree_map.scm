
(define l (list 1 (list 2 3 (list 4 5))))

(define (sq x) (* x x))

(define (tree-map f tree)
  (cond ((null? tree) 
          '())
        ((not (pair? tree)) 
          (f tree))
        (else
          (cons (tree-map f (car tree))
                (tree-map f (cdr tree))))))
