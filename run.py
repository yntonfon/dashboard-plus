from application.entrypoints.rest import bootstrap_app

app = bootstrap_app()

if __name__ == '__main__':
    app.run()
