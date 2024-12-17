(define (problem puzzle-8)
    (:domain puzzle)
    (:objects
        n1 n2 n3 n4 n5 n6 n7 n8 - tile
        c11 c12 c13 c21 c22 c23 c31 c32 c33 - position
    )

    (:init
        (adjacent c11 c12) (adjacent c11 c21)
        (adjacent c12 c11) (adjacent c12 c13) (adjacent c12 c22)
        (adjacent c13 c12) (adjacent c13 c23)

        (adjacent c21 c11) (adjacent c21 c22) (adjacent c21 c31)
        (adjacent c22 c21) (adjacent c22 c12) (adjacent c22 c23) (adjacent c22 c32)
        (adjacent c23 c13) (adjacent c23 c22) (adjacent c23 c33)

        (adjacent c31 c21) (adjacent c31 c32)
        (adjacent c32 c31) (adjacent c32 c33) (adjacent c32 c22)
        (adjacent c33 c23) (adjacent c33 c32)

        ; initial state
        (at n7 c11) (at n2 c12) (at n4 c13)
        (at n5 c21) (empty c22) (at n6 c23)
        (at n8 c31) (at n3 c32) (at n1 c33)
    )

    (:goal (and
        (at n1 c11) (at n2 c12) (at n3 c13)
        (at n4 c21) (at n5 c22) (at n6 c23)
        (at n7 c31) (at n8 c32) (empty c33)
    ))
)