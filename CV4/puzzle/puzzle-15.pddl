(define (problem puzzle-15)
    (:domain puzzle)
    (:objects
        n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 - tile
        c11 c12 c13 c14 c21 c22 c23 c24 c31 c32 c33 c34 c41 c42 c43 c44 - position
    )

    (:init
        (adjacent c11 c12) (adjacent c11 c21)
        (adjacent c12 c11) (adjacent c12 c13) (adjacent c12 c22)
        (adjacent c13 c12) (adjacent c13 c23) (adjacent c13 c14)
        (adjacent c14 c13) (adjacent c14 c24)

        (adjacent c21 c11) (adjacent c21 c22) (adjacent c21 c31)
        (adjacent c22 c21) (adjacent c22 c12) (adjacent c22 c23) (adjacent c22 c32)
        (adjacent c23 c13) (adjacent c23 c22) (adjacent c23 c33) (adjacent c23 c24)
        (adjacent c24 c14) (adjacent c24 c23) (adjacent c24 c34)

        (adjacent c31 c21) (adjacent c31 c32) (adjacent c31 c41)
        (adjacent c32 c31) (adjacent c32 c22) (adjacent c32 c42) (adjacent c32 c33)
        (adjacent c33 c32) (adjacent c33 c23) (adjacent c33 c34) (adjacent c33 c43)
        (adjacent c34 c24) (adjacent c34 c33) (adjacent c34 c44)

        (adjacent c41 c31) (adjacent c41 c42)
        (adjacent c42 c41) (adjacent c42 c43) (adjacent c42 c32)
        (adjacent c43 c42) (adjacent c43 c44) (adjacent c43 c33)
        (adjacent c44 c43) (adjacent c44 c34)

        ; initial state
        (at n3  c11) (at n11 c12) (at n4  c13) (at n15 c14)
        (at n1  c21) (at n13 c22) (empty  c23) (at n12 c24)
        (at n7  c31) (at n14 c32) (at n6  c33) (at n2  c34)
        (at n8  c41) (at n9  c42) (at n5  c43) (at n10 c44)
    )

    (:goal (and
        (at n1  c11) (at n2  c12) (at n3  c13) (at n4  c14)
        (at n5  c21) (at n6  c22) (at n7  c23) (at n8  c24)
        (at n9  c31) (at n10 c32) (at n11 c33) (at n12 c34)
        (at n13 c41) (at n14 c42) (at n15 c43) (empty  c44)
    ))
)