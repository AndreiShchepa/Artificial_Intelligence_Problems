;; Domain definition
(define (domain sokoban)
    (:requirements :strips)
    (:predicates
        (player ?x)           ; x is the player
        (box ?x)             ; x is a box
        (adj ?x ?y)          ; location x is adjacent to y
        (at ?x ?y)           ; object x is at location y
        (clear ?x)           ; location x is clear
    )

    (:action move
        :parameters (?p ?from ?to)
        :precondition (and
            (player ?p)
            (at ?p ?from)
            (adj ?from ?to)
            (clear ?to)
        )
        :effect (and
            (at ?p ?to)
            (clear ?from)
            (not (at ?p ?from))
            (not (clear ?to))
        )
    )

    (:action push
        :parameters (?p ?from ?box_pos ?to)
        :precondition (and
            (player ?p)
            (box ?box_pos)
            (at ?p ?from)
            (adj ?from ?box_pos)
            (adj ?box_pos ?to)
            (at ?box_pos ?box_pos)
            (clear ?to)
        )
        :effect (and
            (at ?p ?box_pos)
            (at ?box_pos ?to)
            (clear ?from)
            (not (at ?p ?from))
            (not (at ?box_pos ?box_pos))
            (not (clear ?to))
        )
    )
)