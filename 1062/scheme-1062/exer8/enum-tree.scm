
 ;enumerate tree
(define (enumerate-tree tree)
  (cond ((null? tree) '())
        ((not (pair? tree)) 
              (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))
;use map list a tree to see ex2.30  
;(1) map a tree
(define (lst x) (append x))
(define (map-tree t)
    (enumerate-tree 
        (map (lambda (sub-tree)
             (if (pair? sub-tree)
                 (map-tree sub-tree)
                 (lst sub-tree)))
                t))
)
(define nil '()) 
;p78 accumulate.scm
(define (accumulate op initial sequence) 
    (if (null? sequence) 
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence))))
)
;(2) accumulate a tree
(define (enum-tree t ) 
   (accumulate cons 
               (list)         ;empty list
               (map-tree t))
)
