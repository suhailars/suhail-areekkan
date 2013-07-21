;tes.rkt
(define left "")
(define right "")
(define codes (make-hash))
(define h (make-hash))
(define tuple empty)
(define tuples empty)
(define tree empty)

(define (freq  str)     
      (for ([ch (in-string str)])
       (if (dict-has-key? h ch)
          (hash-set! h ch (add1(hash-ref h ch)))
          (hash-set! h ch 1)))
    ) 
(freq "malayalam")
(define (sortfreq freqs)
          (begin  (define list1 (hash-keys freqs)) 
                  (for-each (lambda (x)
                            (set! tuple (cons (list (hash-ref h x) x) tuple))) 
                            list1)
                  tuple   ))
                   
(sortfreq h)
(define (buildtree tuple)
   (define least empty)
   (define Rest empty)
   (define branch empty)
   (define combfreq 0)    
   (if (> (length tuple) 1)
    (begin
      (set! least (list (car tuple) (car (cdr tuple))))
      (set! Rest (list-tail tuple 2))
      (set! combfreq  (+ (car (car least)) (car (car (cdr least)))))
      (set! branch (list  combfreq least))
      (set! tuple (append Rest (list branch)))
      (set! tuples (sort tuple #:key car <))
       
      (buildtree tuple) ) 
 
    (begin
         (set! tuples (first tuple))
          tuples ) ) )    
(buildtree tuple)

(define (trimtree tree)
            (begin 
               (define p (second tree))    
               (cond [(char? p) p]
                     [else 
                      (list (trimtree (first p)) (trimtree (second p)))] )))
             
(set! tree (trimtree tuples)) 
(define (assigncodes node [pat ""])
         (if (char? node )
             (hash-set! codes node pat)                        
             (begin
  		   (set! left (string-append pat "0"))	
                   (assigncodes (first node) left) 
                   (set! right (string-append pat "1"))                                            (assigncodes (second node) right)  )))

(assigncodes tree) 
(define (encode str)
         (begin
               (define output "")
               (for ([ch (in-string str)])
                   (set! output (string-append output (hash-ref codes ch)))
                      ) 
               output))
(define l (encode "malayalam"))    
(define (decode tree str)
        (begin
             (define output "")
             (define p tree)
             (for ([bit (in-string str)])
                (begin 
                   (if (equal? bit #\0)
                      (set! p (first p))
                      (set! p (second p)))
                   (when (char? p)
                        (set! output (string-append output (~a p)))
                        (set! p tree))
                      ))
                       output    ))
                  
   
