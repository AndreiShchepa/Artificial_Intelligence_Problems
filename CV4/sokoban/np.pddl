;; Problem instance
(define (problem s1)
    (:domain sokoban)
    (:objects
        p box
        l1 l2 l5 l6 l9 l10 l11 l12 l13 l14 l15 l16 l17 l18
    )
    (:init
        (player p)
        (box box)

        ; Adjacency relationships combining horizontal and vertical
        (adj l1 l2) (adj l2 l1)
        (adj l5 l6) (adj l6 l5)
        (adj l9 l10) (adj l10 l9)
        (adj l10 l11) (adj l11 l10)
        (adj l11 l12) (adj l12 l11)
        (adj l13 l14) (adj l14 l13)
        (adj l14 l15) (adj l15 l14)
        (adj l15 l16) (adj l16 l15)
        (adj l17 l18) (adj l18 l17)

        (adj l1 l5) (adj l5 l1)
        (adj l2 l6) (adj l6 l2)
        (adj l5 l9) (adj l9 l5)
        (adj l6 l10) (adj l10 l6)
        (adj l9 l13) (adj l13 l9)
        (adj l10 l14) (adj l14 l10)
        (adj l11 l15) (adj l15 l11)
        (adj l12 l16) (adj l16 l12)
        (adj l13 l17) (adj l17 l13)
        (adj l14 l18) (adj l18 l14)

        ; Initial positions
        (at p l10)
        (at box l15)

        ; Clear spaces
        (clear l1)
        (clear l2)
        (clear l5)
        (clear l6)
        (clear l9)
        (clear l11)
        (clear l12)
        (clear l13)
        (clear l14)
        (clear l16)
        (clear l17)
        (clear l18)
    )

    (:goal (and (at box l2)))
)