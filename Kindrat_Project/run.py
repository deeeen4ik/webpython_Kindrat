from app import create_app

app = create_app(config_name='local')

if __name__ == "__main__":
    app.run()