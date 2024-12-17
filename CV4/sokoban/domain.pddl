;; Domain definition
(define (domain sokoban)
  (:requirements :strips :typing)
  (:types
    location
    box
  )
  (:predicates
    (adjacent ?l1 - location ?l2 - location)
    (free ?l - location)
    (box-at ?b - box ?l - location)
    (person-at ?l - location)
    (target ?l - location)
    (left-of ?l1 - location ?l2 - location)    ; l1 is to the left of l2
    (below ?l1 - location ?l2 - location)      ; l1 is below l2
  )

  (:action move
    :parameters (?from - location ?to - location)
    :precondition (and
      (person-at ?from)
      (free ?to)
      (adjacent ?from ?to)
    )
    :effect (and
      (not (person-at ?from))
      (person-at ?to)
      (free ?from)
      (not (free ?to))
    )
  )

  (:action push-right
    :parameters (?from - location ?box-loc - location ?to - location ?box - box)
    :precondition (and
      (person-at ?from)
      (box-at ?box ?box-loc)
      (free ?to)
      (left-of ?from ?box-loc)
      (left-of ?box-loc ?to)
    )
    :effect (and
      (not (person-at ?from))
      (person-at ?box-loc)
      (not (box-at ?box ?box-loc))
      (box-at ?box ?to)
      (free ?from)
      (not (free ?to))
    )
  )

  (:action push-left
    :parameters (?from - location ?box-loc - location ?to - location ?box - box)
    :precondition (and
      (person-at ?from)
      (box-at ?box ?box-loc)
      (free ?to)
      (left-of ?box-loc ?from)
      (left-of ?to ?box-loc)
    )
    :effect (and
      (not (person-at ?from))
      (person-at ?box-loc)
      (not (box-at ?box ?box-loc))
      (box-at ?box ?to)
      (free ?from)
      (not (free ?to))
    )
  )

  (:action push-up
    :parameters (?from - location ?box-loc - location ?to - location ?box - box)
    :precondition (and
      (person-at ?from)
      (box-at ?box ?box-loc)
      (free ?to)
      (below ?box-loc ?from)
      (below ?to ?box-loc)
    )
    :effect (and
      (not (person-at ?from))
      (person-at ?box-loc)
      (not (box-at ?box ?box-loc))
      (box-at ?box ?to)
      (free ?from)
      (not (free ?to))
    )
  )

  (:action push-down
    :parameters (?from - location ?box-loc - location ?to - location ?box - box)
    :precondition (and
      (person-at ?from)
      (box-at ?box ?box-loc)
      (free ?to)
      (below ?from ?box-loc)
      (below ?box-loc ?to)
    )
    :effect (and
      (not (person-at ?from))
      (person-at ?box-loc)
      (not (box-at ?box ?box-loc))
      (box-at ?box ?to)
      (free ?from)
      (not (free ?to))
    )
  )
)