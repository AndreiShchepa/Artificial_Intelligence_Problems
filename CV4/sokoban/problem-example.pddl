;; Problem instance
(define (problem sokoban-problem)
  (:domain sokoban)
  (:objects
    ; Locations
    loc-1-1 loc-1-2 loc-1-3
    loc-2-1 loc-2-2 loc-2-3 loc-2-4 loc-2-5 loc-2-6
    loc-3-1 loc-3-2 loc-3-3 loc-3-5 loc-3-7
    loc-4-3 loc-4-4 loc-4-5 loc-4-6 loc-4-7
    loc-5-2 loc-5-3 loc-5-4
    loc-6-2 loc-6-3 loc-6-4 loc-6-5 loc-6-6 - location

    ; Boxes
    box1 box2 box3 - box
  )

  (:init
    ; Adjacent relations stay the same as in your example
    (adjacent loc-1-1 loc-1-2) (adjacent loc-1-2 loc-1-1)
    (adjacent loc-1-1 loc-2-1) (adjacent loc-2-1 loc-1-1)
    (adjacent loc-1-2 loc-1-3) (adjacent loc-1-3 loc-1-2)
    (adjacent loc-1-2 loc-2-2) (adjacent loc-2-2 loc-1-2)
    (adjacent loc-1-3 loc-2-3) (adjacent loc-2-3 loc-1-3)
    (adjacent loc-2-1 loc-2-2) (adjacent loc-2-2 loc-2-1)
    (adjacent loc-2-1 loc-3-1) (adjacent loc-3-1 loc-2-1)
    (adjacent loc-2-2 loc-2-3) (adjacent loc-2-3 loc-2-2)
    (adjacent loc-2-2 loc-3-2) (adjacent loc-3-2 loc-2-2)
    (adjacent loc-2-3 loc-2-4) (adjacent loc-2-4 loc-2-3)
    (adjacent loc-2-3 loc-3-3) (adjacent loc-3-3 loc-2-3)
    (adjacent loc-2-4 loc-2-5) (adjacent loc-2-5 loc-2-4)
    (adjacent loc-2-5 loc-2-6) (adjacent loc-2-6 loc-2-5)
    (adjacent loc-2-5 loc-3-5) (adjacent loc-3-5 loc-2-5)
    (adjacent loc-3-5 loc-3-7) (adjacent loc-3-7 loc-3-5)
    (adjacent loc-3-7 loc-4-7) (adjacent loc-4-7 loc-3-7)
    (adjacent loc-4-7 loc-4-6) (adjacent loc-4-6 loc-4-7)
    (adjacent loc-4-6 loc-4-5) (adjacent loc-4-5 loc-4-6)
    (adjacent loc-4-5 loc-4-4) (adjacent loc-4-4 loc-4-5)
    (adjacent loc-4-4 loc-4-3) (adjacent loc-4-3 loc-4-4)
    (adjacent loc-3-5 loc-4-5) (adjacent loc-4-5 loc-3-5)
    (adjacent loc-3-3 loc-4-3) (adjacent loc-4-3 loc-3-3)
    (adjacent loc-3-1 loc-3-2) (adjacent loc-3-2 loc-3-1)
    (adjacent loc-3-2 loc-3-3) (adjacent loc-3-3 loc-3-2)
    (adjacent loc-5-2 loc-5-3) (adjacent loc-5-3 loc-5-2)
    (adjacent loc-5-3 loc-5-4) (adjacent loc-5-4 loc-5-3)
    (adjacent loc-5-2 loc-6-2) (adjacent loc-6-2 loc-5-2)
    (adjacent loc-6-2 loc-6-3) (adjacent loc-6-3 loc-6-2)
    (adjacent loc-6-3 loc-6-4) (adjacent loc-6-4 loc-6-3)
    (adjacent loc-6-4 loc-6-5) (adjacent loc-6-5 loc-6-4)
    (adjacent loc-6-5 loc-6-6) (adjacent loc-6-6 loc-6-5)
    (adjacent loc-5-3 loc-5-4) (adjacent loc-5-4 loc-5-3)
    (adjacent loc-5-3 loc-4-3) (adjacent loc-4-3 loc-5-3)
    (adjacent loc-5-4 loc-4-4) (adjacent loc-4-4 loc-5-4)
    (adjacent loc-2-1 loc-3-1) (adjacent loc-3-1 loc-2-1)

    ; Left-of relations
    (left-of loc-1-1 loc-1-2) (left-of loc-1-2 loc-1-3)
    (left-of loc-2-1 loc-2-2) (left-of loc-2-2 loc-2-3)
    (left-of loc-2-3 loc-2-4) (left-of loc-2-4 loc-2-5)
    (left-of loc-2-5 loc-2-6)
    (left-of loc-3-1 loc-3-2) (left-of loc-3-2 loc-3-3)
    (left-of loc-4-3 loc-4-4) (left-of loc-4-4 loc-4-5)
    (left-of loc-4-5 loc-4-6) (left-of loc-4-6 loc-4-7)
    (left-of loc-5-2 loc-5-3) (left-of loc-5-3 loc-5-4)
    (left-of loc-6-2 loc-6-3) (left-of loc-6-3 loc-6-4)
    (left-of loc-6-4 loc-6-5) (left-of loc-6-5 loc-6-6)

    ; Below relations
    (below loc-2-1 loc-1-1) (below loc-3-1 loc-2-1)
    (below loc-2-2 loc-1-2) (below loc-3-2 loc-2-2)
    (below loc-2-3 loc-1-3) (below loc-3-3 loc-2-3)
    (below loc-4-3 loc-3-3) (below loc-5-3 loc-4-3)
    (below loc-6-3 loc-5-3)
    (below loc-4-4 loc-3-4) (below loc-5-4 loc-4-4)
    (below loc-4-5 loc-3-5) (below loc-5-5 loc-4-5)

    ; Free Locations - same as your example
    (free loc-1-1) (free loc-1-2) (free loc-1-3)
    (free loc-2-1) (free loc-2-3) (free loc-2-4) (free loc-2-5) (free loc-2-6)
    (free loc-3-1) (free loc-3-2) (free loc-3-3) (free loc-3-7)
    (free loc-4-4) (free loc-4-5) (free loc-4-6) (free loc-4-7)
    (free loc-5-2) (free loc-5-3) (free loc-5-4)
    (free loc-6-2) (free loc-6-4) (free loc-6-5) (free loc-6-6)

    ; Box Positions - same as your example
    (box-at box1 loc-2-2) (not (free loc-2-2))
    (box-at box2 loc-3-5) (not (free loc-3-5))
    (box-at box3 loc-4-3) (not (free loc-4-3))

    ; Person Position - same as your example
    (person-at loc-6-3) (not (free loc-6-3))

    ; Target Locations - same as your example
    (target loc-6-4) (target loc-6-5) (target loc-6-6)
  )

  (:goal
    (and
      (or
        (and (box-at box1 loc-6-4) (box-at box2 loc-6-5) (box-at box3 loc-6-6))
        (and (box-at box1 loc-6-4) (box-at box3 loc-6-5) (box-at box2 loc-6-6))
        (and (box-at box2 loc-6-4) (box-at box1 loc-6-5) (box-at box3 loc-6-6))
        (and (box-at box2 loc-6-4) (box-at box3 loc-6-5) (box-at box1 loc-6-6))
        (and (box-at box3 loc-6-4) (box-at box1 loc-6-5) (box-at box2 loc-6-6))
        (and (box-at box3 loc-6-4) (box-at box2 loc-6-5) (box-at box1 loc-6-6))
      )
    )
  )
)