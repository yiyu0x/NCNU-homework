


;exer9 enumerating tuples 
(define proc-list
    (lambda (lst f)
        (cond
        	((null? lst) '())
        	(else
        	    (append (f (car lst)) (proc-list (cdr lst) f )))))
) ;proc-list END
(define combine
  (lambda (list1 list2)
    (proc-list list1 (lambda (x)
                     (map (lambda (y) (list x y)) list2))))
) ;combine END
(define enum-tuples
  (lambda (x-lst . y-lst*)
    (cond
      ((null? y-lst*) (map list x-lst)) ;case1: (enum-tuples '(x y z))
      ((null? (cdr y-lst*)) (combine x-lst (car y-lst*))) 
      (else 
            (proc-list x-lst (lambda (x)
                             (map (lambda (y) (cons x y))
                                  (apply enum-tuples y-lst*)))))))
) ;enum-tuples END
