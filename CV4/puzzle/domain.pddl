(define (domain puzzle)
    (:requirements
        :strips
        :typing
        :equality
        :adl
    )

    (:types
        position
        tile
    )

    (:predicates
        (at ?t - tile ?p - position)
        (empty ?p - position)
        (adjacent ?from ?to - position)
    )

    (:action slide
        :parameters (
            ?t - tile
            ?from ?to - position
        )
        :precondition (and
            (adjacent ?from ?to)
            (empty ?to)
            (at ?t ?from)
        )
        :effect (and
            (not (at ?t ?from))
            (at ?t ?to)
            (empty ?from)
            (not (empty ?to))
        )
    )
)