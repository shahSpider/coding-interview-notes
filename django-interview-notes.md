# DJANGO INTERVIEW NOTES

## MVT Architecture

#### Django uses:
    Model → View → Template


#### Middleware
    Request → Middleware → View
    Response → Middleware → User

#### Examples:
    Authentication
    Logging
    Security

## Django Request Lifecycle
    Request arrives
    URL routing
    Middleware
    View
    ORM
    Template/JSON response


## select_related vs prefetch_related
    Avoid N+1 query problem.

    ### ForeignKey
    select_related()

    Single JOIN query.

    ### ManyToMany
    prefetch_related()

    Multiple optimized queries.

    Caching

### Purpose:
    Reduce database hits.

#### Types:
    Local memory
    Redis
    Memcached