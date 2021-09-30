from Router.Router import Router


def routing():
    Router.get("/", "IndexController@index")
    Router.get("/lesson/{lesson}", "IndexController@lesson")
    Router.get("/search", "IndexController@search")
    Router.get("/bookmarks", "IndexController@bookmarks")

    api_routes()


def api_routes():
    Router.post_api("/lesson/bookmark", "IndexController@bookmark")
