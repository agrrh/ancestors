# UML

```mermaid
classDiagram
  Name --|> Person
  Event --|> Person
  Relation --|> Person

  class Person {
    +id UUID

    +names list[UUID]
    +events list[UUID]
    +relations list[UUID]
  }

  class Name {
    +id UUID

    +first str
    +middle str
    +family str
  }

  class Event {
    +id UUID

    +class str
    +date date
    +time time
    +date_exact bool
    +body str
  }

  class Relation {
    +id UUID

    +class str
    +peerA UUID
    +peerB UUID
  }

  class View {
    +id UUID

    +node UUID
    +depth int
    +include_classes list[str]
    +exclude_classes list[str]
  }
```


# Models

## Person

Person must have at least one Name.

Person may change a Name.

Person may have multiple Events.

Person may have multiple Relations to other Persons.

## Name

Name must be bound to a single Person.

## Event

Event may be bound to multiple Persons (e.g. marriage).

## Relation

Relation must be bound to two Persons.
