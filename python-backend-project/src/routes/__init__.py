def set_routes(app):
    from src.controllers import IndexController

    index_controller = IndexController()
    app.add_url_rule('/', view_func=index_controller.get_index)